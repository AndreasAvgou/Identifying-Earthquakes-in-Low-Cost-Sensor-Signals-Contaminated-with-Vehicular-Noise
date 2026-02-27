import numpy as np
from obspy.signal.trigger import z_detect

def get_trigger_segments(trace, threshold=5.0):
    """
    Detects events using Z-score and returns the start and end indices
    for all triggered segments in the trace.
    """
    df = trace.stats.sampling_rate
    # Calculate Z-score with a 0.5s window
    z_scores = z_detect(trace.data, int(0.5 * df))
    
    # Find all indices where the threshold is exceeded
    trigger_indices = np.where(z_scores > threshold)[0]
    
    if len(trigger_indices) == 0:
        return [], z_scores

    # Group consecutive indices or identify distinct event boundaries
    # (Simplified: returning the full range between first and last trigger for the demonstration)
    return [(trigger_indices[0], trigger_indices[-1])], z_scores

def extract_segment_data(trace, start_idx, end_idx):
    """
    Extracts and normalizes a specific segment from the trace data.
    """
    segment = trace.data[start_idx:end_idx]
    
    # Min-Max Normalization to [-1, 1]
    min_val = np.min(segment)
    max_val = np.max(segment)
    if max_val - min_val == 0:
        return np.zeros_like(segment)
        
    normalized_segment = ((segment - min_val) / (max_val - min_val)) * 2 - 1
    return normalized_segment