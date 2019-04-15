import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from src.components.dataTitanic import dfTitanic, dfTitanicTable

# def generate_table(dataframe, max_row=10):
#     return html.Table(
#         #Header
#         [html.Tr([html.Th(col) for col in dataframe.columns])] +
#         #Body
#         [html.Tr(
#             [html.Td(
#                 str(dataframe.iloc[i][col])) for col in dataframe.columns
#                 ]) for i in range(min(len(dataframe), int(max_row)))]
#     )

def generate_table(dataframe, pagesize=10):
    return dt.DataTable(
        id='table-multicol-sorting',
        columns=[
            {"name": i, "id": i} for i in dataframe.columns
        ],
        pagination_settings={
            'current_page': 0,
            'page_size': pagesize
        },
        style_table={'overflowX': 'scroll'},
        pagination_mode='be',
        sorting='be',
        sorting_type='multi',
        sorting_settings=[]
    )

def renderIsiTab1():
    return [
            html.Div([
                html.Div([
                    html.P('Survived : '),
                    dcc.Dropdown(
                        id='survivedSearch',
                        options=[i for i in [{ 'label': 'All', 'value': 'All' },
                                            { 'label': 'Not-Survived', 'value': 0 },
                                            { 'label': 'Survived', 'value': 1 }]],
                        value='All'
                    )
                ], className='col-4')
            ], className='row'),html.Br(),
            html.Div([
                html.Div([
                    html.P('Age : '),
                    dcc.RangeSlider(
                        marks={i: str(i) for i in range(dfTitanic['age'].min(), dfTitanic['age'].max()+1, 5)},
                        min=dfTitanic['age'].min(),
                        max=dfTitanic['age'].max(),
                        value=[dfTitanic['age'].min(),dfTitanic['age'].max()],
                        className='rangeslider',
                        id='totalSearch'
                    ),
                ], className='col-10'),
                    html.Div([
                        html.Br(),
                        html.Button('Search', id='buttonsearch', style=dict(width='100%'))
                    ], className='col-2'),
            ], className = 'row'),html.Br(),html.Br(),
            html.Div([
                html.P('Max Row : '),
                dcc.Input(id='rowMax', value=10, type='number', max=len(dfTitanicTable))
            ], className='col-'),
            html.Center([
                html.H2('Data Titanic', className='title')      
            ]),
            html.Center(id='tableData', children=generate_table(dfTitanicTable))
        ]