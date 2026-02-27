import numpy as np
from obspy.signal.trigger import z_detect, plot_trigger

def detect_event_boundaries(trace, threshold=5.0):
    """
    Calculates Z-scores and identifies the start (onset) and end (offset) indices of an event.
    """
    df = trace.stats.sampling_rate
    # Calculate Z-score with a 0.5-second window
    z_scores = z_detect(trace.data, int(0.5 * df))
    
    # Find indices where Z-score exceeds the threshold
    trigger_indices = np.where(z_scores > threshold)[0]
    
    if len(trigger_indices) > 0:
        return trigger_indices[0], trigger_indices[-1], z_scores
    return None, None, z_scores

def visualize_trigger(trace, z_scores, threshold=5.0):
    """
    Plots the seismic trace alongside the trigger function.
    """
    plot_trigger(trace, z_scores, threshold, 0.5)