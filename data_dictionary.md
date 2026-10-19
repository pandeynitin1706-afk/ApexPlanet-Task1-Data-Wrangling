# Data Dictionary — UCI Online Retail

## Dataset overview

- Original dataset rows (from initial profiling): 541,909
- Exact duplicate rows removed during initial cleaning (from initial profiling): 5,268
- Rows in final cleaned dataset: 536,641
- Columns in final cleaned dataset: 10
- The intermediate CSV used as input was already deduplicated; no further duplicate rows were found.

## Data quality and transformation notes

- Exact duplicate rows remaining: 0
- Missing Description values after handling: 0
- Missing CustomerID values retained: 135,037
- Negative Quantity rows: 10,587
- Zero UnitPrice rows: 2,510
- Negative UnitPrice rows: 2
- Invalid/missing InvoiceDate values after conversion: 0
- Missing descriptions are filled with `Unknown`.
- Missing CustomerID values are retained; no customer IDs are fabricated.
- InvoiceDate is parsed as datetime; Quantity, UnitPrice, and CustomerID are numeric.
- Sales = Quantity × UnitPrice, rounded to two decimal places.
- TransactionType precedence: negative UnitPrice → Price Adjustment; otherwise negative Quantity → Return; otherwise zero UnitPrice → Zero Price; otherwise Normal.
- Sales is a transaction-line calculation, not a guarantee of final accounting revenue.

## Column definitions

| Column | Data type | Meaning | Business relevance |
|---|---|---|---|
| InvoiceNo | object | Invoice number; values beginning with C commonly indicate cancelled transactions. | Identify invoices and investigate cancellations or returns. |
| StockCode | object | Code identifying the product. | Group transactions by product. |
| Description | object | Product text description; missing values are represented as Unknown. | Understand which products were purchased. |
| Quantity | int64 | Number of units; negative values can indicate returns. | Measure units sold or returned. |
| InvoiceDate | datetime64[ns] | Date and time of the transaction. | Analyze sales patterns over time. |
| UnitPrice | float64 | Price per unit; the UCI Online Retail dataset uses GBP. | Analyze pricing and calculate transaction value. |
| CustomerID | float64 | Customer identifier; some transactions have no customer ID. | Analyze customer behavior when an ID is available. |
| Country | object | Country associated with the transaction. | Compare transaction activity across countries. |
| Sales | float64 | Quantity multiplied by UnitPrice, rounded to two decimal places. | Estimate transaction line value; negative values can represent returns or adjustments. |
| TransactionType | object | Rule-based label: Price Adjustment, Return, Zero Price, or Normal. Negative UnitPrice takes precedence. | Separate unusual transaction types for review and analysis. |

## Transaction type counts

| Transaction type | Rows |
|---|---:|
| Normal | 524,878 |
| Return | 10,587 |
| Zero Price | 1,174 |
| Price Adjustment | 2 |
