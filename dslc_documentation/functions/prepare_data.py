import pandas as pd
import numpy as np
import math
from typing import Optional
from sklearn.model_selection import train_test_split
from sklearn.impute import KNNImputer
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import ast


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


def clean_columns(data, column_dict):
    """
    Cleans columns in a DataFrame based on a dictionary with column names and properties.
    
    Handles:
    - 'rank' and 'num' columns by replacing out-of-bound values with NaN.
    - 'cat' columns by aligning their categories to form a continuous sequence starting from 0.
    
    :param data: DataFrame containing the data.
    :param column_dict: Dictionary containing column names and their properties.
                        Format: {key: {'column': col_name, 'type': col_type, 'unique_values': max_value}}
    :return: Cleaned DataFrame.
    """
    data = data.copy(deep=True)  # Create a deep copy to avoid modifying the original DataFrame.
    data = data.apply(pd.to_numeric, errors='coerce')
    
    for col_key, info in column_dict.items():
        col_name = info.get('column')
        col_type = info.get('type')
        max_value = info.get('unique_values')
        
        if col_name not in data.columns or col_name == 'weights':
            if col_name not in data.columns:
                print(f"Column '{col_name}' not found in DataFrame.")
            continue
            
        if col_name == 'RegistrationStatus':
            data[col_name] = data[col_name].replace(3, 2)
            data[col_name] = data[col_name].replace(0, np.nan)
            
        # Replace values out of bounds (less than 0 or greater than max_value) with NaN
        data[col_name] = data[col_name].apply(
            lambda x: np.nan if (pd.notna(x) and (x < 0 or x > max_value)) else x
        )

    return data


def knn_impute(data, column_dict, label_dict, n_neighbors=5):
    """
    Imputes missing values in a DataFrame using KNN imputation and cleans the data
    according to the specifications in the provided dictionaries.
    
    :param data: DataFrame containing the data with missing values.
    :param column_dict: Dictionary specifying column properties (type, unique values, etc.).
    :param label_dict: Dictionary containing label mappings for categorical columns.
    :param n_neighbors: Number of neighbors to consider for KNN imputation.
    :return: Cleaned and imputed DataFrame.
    """
    # Initialize the KNNImputer with a specified number of neighbors
    KNN_imputer = KNNImputer(n_neighbors=n_neighbors)

    # Fit the imputer to the data and transform it
    df_imputed = pd.DataFrame(KNN_imputer.fit_transform(data), columns=data.columns)
 
    # Post-process imputed values based on column type
    for col_id, info in column_dict.items():
        col_name = info['column']
        col_type = info['type']

        if col_type == 'cat':
            # Round to the nearest integer
            df_imputed[col_name] = np.round(df_imputed[col_name])
            
            # Map to the nearest valid label using the label dictionary
            if col_id in label_dict:
                valid_labels = np.array(list(label_dict[col_id]['labels'].keys()))
                df_imputed[col_name] = df_imputed[col_name].apply(
                    lambda x: valid_labels[np.abs(valid_labels - x).argmin()]
                )
            
            # Ensure the column remains as integers
            df_imputed[col_name] = df_imputed[col_name].astype(int)

        elif col_type == 'rank':
            # Round to the nearest integer and clip to the specified range
            unique_vals = info['unique_values']
            df_imputed[col_name] = np.round(df_imputed[col_name])
            df_imputed[col_name] = df_imputed[col_name].clip(0, unique_vals)
            df_imputed[col_name] = df_imputed[col_name].astype(int)

        elif col_type == 'num':
            # For numerical variables, round to 2 decimal places
            df_imputed[col_name] = df_imputed[col_name].round(2)
    
    return df_imputed


def drop_rows_before_year(df, year_column, cutoff_year):
    """
    Drop all rows where the year is lower than the specified cutoff year.

    Parameters:
        df (pd.DataFrame): The DataFrame to modify.
        year_column (str): The column name representing the year.
        cutoff_year (int): The cutoff year; rows with years below this value will be dropped.

    Returns:
        pd.DataFrame: A new DataFrame with the rows removed.
    """
    if year_column not in df.columns:
        raise ValueError(f"Year column '{year_column}' not found in DataFrame.")
    
    return df[df[year_column] >= cutoff_year]

