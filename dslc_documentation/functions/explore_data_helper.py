import pandas as pd
import numpy as np
import importlib
import sys
import os

def perturb_dataframe_assumptions(path, drop_columns, n_neighborhoods, transform_data, cor_feature_selection_threshold, convert_categorical, year_threshold):
    
    # Add the directory containing the file to the Python path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(path), 'functions')))
    # Import the function
    from functions import load_data
    from functions import prepare_data
    from functions import  load_dictionaries_time_series
    # Reload the module to reflect any updates
    importlib.reload(load_data)
    importlib.reload(prepare_data)
    importlib.reload(load_dictionaries_time_series)
    
    dictionary = load_dictionaries_time_series.dict_time_series()
    column_labels = load_dictionaries_time_series.column_labels_time()
    
    df = load_data.load_data(path, dictionary)
    df = prepare_data.clean_columns(df, dictionary)
    
    year_column = dictionary["VCF0004"]["column"]
    cutoff_year = year_threshold
    df = prepare_data.drop_rows_before_year(df, year_column, cutoff_year)
    
    df = prepare_data.knn_impute(df, dictionary, column_labels, n_neighborhoods)
    df = prepard_data.add_swing_voter_column_timeSeries(df, column_labels_time)
    
    df = df.drop(columns = drop_columns)
    dict_time_series = prepare_data.remove_keys_from_dict(dictionary, drop_columns)
    
    
    if convert_categorical == 'dummy':
        df = prepare_data.one_hot_cat_cols(df, dictionary, column_labels)
    
    if transform_data =="standard":
        from sklearn.preprocessing import StandardScaler

        # Standardizing the data before PCA
        scaler = StandardScaler()
        df = scaler.fit_transform(df)
        
    elif transform_data =="minMax":
        from sklearn.preprocessing import MinMaxScaler

        # Standardizing the data before PCA
        scaler = MinMaxScaler()
        df = scaler.fit_transform(df)
    
    #----------------------- Correlation feature selection ---------------------#
    # select only features that are at least 0.5 correlated with response
    if (cor_feature_selection_threshold != None):
        # compute pairwise correlations
        cor_swing = df.corr().drop(index=["swing_voter"])
        # extract sale price correlations
        cor_swing = cor_saleprice["swing_voter"]

        # identify variables whose corr with sale price is above the threshold
        high_cor_vars = cor_saleprice[(np.abs(cor_swing) >= cor_feature_selection_threshold)].index
        high_cor_vars = list(high_cor_vars)
        high_cor_vars.extend(["swing_voter"])
        # filter to just the highly correlated vars
        df = df[high_cor_vars]
        
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
