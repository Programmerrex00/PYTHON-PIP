# una forma de resorve el problema:
'''
import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        total = 0
        for row in reader:
            data_dict = dict(enumerate(row))
            total += sum(int(value) if value.isdigit() else 0 for value in data_dict.values())
    return total

value = read_csv('dat.csv')
print(value)
'''


# Otra forma de hacerlos con la funcion lambda
import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        total = 0
        for row in reader:
            iterable = row  # No necesitas convertir a lista y luego a tupla, usa directamente la fila, lo da en una list
            total += sum(map(lambda x: int(x) if x.isdigit() else 0, iterable))
    return total

value = read_csv('dat.csv')
print(value)


