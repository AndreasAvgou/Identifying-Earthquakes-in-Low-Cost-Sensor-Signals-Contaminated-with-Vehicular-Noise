import tensorflow as tf
from tensorflow.keras import layers, models
import sklearn.metrics as metrics

def build_lstm_model(input_shape):
    """
    Constructs the LSTM neural network architecture.
    """
    model = models.Sequential(name='model_quake')
    model.add(layers.LSTM(64, input_shape=(input_shape, 1), return_sequences=True))
    model.add(layers.Flatten())
    model.add(layers.Dense(32, activation='relu'))
    model.add(layers.Dense(16, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))
    
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
        loss=tf.keras.losses.BinaryCrossentropy(),
        metrics=['accuracy']
    )
    return model

def evaluate_model(model, X_test, y_test):
    """
    Calculates and prints Precision, Recall, F1, and AUC scores.
    """
    y_pred = model.predict(X_test)
    y_pred_binary = (y_pred > 0.5).astype(int)

    precision = metrics.precision_score(y_test, y_pred_binary, zero_division=0)
    recall = metrics.recall_score(y_test, y_pred_binary)
    f1 = metrics.f1_score(y_test, y_pred_binary)
    auc = metrics.roc_auc_score(y_test, y_pred)

    print(f"Precision: {precision:.4f}")
    print(f"Recall: {recall:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print(f"AUC Score: {auc:.4f}")