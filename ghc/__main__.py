import ghc
import ghc.competition as cmp




if __name__ == '__main__':
  in_filename, out_filename = ghc.get_args(cmp.PROBLEM_NAME, cmp.YEAR)
  in_desc = [
    # llenar con la descripcion de los datos de entrada
  ]
  in_data = ghc.read_input_file(in_filename, in_desc)
  # procesar los datos de entrada segun el problema de la competencia
  # escribir los resultados en un archivo almacenado en la ruta out_filename
