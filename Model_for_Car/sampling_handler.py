from collections import Counter
from imblearn.under_sampling import NearMiss

def apply_undersampling(X, y):
    """
    Balances the dataset using NearMiss version 1.
    """
    print(f"Distribution before sampling: {Counter(y)}")
    
    # Define the undersampling method
    undersample = NearMiss(version=1, n_neighbors=3)
    
    # Execute resampling
    X_resampled, y_resampled = undersample.fit_resample(X, y)
    
    print(f"Distribution after sampling: {Counter(y_resampled)}")
    
    return X_resampled, y_resampled