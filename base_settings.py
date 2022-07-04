# Inputs
SENSOR_LOCATIONS_INPUT = 'docs/input/sensor_locations.tsv'
SENSOR_SCORES_INPUT = 'docs/input/sensor_placements.csv'

# Visualizations
SENSOR_LOCATIONS_PATH = 'docs/output/base/visualizations/_sensor_locations.png'
GATEWAY_PLACEMENTS_PATH = lambda n, dt : f'docs/output/base/visualizations/top_{n}_sensors/{int(dt)}_km_coverage_gateway_placements.png'

# Output as Units
SENSOR_LOCATIONS_UNITS_PATH = 'docs/output/base/units/_sensor_locations_units.txt'
GATEWAY_PLACEMENTS_UNITS_PATH = lambda n, dt : f'docs/output/base/units/top_{n}_sensors/{int(dt)}_km_coverage_gateway_placements.txt'
ALL_GATEWAY_PLACEMENTS_UNITS_PATH = lambda dt : f'docs/output/base/units/{int(dt)}_km_coverage_all_gateway_placements.txt'

# Output as Coordinates
SENSOR_LOCATIONS_COOR_PATH = 'docs/output/base/coordinates/_sensor_locations_coordinates.txt'
GATEWAY_PLACEMENTS_COOR_PATH = lambda n, dt : f'docs/output/base/coordinates/top_{n}_sensors/{int(dt)}_km_coverage_gateway_placements.txt'
ALL_GATEWAY_PLACEMENTS_COOR_PATH = lambda dt : f'docs/output/base/coordinates/{int(dt)}_km_coverage_all_gateway_placements.txt'

# Output as LoraPlan Format
LORAPLAN_SENSOR_LOCATIONS = 'docs/output/base/loraplan_format/sensor_locations.csv'
LORAPLAN_GATEWAY_PLACEMENTS = lambda dt : f'docs/output/base/loraplan_format/{int(dt)}_km_coverage_gateway_placements.csv'
