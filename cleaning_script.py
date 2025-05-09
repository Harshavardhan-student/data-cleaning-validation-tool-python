import pandas as pd
import re
import sqlite3

df = pd.read_csv('data.csv')
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df['email'] = df['email'].str.lower()

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,4}$'
    return bool(re.match(pattern, email))

def is_valid_phone(phone):
    return bool(re.match(r'^[6-9]\d{9}$', str(phone)))

df['valid_email'] = df['email'].apply(is_valid_email)
df['valid_phone'] = df['phone'].apply(is_valid_phone)

conn = sqlite3.connect('cleaned_data.db')
df.to_sql('cleaned_data', conn, if_exists='replace', index=False)
query_result = pd.read_sql_query("SELECT COUNT(*) AS valid_email_count FROM cleaned_data WHERE valid_email = 1", conn)
print(query_result)
conn.close()
