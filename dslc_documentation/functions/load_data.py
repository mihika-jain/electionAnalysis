
import pandas as pd
import numpy as np

def load_data(path, dictionary):
    # Load the data into a pandas dataframe
    df = pd.read_csv(path)  # Modify this if your data is in a different format (e.g., .xlsx, .json, etc.)

    # List to store the new column names
    new_columns = []

    # Loop through the dictionary and rename columns accordingly
    for var, info in dictionary.items():
        # Check if the "V###" column exists in the dataframe
        if var in df.columns:
            # Add the corresponding renamed column to the list
            new_columns.append((var, info['column']))

    # Rename columns based on the dictionary
    df = df.rename(columns=dict(new_columns))

    # Extract the columns that are in the dictionary
    selected_columns = [info['column'] for info in dictionary.values()]
    df_selected = df[selected_columns]

    return df_selected
