# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)

df = pd.read_csv("test_df.csv")

fig = px.choropleth(df.query("Year == 2020"), locations=df.query("Year == 2020")["Code"], hover_data=["Oil Production - TWh"], color="Oil Production - TWh")

app.layout = html.Div(children=[
    html.H1(children='Etisaal Intelligence Dashboard'),

    html.Div(children='''
        Renewable Energy ROI.
    '''),

    html.Div([
        dcc.Dropdown(list(df["Year"].unique()), '2020', id='year_dropdown'),
        dcc.Dropdown(list(df.columns), 'Oil Production - TWh', id='metric_dropdown'),
        dcc.Graph(style={'width': '200vh', 'height': '150vh'}, id='map_figure')])
])

@app.callback(
    Output('map_figure', 'figure'),
    Input('year_dropdown', 'value'),
    Input('metric_dropdown', 'value')
)
def update_output(year, metric):
    df_filtered = df.query(f"Year == {year}")
    fig = px.choropleth(df_filtered, locations=df_filtered["Code"], hover_data=["Oil Production - TWh"], color=metric)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
