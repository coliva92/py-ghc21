import ghc
import ghc.competition as cmp




if __name__ == '__main__':
  in_desc = [
    {
      'name': 'general',
      'columns': [
        { 'name': 'sim_duration', 'type': int },
        { 'name': 'num_inter', 'type': int },
        { 'name': 'num_streets', 'type': int },
        { 'name': 'num_cars', 'type': int },
        { 'name': 'bonus_points', 'type': int }
      ]
    },
    {
      'name': 'streets',
      'row_count': 'general num_streets',
      'columns': [
        { 'name': 'start_inter_id', 'type': int },
        { 'name': 'end_inter_id', 'type': int },
        { 'name': 'street_name', 'type': str },
        { 'name': 'travel_time', 'type': int }
      ]
    },
    {
      'name': 'cars',
      'row_count': 'general num_cars',
      'columns': [
        { 'name': 'travel_length', 'type': int },
        { 'name': 'travel_streets', 'type': str, 'repeat': '*' }
      ]
    }
  ]
  in_filename, out_filename = ghc.get_args(cmp.PROBLEM_NAME, cmp.YEAR)
  in_data = ghc.read_input_file(in_filename, in_desc)
  G = cmp.to_networkx_graph(in_data['streets'])
  intersections = cmp.get_in_edges_for_every_vertex(G)
  histogram = cmp.create_street_usage_histogram(in_data['cars'])
  out_data = cmp.create_schedule_with_stop_signs_only(intersections, histogram)
  cmp.write_output_file(out_filename, out_data)
