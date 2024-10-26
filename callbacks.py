import dash
from dash.dependencies import Input, Output
import pandas as pd
from dash import dcc
from data_generation import (
    generate_data_point,
    detect_anomalies,
    data_stream,
    timestamps,
    anomalies,
    anomaly_values,
    current_algo
)

# Initialize a flag for the algorithm change notification
algo_change_notified = False

def update_graph(app):
    """
    Update the graph and manage algorithm change notifications.

    This function sets up the callback for updating the live graph with real-time data.
    It also handles changes in the selected anomaly detection algorithm and displays
    notifications accordingly.
    """
    @app.callback(
        [Output('live-graph', 'figure'),
         Output('algo-notification', 'children'),
         Output('algo-description', 'children')],
        [Input('graph-update', 'n_intervals'), Input("algo-selector", "value")]
    )
    def update_graph(n, selected_algo):
        global current_algo, algo_change_notified

        try:
            # Check if the selected algorithm has changed
            if current_algo != selected_algo:
                current_algo = selected_algo
                data_stream.clear()
                timestamps.clear()
                anomalies.clear()
                anomaly_values.clear()
                algo_message = f"Algorithm changed to: {selected_algo}. Resetting view..."
                algo_change_notified = True  # Set the notification flag
            else:
                algo_message = ""

            # Generate new data point
            new_time, new_value = generate_data_point()
            data_stream.append(new_value)
            timestamps.append(new_time)

            # Detect anomalies
            anomaly_flags = detect_anomalies(current_algo, list(data_stream))

            # Clear previous anomalies
            anomalies.clear()
            anomaly_values.clear()
            for i, flag in enumerate(anomaly_flags):
                if flag == 1:
                    anomalies.append(timestamps[i])
                    anomaly_values.append(data_stream[i])
                else:
                    anomalies.append(None)
                    anomaly_values.append(None)

            # Determine x-axis range
            window_size = 50
            if len(timestamps) >= window_size:
                x_range = [timestamps[-window_size], timestamps[-1]]
            elif timestamps:
                x_range = [timestamps[0], timestamps[-1]]
            else:
                x_range = [0, 1]

            # Create traces for the graph
            trace1 = {
                'x': list(timestamps),
                'y': list(data_stream),
                'mode': 'lines+markers',
                'name': 'Data Stream'
            }
            trace2 = {
                'x': [timestamps[i] for i in range(len(anomalies)) if anomalies[i] is not None],
                'y': [data_stream[i] for i in range(len(anomaly_values)) if anomaly_values[i] is not None],
                'mode': 'markers+text',
                'name': 'Anomaly',
                'marker': {'color': 'red', 'size': 10},
                'text': [f"Value: {anomaly_values[i]:.2f}" for i in range(len(anomaly_values)) if anomaly_values[i] is not None],
                'textposition': "top center"
            }

            # Create the layout for the graph
            layout = {
                'title': "Real-Time Data Stream with Persistent Anomaly Detection",
                'xaxis': {'title': "Time", 'range': x_range},
                'yaxis': {'title': "Value"},
                'showlegend': True
            }

            # If an algorithm change notification is needed, display the message
            if algo_change_notified:
                algo_change_notified = False  # Reset the flag after notifying
                return {"data": [trace1, trace2], "layout": layout}, algo_message, "Description based on selected algorithm"
            else:
                return {"data": [trace1, trace2], "layout": layout}, "", "Description based on selected algorithm"  # No message on subsequent updates

        except Exception as e:
            # Handle unexpected errors gracefully
            return {}, f"Error: {str(e)}", ""

def download_report(app):
    """
    Download the report of detected anomalies.

    This function sets up the callback for downloading the detected anomalies
    as a CSV file.
    """
    @app.callback(
        Output('download-anomalies', 'data'),
        [Input('download-button', 'n_clicks')]
    )
    def download_report(n_clicks):
        if n_clicks > 0:
            try:
                anomaly_df = pd.DataFrame({
                    'Timestamp': [timestamps[i] for i in range(len(anomalies)) if anomalies[i] is not None],
                    'Anomaly Value': [anomaly_values[i] for i in range(len(anomaly_values)) if anomaly_values[i] is not None]
                })
                return dcc.send_data_frame(anomaly_df.to_csv, "detected_anomalies.csv")
            except Exception as e:
                # Handle download errors
                return dash.no_update
        return dash.no_update
