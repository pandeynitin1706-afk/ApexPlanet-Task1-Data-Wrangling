#!/usr/bin/env python3
"""Clean UCI Online Retail data and create a Markdown data dictionary.
Example: python clean_online_retail.py --input "Online Retail.xlsx"
Dependencies: pandas, openpyxl (for Excel input).
"""
import argparse
from pathlib import Path
import pandas as pd
EXPECTED = ["InvoiceNo","StockCode","Description","Quantity","InvoiceDate","UnitPrice","CustomerID","Country"]
MEANINGS = {
"InvoiceNo":("Invoice number; values beginning with C commonly indicate cancelled transactions.","Identify invoices and investigate cancellations or returns."),
"StockCode":("Code identifying the product.","Group transactions by product."),
"Description":("Product description; missing values are represented as Unknown.","Understand which products were purchased."),
"Quantity":("Number of units; negative values can indicate returns.","Measure units sold or returned."),
"InvoiceDate":("Date and time of the transaction.","Analyze sales patterns over time."),
"UnitPrice":("Price per unit; the UCI dataset uses GBP.","Analyze pricing and calculate transaction value."),
"CustomerID":("Customer identifier; some transactions have no customer ID.","Analyze customer behavior when an ID is available."),
"Country":("Country associated with the transaction.","Compare transaction activity across countries."),
"Sales":("Quantity multiplied by UnitPrice, rounded to two decimal places.","Estimate transaction line value; negative values can represent returns or adjustments."),
"TransactionType":("Rule-based label: Price Adjustment, Return, Zero Price, or Normal. Negative UnitPrice takes precedence.","Separate unusual transaction types for review and analysis.")}
def read_input(path):
    if not path.exists(): raise FileNotFoundError(path)
    if path.suffix.lower() in ('.xlsx','.xls'): return pd.read_excel(path)
    if path.suffix.lower()=='.csv': return pd.read_csv(path)
    raise ValueError('Input must be .xlsx, .xls, or .csv')
def clean(input_path, output_path, dictionary_path):
    df=read_input(input_path); df.columns=df.columns.astype(str).str.strip()
    missing=[c for c in EXPECTED if c not in df.columns]
    if missing: raise ValueError(f'Missing required columns: {missing}')
    rows_before=len(df); duplicates=int(df.duplicated().sum()); df=df.drop_duplicates().copy()
    df['InvoiceDate']=pd.to_datetime(df['InvoiceDate'],errors='coerce')
    for c in ['Quantity','UnitPrice','CustomerID']: df[c]=pd.to_numeric(df[c],errors='coerce')
    df['Description']=df['Description'].fillna('Unknown')
    df['Sales']=(df['Quantity']*df['UnitPrice']).round(2)
    df['TransactionType']='Normal'
    df.loc[df['UnitPrice'].eq(0),'TransactionType']='Zero Price'
    df.loc[df['Quantity'].lt(0),'TransactionType']='Return'
    df.loc[df['UnitPrice'].lt(0),'TransactionType']='Price Adjustment'
    output_path.parent.mkdir(parents=True,exist_ok=True); dictionary_path.parent.mkdir(parents=True,exist_ok=True)
    df.to_csv(output_path,index=False,date_format='%Y-%m-%d %H:%M:%S',float_format='%.2f')
    lines=['# Data Dictionary — UCI Online Retail','','## Dataset overview','',f'- Rows in input: {rows_before:,}',f'- Exact duplicates removed in this run: {duplicates:,}',f'- Rows in output: {len(df):,}',f'- Columns in output: {len(df.columns)}','','## Data quality and transformations','',f'- Exact duplicates remaining: {int(df.duplicated().sum()):,}',f'- Missing Description after handling: {int(df.Description.isna().sum()):,}',f'- Missing CustomerID retained: {int(df.CustomerID.isna().sum()):,}',f'- Negative Quantity rows: {int(df.Quantity.lt(0).sum()):,}',f'- Zero UnitPrice rows: {int(df.UnitPrice.eq(0).sum()):,}',f'- Negative UnitPrice rows: {int(df.UnitPrice.lt(0).sum()):,}','- Description missing values are filled with Unknown; missing CustomerID values are retained.','- Sales = Quantity × UnitPrice, rounded to two decimal places.','- TransactionType precedence: negative UnitPrice → Price Adjustment; otherwise negative Quantity → Return; otherwise zero UnitPrice → Zero Price; otherwise Normal.','','## Column definitions','','| Column | Data type | Meaning | Business relevance |','|---|---|---|---|']
    for c in df.columns:
        meaning,relevance=MEANINGS[c]; vals=[c,str(df[c].dtype),meaning,relevance]
        lines.append('| '+' | '.join(str(v).replace('|',r'\\|') for v in vals)+' |')
    lines+=['','## Transaction type counts','','| Transaction type | Rows |','|---|---:|']
    for label,count in df.TransactionType.value_counts().items(): lines.append(f'| {label} | {int(count):,} |')
    dictionary_path.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(f'Rows: {rows_before:,} -> {len(df):,}; duplicates removed: {duplicates:,}')
    print('Transaction types:\n'+df.TransactionType.value_counts().to_string())
    print('CSV:',output_path.resolve()); print('Dictionary:',dictionary_path.resolve())
if __name__=='__main__':
    p=argparse.ArgumentParser(description='Clean UCI Online Retail dataset')
    p.add_argument('--input',required=True,help='Input .xlsx, .xls, or .csv file')
    p.add_argument('--output',default='final_cleaned_online_retail.csv')
    p.add_argument('--dictionary',default='data_dictionary.md')
    a=p.parse_args(); clean(Path(a.input),Path(a.output),Path(a.dictionary))
