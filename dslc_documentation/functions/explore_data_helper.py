import pandas as pd
import numpy as np
import importlib
import sys
import os
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from functions import prepare_data
importlib.reload(prepare_data)

from sklearn.preprocessing import StandardScaler, MinMaxScaler
import pandas as pd
import numpy as np

def perturb_dataframe_assumptions(df_dict, dictionary, column_labels, drop_columns, n_neighborhoods, transform_data, cor_feature_selection_threshold, convert_categorical, year_threshold):
    
    df = df_dict[n_neighborhoods]
    
    year_column = dictionary["VCF0004"]["column"]
    cutoff_year = year_threshold
    df = prepare_data.drop_rows_before_year(df, year_column, cutoff_year)
    
    df = prepare_data.add_swing_voter_column_timeSeries(df, column_labels)
    df = df.drop(columns=drop_columns)
    
    dictionary_final = prepare_data.remove_keys_from_dict(dictionary, drop_columns)
    column_labels_final = prepare_data.remove_keys_from_dict(column_labels, drop_columns)
    
    if convert_categorical == 'dummy':
        df = prepare_data.one_hot_cat_cols(df, dictionary_final, column_labels_final)
    
    if transform_data == "standard":
        numerical_features = [dictionary_final[col]["column"] for col in dictionary_final.keys()
                              if dictionary_final[col]["type"] == "rank" or dictionary_final[col]["type"] == "num"]
        scaler = StandardScaler()
        df[numerical_features] = scaler.fit_transform(df[numerical_features])
        df = pd.DataFrame(df, columns=df.columns)  # Restore DataFrame structure
    
    # Correlation feature selection - Remove one column of each highly correlated pair
    if cor_feature_selection_threshold != 0:
        # Calculate the correlation matrix
        cor_matrix = df.corr()
        
        # Set the diagonal to NaN to avoid selecting the same column pair
        np.fill_diagonal(cor_matrix.values, np.nan)
        
        # Identify highly correlated pairs
        correlated_pairs = cor_matrix.stack().loc[lambda x: abs(x) >= cor_feature_selection_threshold]
        
        # Initialize a list to keep track of columns to drop
        columns_to_drop = set()

        # Iterate over the correlated pairs and mark one of the columns for removal
        for (col1, col2), cor_value in correlated_pairs.items():
            if col1 != 'swing_voter' and col2 != 'swing_voter':  # Don't drop swing_voter
                # Add the first column of the pair to the drop list
                columns_to_drop.add(col2)  # You can drop col1 instead if preferred

        # Drop the selected columns from the dataframe
        df = df.drop(columns=columns_to_drop)
    
    train_time_data, val_time_data, test_time_data = prepare_data.split_data(df)
    return train_time_data, val_time_data

    

def perturb_dataframe(df, perturb_frac=0.3, random_state=None):
    """
    Perturbs a DataFrame:
    - Numerical columns: Adds random noise between ±0.5 times the column's standard deviation to a fraction of rows.
    - Categorical columns: Randomly replaces a fraction of values with another value from the same column.
    - One-hot encoded columns (True/False): Randomly flips a False to True while ensuring only one True per row.
    
    Parameters:
        df (pd.DataFrame): The input DataFrame.
        perturb_frac (float): Fraction of rows to perturb for each column.
        random_state (int): Random seed for reproducibility.
    
    Returns:
        pd.DataFrame: A perturbed version of the DataFrame.
    """
    np.random.seed(random_state)
    df_perturbed = df.copy()

    # Perturb numerical columns
    for col in df.select_dtypes(include=['number']).columns:
        # Compute column standard deviation and maximum noise
        std_dev = df[col].std()
        max_noise = 0.5 * std_dev
        
        # Select a subset of rows to perturb
        perturb_indices = df.sample(frac=perturb_frac, random_state=random_state).index
        
        # Generate random noise between -max_noise and +max_noise
        noise = np.random.uniform(-max_noise, max_noise, size=len(perturb_indices))
        
        # Apply the noise to the selected rows
        df_perturbed.loc[perturb_indices, col] += noise

    # Perturb categorical columns
    for col in df.select_dtypes(include=['object', 'category']).columns:
        # Select a subset of rows to perturb
        perturb_indices = df.sample(frac=perturb_frac, random_state=random_state).index
        
        # Get unique values from the column (excluding NaN)
        unique_values = df[col].dropna().unique()
        
        # Generate random replacements from the unique values
        replacements = np.random.choice(unique_values, size=len(perturb_indices))
        
        # Replace the selected rows with the random values
        df_perturbed.loc[perturb_indices, col] = replacements
    
    # Perturb one-hot encoded columns (True/False)
    for col in df.select_dtypes(include=['bool']).columns:  # Check for boolean columns
        # Select a subset of rows to perturb
        perturb_indices = df.sample(frac=perturb_frac, random_state=random_state).index
        
        # Randomly flip a False to True, ensuring only one True per row for one-hot columns
        df_perturbed.loc[perturb_indices, col] = ~df_perturbed.loc[perturb_indices, col]  # Flips True to False and vice versa
    
    return df_perturbed
