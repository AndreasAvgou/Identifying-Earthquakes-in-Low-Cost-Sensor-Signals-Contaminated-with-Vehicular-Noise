from obspy import read

def load_and_filter_stream(file_path, channel="HHZ"):
    """
    Loads an mseed file and returns the stream filtered by the specified channel.
    """
    try:
        st = read(file_path)
        filtered_st = st.select(channel=channel)
        return filtered_st
    except Exception as e:
        print(f"Error loading file {file_path}: {e}")
        return None