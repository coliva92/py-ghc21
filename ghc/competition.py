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



def create_schedule_with_stop_signs_only(intersections):
  schedule = {
    'num_inter': len(intersections),
    'intersections': []
  }
  for i in intersections.keys():
    schedule['intersections'].append(_create_inter_schedule(i, 
                                                            intersections[i]))
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
                           in_streets):
  schedule = {
    'id': idx,
    'num_streets': len(in_streets),
    'streets': []
  }
  for street_name in in_streets:
    schedule['streets'].append({ 
      'name': street_name,
      'time_on_green': 1
    })
  return schedule
