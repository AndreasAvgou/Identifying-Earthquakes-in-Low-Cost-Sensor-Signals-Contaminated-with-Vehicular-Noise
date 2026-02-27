import os
from obspy import read
from model_loader import load_saved_models
from signal_segmenter import get_trigger_segments, extract_segment_data
from inference_engine import classify_event

def main():
    # 1. Setup paths
    QUAKE_MODEL_PATH = 'model_quake.h5'
    CAR_MODEL_PATH = 'model_car.h5'
    MSEED_FILE = 'path/to/your/test_data.mseed'
    
    # 2. Load Models
    m_quake, m_car = load_saved_models(QUAKE_MODEL_PATH, CAR_MODEL_PATH)
    if not m_quake or not m_car: return

    # 3. Read and Filter Seismic Data
    st = read(MSEED_FILE).select(channel="HHZ")
    
    for trace in st:
        print(f"\nProcessing Trace: {trace.id}")
        
        # 4. Detect Events
        segments, _ = get_trigger_segments(trace)
        
        for start, end in segments:
            # 5. Preprocess Segment
            segment_data = extract_segment_data(trace, start, end)
            
            # 6. Dual Inference
            # Ensure the segment_data matches the model's expected input shape
            # You might need to interpolate or pad the data here
            label, confidence = classify_event(m_quake, m_car, segment_data)
            
            print(f"-> Detected Event: {label} (Confidence: {confidence:.2f})")
            print(f"   Time: {trace.stats.starttime + (start/trace.stats.sampling_rate)}")

if __name__ == "__main__":
    main()