import pandas as pd
import pytest

# Example: Load your dataset
@pytest.fixture
def zomato_data():
    df = pd.read_csv("zomato.csv")
    return df

# Test 1: Check if dataset loads correctly
def test_dataset_loaded(zomato_data):
    assert not zomato_data.empty, "Dataset should not be empty"

# Test 2: Check expected columns exist
def test_expected_columns(zomato_data):
    expected_columns = ['Restaurant Name', 'City', 'Cuisines', 'Average Cost for two', 'Has Online delivery']
    for col in expected_columns:
        assert col in zomato_data.columns, f"Missing column: {col}"

# Test 3: Check for null values in critical columns
def test_null_values(zomato_data):
    critical_columns = ['Restaurant Name', 'City']
    for col in critical_columns:
        assert zomato_data[col].notnull().all(), f"Null values found in {col}"

# Test 4: Check data types
def test_data_types(zomato_data):
    assert zomato_data['Average Cost for two'].dtype in ['float64', 'int64'], "Cost column should be numeric"

# Test 5: Check unique cities
def test_unique_cities(zomato_data):
    cities = zomato_data['City'].unique()
    assert len(cities) > 1, "There should be more than one city in the dataset"
