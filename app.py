import dash
from layout import create_layout
from callbacks import update_graph, download_report

# Initialize Dash App
app = dash.Dash(__name__)
app.layout = create_layout()

# Register callbacks
update_graph(app)
download_report(app)

if __name__ == '__main__':
    app.run_server(debug=True)
