import pandas as pd
import numpy as np
import math
from typing import Optional
from sklearn.model_selection import train_test_split


def extract_ranked_num_and_cat_columns(dictionary):
    # Initialize lists to store the columns
    ranked_columns = []
    num_columns = []
    cat_columns = []

    # Iterate over the dictionary and categorize columns
    for var, info in dictionary.items():
        # Check the type of each column
        if info['type'] == 'rank':
            ranked_columns.append(info['column'])
        elif info['type'] == 'num':
            num_columns.append(info['column'])
        elif info['type'] == 'cat':
            cat_columns.append(info['column'])

    return ranked_columns, num_columns, cat_columns


def num_unique_cols(data: pd.DataFrame, cols: str, num_unique) -> pd.DataFrame:
    "Changes all values above the number of unique items that should be in the columns to NAN"
    data = data.copy(deep=True)
    for c in cols:
        unique_values = data[c].unique()
        
        if len(unique_values) > num_unique:
            if num_unique == 2:
                d = {1: 1, 2: 0}
                data[c] = data[c].map(d).fillna(np.nan)
            else:
                min_value = data[c].min()
                d = {min_value + n: n for n in range(num_unique)}
                data[c] = data[c].map(d).fillna(np.nan)

        if data[c].min() > 0:
            data[c] = data[c] - data[c].min()

    return data


def clean_columns(data, column_dict):
    """
    This function cleans columns in a DataFrame based on a dictionary with column names and properties.
    It handles 'rank' and 'num' columns by replacing out-of-bound values with NaN and 'cat' columns
    by aligning their categories to form a continuous sequence.
    
    :param data: DataFrame containing the data.
    :param column_dict: Dictionary containing column names and their properties.
    :return: Cleaned DataFrame.
    """
    
    # Iterate over each column in the dictionary
    for colV, info in column_dict.items():
        # Check if the column exists in the DataFrame
        col = info['column']
        if col in data.columns:
            max_value = info['unique_values']
                
            # Replace values greater than max_value or less than 0 with NaN
            data[col] = data[col].apply(lambda x: np.nan if x < 0 or x > max_value else x)
            
            if info['type'] == 'cat':
                # Convert to category if not already
                data[col] = data[col].astype('category')
                # Check if the category starts at 1, if not, shift to start from 0
                categories = data[col].cat.categories
                
                if categories.min() != 0:
                    data[col] = data[col].cat.set_categories(range(len(categories)), ordered=True)
                
        else:
            print(f"Column '{col}' not found in DataFrame.")
    
    return data



def split_data(data: pd.DataFrame, train_size: float = 0.7, val_size: float = 0.15, 
    test_size: float = 0.15, random_state: int = 42) -> tuple:
    """
    Split the data into training, validation, and test sets.
    
    Parameters:
    - data: pd.DataFrame - The input data to be split.
    - train_size: float - The proportion of the data to include in the training set.
    - val_size: float - The proportion of the data to include in the validation set.
    - test_size: float - The proportion of the data to include in the test set.
    - random_state: int - The seed used by the random number generator.
    
    Returns:
    - tuple: A tuple containing the training, validation, and test sets as DataFrames.
    """
    assert train_size + val_size + test_size == 1, "The sum of train_size, val_size, and test_size must be 1."
    
    # Split the data into training and temp sets
    train_data, temp_data = train_test_split(data, train_size=train_size, random_state=random_state)
    
    # Calculate the proportion of validation and test sizes relative to the temp set
    val_size_relative = val_size / (val_size + test_size)
    
    # Split the temp set into validation and test sets
    val_data, test_data = train_test_split(temp_data, train_size=val_size_relative, random_state=random_state)
    
    return train_data, val_data, test_data