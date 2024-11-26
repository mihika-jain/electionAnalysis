import pandas as pd
import numpy as np

def perturb_dataframe(df, perturb_frac=0.3, random_state=None):
    """
    Perturbs a DataFrame:
    - Numerical columns: Adds random noise between ±0.5 times the column's standard deviation to a fraction of rows.
    - Categorical columns: Randomly replaces a fraction of values with another value from the same column.
    
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

    return df_perturbed
