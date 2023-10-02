import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import csv

def busquedas():
  pytrends = TrendReq(hl='es')

  ## querys a analizar
  querys = ['Massa', 'Milei', 'Bullrich', 'Bregman', 'Schiaretti']

  ## cargamos parametros
  pytrends.build_payload(querys, cat=0, timeframe='now 1-H', geo='AR')

  ##ejecutamos
  df = pytrends.interest_over_time()

  df_local = pytrends.interest_by_region(resolution='COUNTRY').reset_index()
  df_filter = df_local[(df_local['Massa'] != 0) | (df_local['Milei'] != 0) | (df_local['Bullrich'] != 0) | (df_local['Bregman'] != 0) | (df_local['Schiaretti'] != 0)]

  fig, ax = plt.subplots(figsize= (40,10))

  ax.bar(df_filter['geoName'], df_filter['Massa'], color='blue')
  ax.bar(df_filter['geoName'], df_filter['Milei'], color='purple')
  ax.bar(df_filter['geoName'], df_filter['Bullrich'], color='yellow')
  ax.bar(df_filter['geoName'], df_filter['Bregman'], color='red')
  ax.bar(df_filter['geoName'], df_filter['Schiaretti'], color='green')
  plt.xticks(rotation=90)
  ##plt.show()
  
  df = pd.DataFrame(df_filter)
  df.to_csv("datos_google_trends.csv", index=False)

busquedas()