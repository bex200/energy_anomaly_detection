from dash import dcc, html

def create_layout():
    return html.Div([
        html.H2("Real-Time Data Stream with Persistent Anomaly Detection"),
        dcc.Graph(id='live-graph', animate=True),
        html.Div(id="algo-notification", style={"color": "blue", "font-weight": "bold"}),
        dcc.Dropdown(
            id="algo-selector",
            options=[
                {"label": "Isolation Forest", "value": "IF"},
                {"label": "Seasonal Hybrid ESD", "value": "S-H-ESD"},
                {"label": "Gaussian Mixture Model", "value": "GMM"},
            ],
            value="IF",
            placeholder="Select Anomaly Detection Algorithm"
        ),
        html.Div(id='algo-description', style={'margin-top': '10px', 'font-style': 'italic'}),
        dcc.Interval(
            id='graph-update',
            interval=200,
            n_intervals=0
        ),
        html.Button("Download Report", id="download-button", n_clicks=0),
        dcc.Download(id="download-anomalies"),
        html.Div(id="download-notification", style={"margin-top": "10px"})
    ])
