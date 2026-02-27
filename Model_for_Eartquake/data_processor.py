import pandas as pd
import glob

def load_and_normalize_data(csv_path):
    """
    Reads all CSV files from a path, normalizes the 'Value' column to [-1, 1],
    and returns a concatenated DataFrame.
    """
    all_files = glob.glob(csv_path + "/*.csv")
    data_list = []

    for filename in all_files:
        df = pd.read_csv(filename, header=0)
        min_val = df[' Value'].min()
        max_val = df[' Value'].max()

        # Normalization formula: ((x - min) / (max - min)) * 2 - 1
        df['NORMALIZED'] = ((df[' Value'] - min_val) / (max_val - min_val)) * 2 - 1
        data_list.append(df)

    combined_df = pd.concat(data_list, ignore_index=True)
    
    # Drop unnecessary columns and rename label for consistency
    combined_df.drop(['Timestamp', ' Value'], axis=1, inplace=True)
    combined_df.rename(columns={' label': 'Class'}, inplace=True)
    
    return combined_df