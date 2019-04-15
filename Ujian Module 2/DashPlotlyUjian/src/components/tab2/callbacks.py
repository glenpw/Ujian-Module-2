import plotly.graph_objs as go
from src.components.dataTitanic import dfTitanic

listGoFunc = {
    'Bar' : go.Bar,
    'Box' : go.Box,
    'Violin' : go.Violin
}

def generateValuePlot(x,y,stats = 'mean'):
    return {
        'x' : {
            'Bar' : dfTitanic[x].unique(),
            'Box' : dfTitanic[x],
            'Violin' : dfTitanic[x],
        },
        'y' : {
            'Bar' : dfTitanic.groupby(x)[y].describe()[stats],
            'Box' : dfTitanic[y],
            'Violin' : dfTitanic[y],
        }
    }

def callbackupdatecatgraph(jenisPlot,xPlot,yPlot,stats):
    return dict(
        layout= go.Layout(
            title = '{} Plot Titanic'.format(jenisPlot),
            xaxis = {'title' : xPlot},
            yaxis = dict(title=yPlot),
            boxmode = 'group',
            violinmode = 'group',
        ),
        data = [
            listGoFunc[jenisPlot](
                x= generateValuePlot(xPlot,yPlot)['x'][jenisPlot],
                y= generateValuePlot(xPlot,yPlot,stats)['y'][jenisPlot],
                name = 'Legendary',
                opacity= 0.6
            )
        ]
    )