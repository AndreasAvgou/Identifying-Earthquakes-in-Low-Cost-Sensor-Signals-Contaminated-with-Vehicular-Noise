from collections import Counter
from imblearn.under_sampling import NearMiss
from sklearn.preprocessing import LabelEncoder

def balance_classes(df):
    """
    Encodes labels and applies NearMiss undersampling to balance the dataset.
    """
    # Encode 'noise'/'quake' to 0/1
    le = LabelEncoder()
    df['Class'] = le.fit_transform(df['Class'])
    
    X = df.drop(['Class'], axis=1)
    y = df['Class']
    
    print(f"Original distribution: {Counter(y)}")
    
    # Apply NearMiss undersampling
    undersample = NearMiss(version=1, n_neighbors=3)
    X_resampled, y_resampled = undersample.fit_resample(X, y)
    
    print(f"Resampled distribution: {Counter(y_resampled)}")
    
    return X_resampled, y_resampled