def drop_high_missing_columns(df, missing_threshold=0.5):
    """
    Drops columns with a proportion of missing values exceeding the specified threshold.

    Parameters:
    - df (pd.DataFrame): The input DataFrame to process.
    - missing_threshold (float): The proportion of missing values allowed per column (default is 0.5).

    Returns:
    - pd.DataFrame: The DataFrame with columns dropped.
    - list: A list of column names that were dropped.
    """
    # Calculate the threshold for allowed missing values
    threshold = len(df) * missing_threshold

    # Get the initial columns
    original_columns = set(df.columns)

    # Drop columns with more missing values than the threshold
    df_dropped = df.dropna(axis=1, thresh=threshold)

    # Get the dropped columns
    dropped_columns = list(original_columns - set(df_dropped.columns))

    return df_dropped, dropped_columns


def remove_keys_from_dict(dictionary, key_list, column_key='column'):
    """
    Safely removes keys from a dictionary based on a condition.
    
    Parameters:
    - dictionary (dict): The dictionary to modify.
    - key_list (list): List of values to match for removal.
    - column_key (str): The key to look up inside the dictionary values for comparison.
    
    Returns:
    - dict: The updated dictionary with specified keys removed.
    """
    # Iterate over a list of keys to avoid modifying during iteration
    for key in list(dictionary.keys()):
        if dictionary[key][column_key] in key_list:
            #print(dictionary[key][column_key])
            del dictionary[key]
    return dictionary



def add_swing_voter_column_timeSeries(df, column_labels_time):
    """
    Add a column `swing_voter` to the DataFrame based on the criteria:
    - If `PRE_IntentVote` is 3 or 4, `swing_voter` is True.
    - If `PRE_IntentVote` is 1 or 2 and `VotePresident` flips, `swing_voter` is True.
    - Otherwise, `swing_voter` is False.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        column_labels_time (dict): A dictionary defining columns and their labels.

    Returns:
        pd.DataFrame: The DataFrame with the new `swing_voter` column.
    """
    # Extract column names from the dictionary
    pre_intent_vote_col = column_labels_time["VCF0713"]["column"]  # "PRE_IntentVote"
    vote_president_col = "VotePresident"  # Assuming this column exists in the DataFrame

    # Ensure required columns exist in the DataFrame
    required_columns = [pre_intent_vote_col, vote_president_col]
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Required column '{col}' not found in DataFrame.")

    def is_swing_voter(row):
        """
        Determine if a row qualifies as a swing voter based on the criteria.
        """
        pre_vote = row[pre_intent_vote_col]
        vote_president = row[vote_president_col]

        # If PRE_IntentVote is 3 or 4
        if pre_vote in [3, 4]:
            return True

        # If PRE_IntentVote is 1 or 2 and VotePresident flips
        if pre_vote in [1, 2] and pre_vote != vote_president:
            return True

        # Otherwise, not a swing voter
        return False

    # Apply the function to each row to create the new column
    df["swing_voter"] = df.apply(is_swing_voter, axis=1)

    return df


def knn_impute_nonDict(data, column_dict, label_dict, n_neighbors=5):
    """
    Imputes missing values in a DataFrame using KNN imputation and cleans the data
    according to the specifications in the provided dictionaries.
    
    :param data: DataFrame containing the data with missing values.
    :param column_dict: DF specifying column properties (type, unique values, etc.).
    :param label_dict: DF containing label mappings for categorical columns.
    :param n_neighbors: Number of neighbors to consider for KNN imputation.
    :return: Cleaned and imputed DataFrame.
    """
    # Initialize the KNNImputer with a specified number of neighbors
    KNN_imputer = KNNImputer(n_neighbors=n_neighbors)

    # Fit the imputer to the data and transform it
    df_imputed = pd.DataFrame(KNN_imputer.fit_transform(data), columns=data.columns)
 
    # Post-process imputed values based on column type
    for col_id in column_dict.index:
        col_name = column_dict.loc[col_id]['column']
        col_type = column_dict.loc[col_id]['type']

        if col_type == 'cat':
            # Round to the nearest integer
            df_imputed[col_name] = np.round(df_imputed[col_name])
            
            # Map to the nearest valid label using the label dictionary
            if col_id in label_dict.index:
                valid_labels = np.array(list(ast.literal_eval(label_dict.iloc[0]['labels']).keys()))
                df_imputed[col_name] = df_imputed[col_name].apply(
                    lambda x: valid_labels[np.abs(valid_labels - x).argmin()]
                )
            
            # Ensure the column remains as integers
            df_imputed[col_name] = df_imputed[col_name].astype(int)

        elif col_type == 'rank':
            # Round to the nearest integer and clip to the specified range
            unique_vals = column_dict.loc[col_id]['unique_values']
            df_imputed[col_name] = np.round(df_imputed[col_name])
            df_imputed[col_name] = df_imputed[col_name].clip(0, unique_vals)
            df_imputed[col_name] = df_imputed[col_name].astype(int)

        elif col_type == 'num':
            # For numerical variables, round to 2 decimal places
            df_imputed[col_name] = df_imputed[col_name].round(2)
    
    return df_imputed


