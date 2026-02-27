import tensorflow as tf

def load_saved_models(quake_model_path, car_model_path):
    """
    Loads both the Earthquake and Car detection models.
    """
    try:
        quake_model = tf.keras.models.load_model(quake_model_path)
        car_model = tf.keras.models.load_model(car_model_path)
        print("Models loaded successfully.")
        return quake_model, car_model
    except Exception as e:
        print(f"Error loading models: {e}")
        return None, None