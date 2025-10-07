import pandas as pd
import re

def load_data(path):
    """Load Excel file from given path."""
    return pd.read_excel(path)

def drop_irrelevant_columns(df):
    """Drop columns with excessive missing values."""
    columns_to_drop = ['Unnamed: 20', 'Cuisines 5', 'Cuisines 6', 'Cuisines 7', 'Cuisines 8']
    df.drop(columns=columns_to_drop, inplace=True, errors='ignore')
    return df

def fill_missing_cuisines(df):
    """Fill missing cuisine columns with 'Unknown'."""
    for col in ['Cuisines', 'Cuisines 1', 'Cuisines 2', 'Cuisines 3', 'Cuisines 4']:
        if col in df.columns:
            df[col].fillna('Unknown', inplace=True)
    return df

def clean_rate_column(df):
    """Convert 'Rate' from '4.1/5' to float."""
    def clean_rate(x):
        try:
            return float(str(x).split('/')[0])
        except:
            return None
    df['Rate'] = df['Rating'].apply(clean_rate)
    return df

def clean_cost_column(df):
    """Remove commas and convert cost to float."""
    df['Cost'] = df['Average_Cost_for_two'].astype(str).str.replace(',', '').astype(float)
    return df

def validate_phone_column(df):
    """Add a column to validate phone numbers (if present)."""
    if 'phone' in df.columns:
        df['phone_valid'] = df['phone'].apply(lambda x: bool(re.match(r'^\+?\d{10,13}$', str(x))))
    return df

def rename_columns(df):
    """Rename columns for clarity."""
    df.rename(columns={
        'Average_Cost_for_two': 'Cost',
        'Rating': 'Rate',
        'Votes': 'Vote_Count'
    }, inplace=True)
    return df

def clean_zomato_data(path):
    """Full cleaning pipeline."""
    df = load_data(path)
    df.drop_duplicates(inplace=True)
    df = drop_irrelevant_columns(df)
    df = fill_missing_cuisines(df)
    df = clean_rate_column(df)
    df = clean_cost_column(df)
    df = validate_phone_column(df)
    df = rename_columns(df)
    return df
