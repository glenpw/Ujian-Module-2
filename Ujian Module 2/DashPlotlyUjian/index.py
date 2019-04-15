import os

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from src.components.dataTitanic import dfTitanic
from src.components.tab1.view import renderIsiTab1
from src.components.tab2.view import renderIsiTab2

from src.components.tab1.callbacks import callbacksortingtable, callbackfiltertable
from src.components.tab2.callbacks import callbackupdatecatgraph


app = dash.Dash(__name__)
server = app.server

app.title = 'Dashboard Titanic'

app.layout = html.Div([
    html.H1('Dashboard Titanic',style={'color': '#000080'}),
    html.H4('Created by Glen P. Wangsa'),
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='Data Titanic', value='tab-1', children=renderIsiTab1()),
        dcc.Tab(label='Categorical Plots', value='tab-2', children=renderIsiTab2())
    ],
    style={'fontFamily': 'Arial'},
    content_style={
        'fontFamily' : 'system-ui',
        'borderBottom' : '1px solid #d6d6d6',
        'borderLeft' : '1px solid #d6d6d6',
        'borderRight' : '1px solid #d6d6d6',
        'padding' : '50px'
    })],
    style={
        'maxWidth' : '1200px',
        'margin' : '0 auto'
    }
)

# ______________CALLBACK TABLE________________
@app.callback(
    Output('table-multicol-sorting', "data"),
    [Input('table-multicol-sorting', "pagination_settings"),
     Input('table-multicol-sorting', "sorting_settings")])
def update_sort_paging_table(pagination_settings, sorting_settings):
    return callbacksortingtable(pagination_settings, sorting_settings)

@app.callback(
    Output(component_id='tableData', component_property='children'),
    [Input(component_id='buttonsearch', component_property='n_clicks'),
    Input(component_id='rowMax', component_property='value')],
    [
    State(component_id='survivedSearch', component_property='value'),
    State(component_id='totalSearch', component_property='value')]
)
def update_table(n_clicks,maxrows,survive,age):
    return callbackfiltertable(n_clicks,maxrows,survive,age)

# ________________CALLBACK PLOT________________
@app.callback(
    Output(component_id='categoryGraph', component_property='figure'),
    [
        Input(component_id='jenisplotcategory', component_property='value'),
        Input(component_id='xplotcategory', component_property='value'),
        Input(component_id='yplotcategory', component_property='value'),
        Input(component_id='statsplotcategory', component_property='value')
    ]
)
def update_category_graph(jenisPlot,xPlot,yPlot,stats):
    return callbackupdatecatgraph(jenisPlot,xPlot,yPlot,stats)

# __________CALLBACK DISABLE STATS_____________
@app.callback(
    Output(component_id='statsplotcategory', component_property='disabled'),
    [Input(component_id='jenisplotcategory', component_property='value')]
)
def update_disable_stats(jenisPlot):
    if (jenisPlot == 'Bar'):
        return False
    return True


if __name__ == '__main__':
    app.run_server(debug=True)  



