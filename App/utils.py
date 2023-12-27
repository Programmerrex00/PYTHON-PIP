# Con esta funcion obtenemos el valor de la poblacion dependiendo al valor que tenga esa llave del diccionario
def get_population(country_dict):
  # Con estas lineas de codigo obtenemos los vamos de las poblaciones de esos años
  population_dict = {
      '2022': int(country_dict['2022 Population']),
      '2020': int(country_dict['2020 Population']),
      '2015': int(country_dict['2015 Population']),
      '2010': int(country_dict['2010 Population']),
      '2000': int(country_dict['2000 Population']),
      '1990': int(country_dict['1990 Population']),
      '1980': int(country_dict['1980 Population']),
      '1970': int(country_dict['1970 Population'])
  }
  # Guardamos las llaves y los valores en unas variables
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values


# Funcionn para obtener los datos del pais a buscar mediante el country y retornamos la lista de diccionarios
def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country,data))
  return result
