# Input File Paths
SENSOR_LOCATIONS_INPUT = 'docs/input/sensor_locations.tsv'
SENSOR_SCORES_INPUT = 'docs/input/sensor_placements.csv'

# Output File Paths
SENSOR_LOCATIONS_PATH = 'docs/output/gateway_placements_visualizations/_sensor_locations.png'
GATEWAY_PLACEMENTS_PATH = lambda n, dt : f'docs/output/gateway_placements_visualizations/top_{n}_sensors/{int(dt)}_km_coverage_gateway_placements.png'
SENSOR_LOCATIONS_UNITS_PATH = 'docs/output/gateway_placements_units/_sensor_locations_units.txt'
GATEWAY_PLACEMENTS_UNITS_PATH = lambda n, dt : f'docs/output/gateway_placements_units/top_{n}_sensors/{int(dt)}_km_coverage_gateway_placements.txt'
ALL_GATEWAY_PLACEMENTS_UNITS_PATH = lambda dt : f'docs/output/gateway_placements_units/{int(dt)}_km_coverage_all_gateway_placements.txt'
SENSOR_LOCATIONS_COOR_PATH = 'docs/output/gateway_placements_coordinates/_sensor_locations_coordinates.txt'
GATEWAY_PLACEMENTS_COOR_PATH = lambda n, dt : f'docs/output/gateway_placements_coordinates/top_{n}_sensors/{int(dt)}_km_coverage_gateway_placements.txt'
ALL_GATEWAY_PLACEMENTS_COOR_PATH = lambda dt : f'docs/output/gateway_placements_coordinates/{int(dt)}_km_coverage_all_gateway_placements.txt'
