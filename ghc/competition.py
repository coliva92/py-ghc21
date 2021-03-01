import networkx as nx


PROBLEM_NAME = 'Traffic signaling'
YEAR = 2021




def to_networkx_graph(streets):
  G = nx.DiGraph()
  for street in streets:
    G.add_edge(street['start_inter_id'], 
               street['end_inter_id'], 
               street_name=street['street_name'],
               travel_time=street['travel_time'])
  return G



def get_in_edges_for_every_vertex(G):
  in_streets = {}
  for v in G.nodes.keys():
    in_edges = G.in_edges(v, data=True)
    if len(in_edges) > 0:
      in_streets[v] = []
      for edge in in_edges:
        in_streets[v].append(edge[2]['street_name'])
  return in_streets



def create_street_usage_histogram(cars):
  histogram = {}
  for car in cars:
    for street_name in car['travel_streets']:
      if street_name in histogram: histogram[street_name] += 1
      else: histogram[street_name] = 1
  return histogram



def create_schedule_with_stop_signs_only(intersections, histogram):
  schedule = {
    'num_inter': 0,
    'intersections': []
  }
  for i in intersections.keys():
    inter_schedule = _create_inter_schedule(i, 
                                            intersections[i],
                                            histogram)
    if inter_schedule['num_streets'] > 0:
      schedule['num_inter'] += 1
      schedule['intersections'].append(inter_schedule)
  return schedule



# Escribe los datos contenidos en data en un archivo de texto en la direccion
# especificada por filename.
# filename (str):   ruta completa del archivo que sera creado
# data (any):       los datos a almacenar en el archivo
def write_output_file(filename, 
                      data):
  file = open(filename, 'wt')
  file.write('{}\n'.format(data['num_inter']))
  for inter in data['intersections']:
    file.write('{}\n{}\n'.format(inter['id'], inter['num_streets']))
    for street in inter['streets']:
      file.write('{} {}\n'.format(street['name'], street['time_on_green']))
  file.close()



def _create_inter_schedule(idx, 
                           in_streets,
                           histogram):
  schedule = {
    'id': idx,
    'num_streets': 0,
    'streets': []
  }
  for street_name in in_streets:
    if street_name in histogram:
      schedule['num_streets'] += 1
      schedule['streets'].append({ 
        'name': street_name,
        'time_on_green': 1
      })
  return schedule
