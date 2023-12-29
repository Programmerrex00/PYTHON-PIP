# Importamos modulos donde encontramos diferentes funciones 
import utils # Modulo para obtener la poblacion y los datos de ese pais
import read_csv # Modulo para obtener la lista de diccionarios con todos los paises
import charts # Modulo para generar el diagrama de barras 

import pandas as pd # Vamos a usar pandas para leer los archivos mas rapido 


def run():

  # Forma de filtrar datos de la manera manual ahora con PANDAS lo haremos mas optimo
  '''
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  '''



  # Usando pandas
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == 'South America'] # Optimizamos la busqueda de paises que sean de sur america

  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)
  # Usando pandas

  


  data = read_csv.read_csv('data.csv') # En esta linea de codigo traemos a la funcio read_csv y le pasamos como parametro la ruta donde nuestro archio data.csv
  text = input('Ingrese el nombre de un Pais para ver su Poblacion: ')
  result = utils.population_by_country(data, text) # Con esta linea llamamos a la funcion population_by_country y le pasamos como parametro los datos obtenidos en la linea 8 y le pasamos el pais a buscar

  if len(result) > 0: # se ejecuta si la longitud es mayor a 0
    country = result[0] # Le colocamos 0 ya que solo es un diccionario el que vamos a obtener
    labels, values = utils.get_population(country) # Dependiend al pais que le pasemos como parametro extrae la cantidad de poblacion de cada año
    charts.generate_bar_chart(text ,labels, values) # Linea para generar la grafica acorde a los values y los labels
    # charts.generate_pie_chart(labels, values) # Linea para generar la grafica acorde a los values y los labels




# Ahora esto es para que haya dualidad osea si ejecuto el archivo main.py que se ejecute automaticamente todo lo que tiene, y tambien es para que cuando yo ejecute lo que tiene el archivo example.py pueda controlar lo que quiero llevar de main mas no se ejecute todo con importar todo lo que tiene main.py

if __name__ == '__main__':
  run()

