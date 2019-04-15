import dash_core_components as dcc
import dash_html_components as html
from src.components.dataTitanic import dfTitanic

def renderIsiTab2():
    return [
            html.Div([
                # DROP DOWN JENIS PLOT
                html.Div([
                    html.P('Jenis : '),
                    dcc.Dropdown(
                        id='jenisplotcategory',
                        options=[{'label': i, 'value': i} for i in ['Bar','Box','Violin']],
                        value='Bar'
                    )
                ], className='col-3'),
                # DROP DOWN X
                html.Div([
                    html.P('X : '),
                    dcc.Dropdown(
                        id='xplotcategory',
                        options=[{'label': i, 'value': i} for i in ['sex','survived','embark_town','class','who','alone']],
                        value='sex'
                    )
                ], className='col-3'),
                # DROP DOWN Y
                html.Div([
                    html.P('Y : '),
                    dcc.Dropdown(
                        id='yplotcategory',
                        options=[{'label': i, 'value': i} for i in ['fare','age']],
                        value='fare'
                    )
                ], className='col-3'),
                # DROP DOWN LAST
                html.Div([
                    html.P('Stats : '),
                    dcc.Dropdown(
                        id='statsplotcategory',
                        options=[
                            i for i in [
                                {'label' : 'Mean', 'value' : 'mean'},
                                {'label' : 'Standard Deviation', 'value' : 'std'},
                                {'label' : 'Count', 'value' : 'count'},
                                {'label' : 'Min', 'value' : 'min'},
                                {'label' : 'Max', 'value' : 'max'},
                                {'label' : '25th Percentiles', 'value' : '25%'}, 
                                {'label' : 'Median', 'value' : '50%'},
                                {'label' : '75th Percentiles', 'value' : '75%'},
                            ]
                        ],
                        value='mean',
                        disabled = False
                    )
                ], className='col-3')
            ], className='row'),
            html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),html.Br(),
            dcc.Graph(
                id='categoryGraph'
            )
        ]