def combine_columns_by_group(data, 
                             groups = {
                                'mentionFox': ['Fox'],
                                'mentionABC': ['ABC'],
                                'mentionCNN': ['CNN']
                            }):
    """
    Combines columns with specific substrings into a single column, where the value is 1 
    if any of the columns in the group have a 1, otherwise 0.
    
    :param data: DataFrame containing the data.
    :param groups: A dictionary where the keys are group names (e.g., 'fox', 'abc', 'cnn') 
                   and values are lists of column substrings to be grouped together.
    :return: DataFrame with the new combined columns.
    """
    # Create a copy of the DataFrame to avoid modifying the original
    data_combined = data.copy()

    # Loop through each group and combine columns
    for group, substrings in groups.items():
        # Select the columns that match the substrings for the group
        group_columns = [col for col in data.columns if any(substring in col for substring in substrings)]
        
        # Ensure all selected columns are numeric (if they are categorical, convert them to numeric)
        data_combined[group_columns] = data_combined[group_columns].apply(pd.to_numeric, errors='coerce')

        # Combine the columns: if any of them have a 1, the result will be 1, otherwise 0
        data_combined[group] = data_combined[group_columns].max(axis=1)

        # Drop the original columns used for combining
        data_combined.drop(columns=group_columns, inplace=True)

    return data_combined


def group_top_and_other(data, column, topNum = 10, other_label=83):
    """
    Groups the top 10 categories in a column and assigns the rest to 'Other.'
    
    :param data: DataFrame containing the data.
    :param column: The column to process.
    :param other_label: The numeric value to assign to 'Other.'
    :return: DataFrame with the processed column.
    """
    # Get the top 10 categories
    top_10 = data[column].value_counts().nlargest(topNum).index
    
    # Replace categories not in the top 10 with 'Other'
    data[column] = data[column].apply(lambda x: x if x in top_10 else other_label)
    
    return data

def replace_all_other_cols(data, column, trueVal):
    # Replace categories not trueVal with 'Other'
    data[column] = data[column].apply(lambda x: x if x is trueVal else 0)
    
    return data


def one_hot_cat_cols(data, column_dict, label_dict):
    """
    One-hot encodes categorical columns based on type and renames columns using label mappings.

    Parameters:
        data (pd.DataFrame): The DataFrame to transform.
        col_type_dict (dict): Dictionary defining the type of each column (e.g., 'cat', 'num').
        label_dict (dict): Dictionary defining the label mappings for categorical columns.

    Returns:
        pd.DataFrame: The transformed DataFrame with one-hot encoded columns.
    """
    for col_key, info in column_dict.items():
        col_name = info.get('column')
        col_type = info.get('type')
        max_value = info.get('unique_values', 0)
        
        # Check if the column is categorical
        if col_type == 'cat' and col_name in data.columns:
            # Perform one-hot encoding
            one_hot = pd.get_dummies(data[col_name], prefix=col_name, drop_first=True)
            
            # Rename columns using the label mapping, if provided
            label_map = label_dict.get(col_key)['labels']
            if label_map:
                one_hot = one_hot.rename(
                    columns={f"{col_name}_{key}": f"{col_name}_{label}" for key, label in label_map.items()}
                )
            
            # Drop the original column and append the one-hot columns
            data = pd.concat([data.drop(columns=[col_name]), one_hot], axis=1)
    
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