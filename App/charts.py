# Vamos a graficar
import matplotlib.pyplot as plt

# Grafica de barras
def generate_bar_chart(name, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{name}.png') # Lo guardara en un archivo, la imagen que genera
  plt.close()

# Grafica tipo torta
def generate_pie_chart(labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  plt.savefig('pie.png') # Lo guardara en un archivo, la imagen que genera
  plt.close()

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [10, 40, 800]
  #generate_bar_chart(labels, values)  
  generate_pie_chart(labels, values)