import pandas as pd

def preprocess_car_data(df):
    """
    Cleans the dataframe: handles string formatting, drops columns, 
    encodes classes, and normalizes values.
    """
    # Drop timestamp as it's not used for training
    df.drop(['TIMESTAMP'], axis=1, inplace=True)
    
    # Rename for consistency
    df.rename(columns={'GEOPHONE-Z': 'Value'}, inplace=True)
    
    # Convert string values (decimal comma to dot) and cast to float
    df['Value'] = df['Value'].str.replace(',', '.').astype('float32')
    
    # Map class labels to binary integers
    df["Class"] = df["Class"].replace({"noise": 0, "car": 1})
    
    # Normalize 'Value' to the range [-1, 1]
    min_val = df['Value'].min()
    max_val = df['Value'].max()
    df['NORMALIZED'] = ((df['Value'] - min_val) / (max_val - min_val)) * 2 - 1
    
    # Drop original 'Value' column, keep normalized version
    df.drop('Value', axis=1, inplace=True)
    
    return df