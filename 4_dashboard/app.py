# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

app = Dash(__name__)

key_columns = [
    'Annual CO2 emissions', 'Annual change in primary energy consumption (%)',
    'Per capita electricity (kWh)',
    'Fossil fuels per capita (kWh)', 'Fossil fuels (% equivalent primary energy)',
    'Renewables per capita (kWh - equivalent)', 'Renewables (% electricity)',
    'Solar Generation - TWh', 'prod of Electricity from solar (TWh)',
    'Land area (sq. km)', 'Population density (people per sq. km of land area)'
]

df = pd.read_csv("../data/silver_tables/yearly_values_per_entity.csv")
df_predicted = pd.read_csv("../data/forecasts_tables/all_entities_forecasts.csv")

df = df.loc[df['Entity_Category'] == 'Country']
df_predicted = df_predicted.loc[df_predicted['Entity_Category'] == 'Country']

df_predicted = df_predicted.merge(df[['Entity', 'Code']], how='left', on='Entity')
df_predicted = df_predicted.loc[df_predicted['Year'] == 2020]

def get_figure_2():
    y = 'Annual CO2 emissions_predicted_next_10_year_sum'
    
    div2 = html.Div([
        dcc.Dropdown(list(df_predicted.columns), y, id='metric_dropdown2'),
        dcc.Graph(
        style={'width': '200vh', 'height': '150vh'},
        figure = px.choropleth(df_predicted, locations=df_predicted["Code"], color=y)
        )
    ])
    return div2

# fig = px.choropleth(df.query("Year == 2020"), locations=df.query("Year == 2020")["Code"], hover_data=["Oil Production - TWh"], color="Oil Production - TWh")

app.layout = html.Div(children=[
    html.H1(children='Global Metric Dashboard'),

    html.Div([
        dcc.Dropdown(list(df["Year"].unique()), '2020', id='year_dropdown'),
        dcc.Dropdown(list(df.columns), 'Oil Production - TWh', id='metric_dropdown'),
        dcc.Graph(style={'width': '200vh', 'height': '150vh'}, id='map_figure')
        ]),
    
    html.H1(children='Forecasted Next 10 Years CO2 Emissions'),
    get_figure_2(),
])

@app.callback(
    Output('map_figure', 'figure'),
    Input('year_dropdown', 'value'),
    Input('metric_dropdown', 'value')
)
def update_output(year, metric):
    df_filtered = df.query(f"Year == {year}")
    fig = px.choropleth(df_filtered, locations=df_filtered["Code"], hover_data=key_columns, color=metric)
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
