import numpy as np
import random
from collections import deque

# Global variables
data_stream = deque(maxlen=200)
timestamps = deque(maxlen=200)
anomalies = deque(maxlen=200)
anomaly_values = deque(maxlen=200)
current_time = 0
current_algo = None

# Generate data with seasonality, concept drift, and noise
def generate_data_point():
    global current_time
    current_time += 1
    drift = current_time / 200
    seasonal = 10 * np.sin(current_time / 20)
    noise = random.normalvariate(0, 2)
    value = 20 + drift + seasonal + noise

    if random.random() < 0.02:  # Lower chance for anomalies (2%)
        value += random.choice([-20, 20])

    return current_time, value

# Improved anomaly detection placeholder
def detect_anomalies(selected_algo, data):
    if selected_algo == "IF":
        return [1 if abs(point - np.mean(data)) > 15 else 0 for point in data]
    elif selected_algo == "S-H-ESD":
        return [1 if abs(point - np.median(data)) > 18 else 0 for point in data]
    elif selected_algo == "GMM":
        return [1 if point > np.mean(data) + 12 or point < np.mean(data) - 12 else 0 for point in data]
    else:
        return [0] * len(data)
