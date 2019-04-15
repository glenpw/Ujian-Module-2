import requests
import pandas as pd

from src.components.tab1.view import generate_table
from src.components.dataTitanic import dfTitanicTable

def callbacksortingtable(pagination_settings, sorting_settings):
    # print(sorting_settings)
    if len(sorting_settings):
        dff = dfTitanicTable.sort_values(
            [col['column_id'] for col in sorting_settings],
            ascending=[
                col['direction'] == 'asc'
                for col in sorting_settings
            ],
            inplace=False
        )
    else:
        # No sort is applied
        dff = dfTitanicTable

    return dff.iloc[
        pagination_settings['current_page']*pagination_settings['page_size']:
        (pagination_settings['current_page'] + 1)*pagination_settings['page_size']
    ].to_dict('rows')

def callbackfiltertable(n_clicks,maxrows,survive,age):
    global dfTitanicTable
    dfFilter = dfTitanicTable[((dfTitanicTable['age'] >= age[0]) & (dfTitanicTable['age'] <= age[1]))]
    if(survive == 'All'):
        dfTitanicTable = dfFilter
    else:
        dfTitanicTable = dfFilter[dfFilter['survived'] == int(survive)]
    return generate_table(dfTitanicTable, pagesize=maxrows)