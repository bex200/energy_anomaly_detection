# anomaly_detection.py

import numpy as np

def detect_anomalies(selected_algo, data):
    # Simulate different anomaly detection logics per algorithm
    if selected_algo == "IF":
        return [1 if abs(point - np.mean(data)) > 15 else 0 for point in data]
    elif selected_algo == "S-H-ESD":
        return [1 if abs(point - np.median(data)) > 18 else 0 for point in data]
    elif selected_algo == "GMM":
        return [1 if point > np.mean(data) + 12 or point < np.mean(data) - 12 else 0 for point in data]
    else:
        return [0] * len(data)
