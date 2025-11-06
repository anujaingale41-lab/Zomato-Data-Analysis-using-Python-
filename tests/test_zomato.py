import pandas as pd
import pytest
import os

# Fixture to load the dataset
@pytest.fixture
def zomato_df():
    path = "zomato.xlsx"
    assert os.path.exists(path), f"{path} not found"
    return pd.read_excel(path)

# Test 1: Dataset should not be empty
def test_dataset_not_empty(zomato_df):
    assert not zomato_df.empty, "Dataset is empty"

# Test 2: Expected columns should be present
def test_expected_columns_exist(zomato_df):
    expected = ['Restaurant Name', 'City', 'Cuisines', 'Average Cost for two', 'Has Online delivery']
    missing = [col for col in expected if col not in zomato_df.columns]
    assert not missing, f"Missing columns: {missing}"

# Test 3: Critical columns should not have nulls
def test_no_nulls_in_critical_columns(zomato_df):
    critical = ['Restaurant Name', 'City']
    for col in critical:
        assert zomato_df[col].notnull().all(), f"Null values found in {col}"

# Test 4: Cost column should be numeric
def test_cost_column_is_numeric(zomato_df):
    assert pd.api.types.is_numeric_dtype(zomato_df['Average Cost for two']), "Cost column is not numeric"

# Test 5: At least one city should be present
def test_multiple_cities_exist(zomato_df):
    assert zomato_df['City'].nunique() > 1, "Only one city found in dataset"
