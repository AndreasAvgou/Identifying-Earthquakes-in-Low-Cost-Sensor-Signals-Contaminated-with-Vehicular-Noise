from sklearn.model_selection import train_test_split
from data_processor import load_and_normalize_data
from sampler_utils import balance_classes
from earthquake_model import build_lstm_model, evaluate_model

def main():
    # 1. Load and Preprocess
    csv_path = 'path/to/your/csv/files' # Update with your path
    df = load_and_normalize_data(csv_path)
    
    # 2. Balance Dataset
    X_res, y_res = balance_classes(df)
    
    # 3. Split Data
    X_train, X_test, y_train, y_test = train_test_split(
        X_res, y_res, test_size=0.2, random_state=42
    )
    
    # 4. Build and Train Model
    # Input shape is (features, 1) for LSTM
    model = build_lstm_model(X_train.shape[1])
    
    print("Starting model training...")
    history = model.fit(
        X_train, y_train, 
        batch_size=64, 
        epochs=12, 
        verbose=1
    )
    
    # 5. Evaluate
    print("\nModel Evaluation Results:")
    evaluate_model(model, X_test, y_test)

if __name__ == "__main__":
    main()