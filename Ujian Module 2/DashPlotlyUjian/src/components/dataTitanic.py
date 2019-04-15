import pandas as pd
import requests
from sqlalchemy import create_engine
engine = create_engine("mysql+mysqlconnector://root:673nPeW@@localhost/titanic?host=localhost?port=3306")
conn = engine.connect()
# dfTitanic = pd.DataFrame(res.json(), columns=res.json()[0].keys())
# dfTitanicTable = pd.DataFrame(res.json(), columns=res.json()[0].keys())

results = conn.execute("{}".format('select * from titanic')).fetchall()
dfTitanic = pd.DataFrame(results, columns=results[0].keys())
dfTitanicTable = pd.DataFrame(results, columns=results[0].keys())

# def displayDf(query, index='id'):
#     results = conn.execute("{}".format(query)).fetchall()
#     disp = pd.DataFrame(results, columns=results[0].keys())
#     # disp = disp.set_index('{}'.format(index))
#     return disp