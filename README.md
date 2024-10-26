# Real-Time Anomaly Detection in Data Streams

## Overview

This project implements a real-time anomaly detection system using Python, Dash, and various machine learning algorithms. It simulates a data stream and detects anomalies, providing an interactive visualization to analyze the data effectively.

## Project Features

- Real-time data generation and visualization
- Support for multiple anomaly detection algorithms
- Dynamic updating of graphs with anomaly highlights
- Downloadable reports of detected anomalies
- Robust error handling and data validation

## Chosen Algorithms

### 1. **Isolation Forest**
The Isolation Forest algorithm isolates observations by randomly partitioning the data. Anomalies are defined as observations that require fewer splits to isolate, making this method effective for high-dimensional datasets. It is computationally efficient and suitable for real-time applications.

### 2. **Other Algorithms**
*You can add additional algorithms here as needed.*

## Project Structure

```
/cobbleston_test
│
├── app.py                # Main application file to run the Dash app
├── callbacks.py          # Contains callbacks for updating the graph and handling user interactions
├── data_generation.py     # Generates synthetic data and detects anomalies
├── layout.py              # For a proper layout styling
├── requirements.txt       # List of Python package dependencies
└── README.md              # Project documentation
```

## Setup Instructions

To set up the project locally, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone https://github.com/bex200/energy_anomaly_detection.git
   cd energy_anomaly_detection
   ```

2. **Create a Virtual Environment (Optional but Recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   Install the required libraries listed in the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   Launch the Dash app:
   ```bash
   python app.py
   ```
   The application will run on `http://127.0.0.1:8050/` by default.

## Usage

- Select an anomaly detection algorithm from the dropdown menu.
- The graph will update in real-time, highlighting detected anomalies.
- Click the "Download" button to save a report of detected anomalies as a CSV file.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please create a pull request or open an issue.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Dash](https://dash.plotly.com) - A productive Python framework for building web applications.
- [Pandas](https://pandas.pydata.org) - A fast, powerful, flexible, and easy-to-use open-source data analysis and manipulation tool.
