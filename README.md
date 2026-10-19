# ApexPlanet Internship — Task 1: Data Immersion & Wrangling

## 📌 Project Overview

This project is part of my ApexPlanet Internship. The objective is to understand, assess, clean, and transform the UCI Online Retail dataset into an analysis-ready format using Python and Pandas.

The project focuses on identifying data quality issues, handling missing values, removing duplicate records, standardizing data types, and creating useful analytical columns.

## 🎯 Objectives

- Understand the structure of the retail dataset.
- Identify missing values, duplicate records, and unusual transactions.
- Clean and transform the dataset using Python.
- Calculate transaction-level sales.
- Create a data dictionary documenting each column.
- Export a cleaned dataset ready for further analysis.

## 🛠️ Tools & Technologies

- Python
- Pandas
- Jupyter Notebook
- Google Colab
- GitHub

## 📂 Project Files

| File | Description |
|---|---|
| `ApexPlanet_Task1_Clean.ipynb` | Notebook containing data inspection, cleaning, validation, and export steps. |
| `clean_online_retail.py` | Python script for cleaning and transforming the dataset. |
| `data_dictionary.md` | Documentation of column meanings, data types, business relevance, and data quality. |
| `final_cleaned_online_retail.zip` | Compressed archive containing the cleaned retail dataset. |

## 🔍 Data Cleaning & Transformation

The project includes the following operations:

1. Inspect dataset structure, columns, data types, and missing values.
2. Remove exact duplicate records.
3. Standardize column names by removing surrounding spaces.
4. Convert `InvoiceDate` to a datetime format.
5. Convert `Quantity`, `UnitPrice`, and `CustomerID` to numeric types.
6. Fill missing product descriptions with `Unknown`.
7. Preserve missing customer IDs rather than creating artificial values.
8. Create a `Sales` column using `Quantity × UnitPrice`, rounded to two decimal places.
9. Create a `TransactionType` column to categorize transactions.
10. Validate the cleaned dataset and export the results.

## 🏷️ Transaction Classification

The `TransactionType` column uses these rules:

- **Price Adjustment:** Unit price is negative.
- **Return:** Quantity is negative and unit price is not negative.
- **Zero Price:** Unit price is zero and quantity is not negative.
- **Normal:** None of the above conditions apply.

## 📊 Output

The final dataset contains the original retail transaction fields along with two additional columns:

- `Sales`
- `TransactionType`

The cleaned dataset and data dictionary can be used for further exploratory data analysis and business reporting.

## ▶️ How to Run

### Option 1: Google Colab

1. Open `ApexPlanet_Task1_Clean.ipynb` in Google Colab.
2. Upload the original Online Retail dataset when prompted.
3. Run all notebook cells in order.
4. Review the validation results.
5. Download the generated cleaned CSV and data dictionary.

### Option 2: Python Script

Install the required dependencies:

```bash
pip install pandas openpyxl
```

Run the script with the original Excel dataset:

```bash
python clean_online_retail.py --input "Online Retail.xlsx"
```

Or use a CSV source:

```bash
python clean_online_retail.py --input "Online Retail.csv"
```

The script generates the cleaned CSV and Markdown data dictionary in the specified output locations.

## 💡 Learning Outcomes

Through this task, I practiced:

- Data profiling and quality assessment.
- Missing-value handling and duplicate removal.
- Data type conversion and feature creation.
- Pandas-based data transformation.
- Data validation and documentation.
- Version control and project organization using GitHub.

## 👨‍💻 Internship

**Organization:** ApexPlanet Software Pvt. Ltd.  
**Task:** Task 1 — Data Immersion & Wrangling

---

*This project demonstrates the initial stages of a data analytics workflow: understanding, cleaning, transforming, and preparing data for analysis.*
