import csv # Importa el módulo csv, que proporciona funcionalidades para leer y escribir archivos CSV (Comma-Separated Values).
import re # Modulo para trabajar con expresiones regulares
import matplotlib.pyplot as plt # Modulo para graficar






def read_country(path, country): # Toma como argumento la ruta y el nombre del pais
  with open(path, 'r') as file: # Abre el archivo en modo lectura
    csv_file = csv.reader(file, delimiter=',') # Delimitador del archivo con la coma
    header = next(csv_file) # Obtiene el encabezado del archivo y lo guarda en la variable header
    for row in csv_file: # Recorremos fila por fila
      if row[2] == country: # Si es pais es igual a country
        new_row = zip(header, row) # Unimos el encabezado y los datos del pais en una tupla
        new_dictionary = {key: value for key, value in new_row} # Crea un diccionario con los datos de las tuplas
  return header, new_dictionary # Retorna el encabezado y el diccionario








def dictionary_population(path, country): # Toma como argumento la ruta y el nombre del pais
  header, data = read_country(path, country) # Invocamos al metodo para obtener el encabezado y los datos del pais
  new_dictionary = {} # Creamos un diccionario vacio
  
  for i in range(len(header)): # Recorremos cada uno de los elementos que tiene el header
    matches = re.findall(r'\d{4,4}', header[i]) # Guardamos en matches listas con los años buscados en la expresion regular mediante el iterador i en la lista del header, buscando 4 dijitos que serian el año
    if matches != []: # Comprobamos que la lista sea diferente a vacio

      # Unimos el diccionario new_dictionary | con otro diccionario
      new_dictionary = new_dictionary | { matches[0]: int(value) for key, value in data.items() if matches[0] in key }

  
  return new_dictionary # Retornamos el diccionario con las llaves como los años y los valores como la cantidad de habitantes que tiene le pais







def generate_bar_chart(labels, values): 
  fig, ax = plt.subplots() # Crea una figura y el eje de x y y
  ax.bar(labels, values) # Crea un grafico de barras
  plt.show() # Muestra el grafico








if __name__ == '__main__':
  path = 'data.csv' # Ruta
  country = input('Escriba el nombre de un pais: ') # Obtenemos el nombre del pais
  country_dict = dictionary_population(path, country) # Invocamos al metodo dictionary_population
  generate_bar_chart(country_dict.keys(), country_dict.values()) # Invocamos al metodo generate_bar_chart que nos ayuda a graficar con los labels(keys) y los values(values)
