import os

def export_event_to_csv(trace, first_onset_index, last_off_index, output_filename):
    """
    Exports seismic data to a CSV file with 'quake' or 'noise' labels based on trigger indices.
    """
    starttime = trace.stats.starttime
    df = trace.stats.sampling_rate
    
    # Calculate precise time objects for labeling
    first_onset_time = starttime + first_onset_index / df
    last_off_time = starttime + last_off_index / df

    with open(output_filename, "w") as f:
        f.write("Timestamp, Value, label\n")
        for t, v in zip(trace.times(), trace.data):
            current_time = starttime + t
            timestamp = current_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            
            # Labeling logic: 'quake' if within detection boundaries, else 'noise'
            label = 'quake' if first_onset_time <= current_time <= last_off_time else 'noise'
            f.write(f"{timestamp}, {v}, {label}\n")
    
    print(f"Successfully created: {output_filename}")