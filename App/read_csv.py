# Modulo de python para leer archivos csv
import csv # modulo propio de python para manejar archivos CSV


def read_csv(path):
  
  with open(path, 'r') as csvfile: # nos ayuda abrir el archivo en modo lectura y lo cierra al mismo tiempo despues de utilizarlo
    reader = csv.reader(csvfile, delimiter=',') # guardamos los datos de ese archivo con el delimitador ,
    header = next(reader) # obtenermos el encabezado para usarlo e el diccionario
    data = []
    for row in reader: # Iteramos fila por fila en lo que hay en ese archivo 
      iterable = zip(header, row) # Lo convierte en listas de tuplas
      country_dict = {key: value for key, value in iterable} # Lo volvemos en un diccionario con los datos con los datos pasados por el iterable
      data.append(country_dict) # Lo añadimos a una lista para que quede un una lista de diccionarios
    return data  




if __name__ == '__main__':
  data = read_csv('data.csv')
  print(data[0])

























'''
no es por nada pero hay un método que ya resuelve lo de pasar los datos a diccionarios:


fileCSV = csv.DictReader(file,delimiter=',')
'''