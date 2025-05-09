# 🧹 Data Cleaning & Validation Tool (Python)

This is a simple Python tool that cleans and validates datasets — useful in AI data preparation and quality checks.

## 🚀 Features
- Removes duplicate records
- Handles missing values
- Normalizes text (lowercase conversion)
- Validates email formats
- Validates Indian phone numbers (10-digit)
- Stores cleaned data in SQLite database
- Runs SQL queries to count valid records

## 🛠️ Tech Used
- Python
- Pandas
- Regex
- SQLite3 (SQL)

## 📂 How to Run

1. Install required package:
   ```bash
   pip install pandas
   ```

2. Place your dataset as `data.csv`.

3. Run the cleaning script:
   ```bash
   python cleaning_script.py
   ```

4. Cleaned data will be saved to `cleaned_data.db`.

## 📊 Sample Data (`data.csv`)

| name  | email             | phone      |
|-------|-------------------|------------|
| Harsha| harsha@example.com| 9876543210 |
| Rohit | wrongemail.com    | 1234567890 |
| Priya | priya@example.com | 9123456789 |

## ✅ Sample Output
```
   valid_email_count
0                  2
```
