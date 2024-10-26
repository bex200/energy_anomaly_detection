# data_stream.py

import numpy as np
import pandas as pd

class DataStream:
    def __init__(self):
        self.data_stream = []
        self.timestamps = []
        self.current_time = pd.Timestamp.now()

    def generate_data_point(self):
        # Generate a new data point (for example, random)
        new_value = np.random.randn()  # Generate a random value
        self.current_time += pd.Timedelta(minutes=30)  # Increment time by 30 minutes
        self.data_stream.append(new_value)
        self.timestamps.append(self.current_time)
        return self.current_time, new_value

    def get_data(self):
        return self.data_stream, self.timestamps
