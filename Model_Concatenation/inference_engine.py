import numpy as np

def classify_event(quake_model, car_model, segment_data):
    """
    Runs the segment through both models and determines the final classification.
    """
    # Reshape data for LSTM input: (samples, features, 1)
    # Note: Models expect specific input lengths. Adjust padding/slicing as needed.
    input_data = segment_data.reshape(1, -1, 1)
    
    quake_pred = quake_model.predict(input_data, verbose=0)[0][0]
    car_pred = car_model.predict(input_data, verbose=0)[0][0]
    
    # Logic for final label
    if quake_pred > 0.5:
        return "Earthquake", quake_pred
    elif car_pred > 0.5:
        return "Car/Vehicle", car_pred
    else:
        return "Noise/Undefined", max(quake_pred, car_pred)