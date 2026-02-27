from sklearn.model_selection import train_test_split
from db_loader import fetch_data_from_sql
from car_data_processor import preprocess_car_data
from sampling_handler import apply_undersampling
from car_model_manager import build_car_lstm, evaluate_car_model

def main():
    # Database credentials
    DB_CONFIG = {
        "server": "YOUR_SERVER",
        "database": "YOUR_DATABASE",
        "username": "YOUR_USERNAME",
        "password": "YOUR_PASSWORD"
    }

    # 1. Fetch Data
    raw_df = fetch_data_from_sql(**DB_CONFIG)
    if raw_df is None: return

    # 2. Preprocess
    clean_df = preprocess_car_data(raw_df)
    
    # 3. Split Features and Target
    X = clean_df.drop(['Class'], axis=1)
    y = clean_df['Class']

    # 4. Handle Imbalance
    X_balanced, y_balanced = apply_undersampling(X, y)

    # 5. Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X_balanced, y_balanced, test_size=0.2, random_state=42
    )

    # 6. Model Training
    model = build_car_lstm(X_train.shape[1])
    print("Starting training...")
    model.fit(X_train, y_train, batch_size=64, epochs=4)

    # 7. Evaluation
    print("\nFinal Model Evaluation:")
    evaluate_car_model(model, X_test, y_test)

if __name__ == "__main__":
    main()