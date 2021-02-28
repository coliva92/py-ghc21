from argparse import ArgumentParser


# La version del paquete aqui presentado
VERSION = '0.0.00'




# Lee las rutas de los archivos de entrada y salida proveidos como argumentos 
# del programa por la interfaz de la linea de comandos.
# name (str):         el nombre del problema que el programa resuelve
# year (int|str):     el año de la competencia en la que se está participando
# return (str, str):  las rutas proveidas como argumentos del programa
def get_args(name, 
             year):
  desc = f"""Program for competing in Google Hash Code {year}, programmed 
         using py-ghc version {VERSION}. This year's problem is \'{name}\'"""
  parser = ArgumentParser(prog='ghc', description=desc)
  info = """Path for the text file containing the problem's input data"""
  parser.add_argument('input', help=info)
  info = """Path for the text file where the problem's output data will be 
         stored"""
  parser.add_argument('output', help=info)
  args = parser.parse_args()
  return args.input, args.output



# Permite leer los datos de un archivo de texto y cargarlos a un diccionario, 
# segun la estructura definida por data_desc. Para conocer el formato en 
# el que debe proporcionarse data_desc, se recomienda leer la documentación.
# filename (str):   ruta completa al archivo que sera leido
# data_desc (dict): diccionario que define como se organizaran los datos leidos  
#                   del archivo en el diccionario resultante
# return (dict):    un diccionario que contiene los datos leidos del archivo
def read_input_file(filename,
                    data_desc):
  input_data = {}
  file = open(filename, 'rt')
  for section in data_desc:
    item = row_count = None
    if 'row_count' not in section:
      input_data[section['name']] = {}
      item = input_data[section['name']]
      row_count = 1
    else:
      input_data[section['name']] = []
      item = {}
      keys = section['row_count'].split()
      row_count = input_data[keys[0]][keys[1]]
    for _ in range(row_count):
      values = next(file).split()
      for i in range(len(section['columns'])):
        col = section['columns'][i]
        if 'repeat' not in col:
          item[col['name']] = col['type'](values[i])
        elif col['repeat'] == '*':
          item[col['name']] = [ 
            col['type'](values[j]) for j in range(i, len(values)) ]
        else:
          item[col['name']] = [ 
            col['type'](values[j]) for j in range(i, i + item[col['repeat']]) ]
      if 'row_count' in section: 
        input_data[section['name']].append(item)
        item = {}
  file.close()
  return input_data
