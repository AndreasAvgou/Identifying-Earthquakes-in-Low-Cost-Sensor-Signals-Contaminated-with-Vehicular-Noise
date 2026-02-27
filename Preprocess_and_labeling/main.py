import os
from data_loader import load_and_filter_stream
from trigger_handler import detect_event_boundaries
from data_exporter import export_event_to_csv

def main():
    # Set your directory path and threshold here
    mseed_dir = "path/to/your/mseed/files" 
    threshold = 5.0

    if not os.path.exists(mseed_dir):
        print(f"Directory not found: {mseed_dir}")
        return

    # Iterate through all mseed files in the directory
    for filename in os.listdir(mseed_dir):
        if filename.endswith(".mseed"):
            file_path = os.path.join(mseed_dir, filename)
            st = load_and_filter_stream(file_path)
            
            if st:
                for i, trace in enumerate(st):
                    onset, offset, z_vals = detect_event_boundaries(trace, threshold)
                    
                    if onset is not None:
                        # Construct output filename based on original file and event index
                        csv_name = f"{os.path.splitext(filename)[0]}_event{i}.csv"
                        export_event_to_csv(trace, onset, offset, csv_name)
                    else:
                        print(f"No triggers found in {filename} (Trace {i})")

if __name__ == "__main__":
    main()