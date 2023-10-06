import json
import csv
import requests

# Descarga los datos JSON de la IMF
url_periods = 'https://www.imf.org/external/datamapper/api/v1/PCPIPCH?periods=2023'
url_countries = 'https://www.imf.org/external/datamapper/api/v1/countries'

response_periods = requests.get(url_periods)
response_countries = requests.get(url_countries)

data_periods = json.loads(response_periods.text)
data_countries = json.loads(response_countries.text)

# Extrae los datos requeridos de inflación
values = data_periods['values']['PCPIPCH']
csvData = [[key, values[key]['2023']] for key in values.keys()]

# Extrae los datos de países y crea un diccionario
country_data_dict = data_countries['countries']

# Combina los datos de inflación con los nombres de los países
for row in csvData:
    country_code = row[0]
    country_name = country_data_dict.get(country_code, {}).get('label', '')
    row.insert(0, f'"{country_name}"')

# Convierte los datos a formato CSV
csv = '\n'.join([','.join(map(str, row)) for row in csvData])

# Agrega encabezados
csv_with_headers = "country,code,inflation_rate\n" + csv

# Escribe los datos CSV en un archivo
with open('./data/inflation.csv', 'w', newline='') as csv_file:
    csv_file.write(csv_with_headers)

print('CSV file generated successfully.')