import csv
import re
import matplotlib.pyplot as plt


def dictionary_World_Population_Percentage_and_Country(path):
  with open(path, 'r') as file:
    csv_file = csv.reader(file, delimiter=',')
    header = next(csv_file)  # Obtengo el encabezado para obtener los indices
    country_index = header.index('Country/Territory')  # Busca el indice del pais
    percentage_index = header.index('World Population Percentage')  # Busca el indice del porcentaje del pais
    country_america = header.index('Continent')
    result = list(filter(lambda item: item[country_america] == 'South America',csv_file))
    resultt = dict(map(lambda item: (item[country_index], item[percentage_index]),result))
    return resultt


def generate_pie_chart(labels, values): 
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  plt.savefig('pie.png') # Lo guardara en un archivo, la imagen que genera
  plt.close()


if __name__ == '__main__':
  path = 'data.csv'  # Ruta
  country_dict = dictionary_World_Population_Percentage_and_Country(path)
  generate_pie_chart(country_dict.keys(), country_dict.values())
  #generate_bar_chart(dictionary_World_Population_Percentage_and_Country.keys(),
  #dictionary_World_Population_Percentage_and_Country.values())











'''
# Otra forma de hacerlo
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)





if __name__ == '__main__':
  run()

'''
