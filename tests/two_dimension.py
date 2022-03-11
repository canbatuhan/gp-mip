import numpy as np
import matplotlib.pyplot as plt
import mip


GRID_SIZE = 100
SENSOR_COUNT = 75
COVERAGE_DIST = 15
GRID = [[0]*GRID_SIZE]*GRID_SIZE


def calc_distance(point1:tuple, point2:tuple) -> int:
    x1, y1 = point1
    x2, y2 = point2
    return int(np.sqrt((x1-x2)**2 + (y1-y2)**2))


sensor_locations = list()
for _ in range(SENSOR_COUNT):
    sensor_location = (np.random.randint(0, GRID_SIZE), np.random.randint(0, GRID_SIZE))
    sensor_locations.append(sensor_location)

for (x, y) in sensor_locations:
    GRID[y][x] = 1

model = mip.Model()

gateway_locations = [
    [
        model.add_var(var_type=mip.BINARY) for _ in range(GRID_SIZE)
    ] for _ in range(GRID_SIZE)
]

"""model.objective = mip.minimize(
    mip.xsum(
        gateway_locations[y][x] for y in range(GRID_SIZE) for x in range(GRID_SIZE)
    )
)"""

model.objective = mip.minimize(
    mip.xsum(
        [
            gateway_locations[gateway_y][gateway_x]*(2 < calc_distance(
                (sensor_x, sensor_y), (gateway_x, gateway_y)
            ) <= COVERAGE_DIST)
            for gateway_y in range(GRID_SIZE) for gateway_x in range(GRID_SIZE)
            for sensor_x, sensor_y in sensor_locations
        ]
    )
)

for (sensor_x, sensor_y) in sensor_locations:
    model += mip.xsum(
        [
            gateway_locations[gateway_y][gateway_x]*(2 < calc_distance(
                (sensor_x, sensor_y), (gateway_x, gateway_y)
            ) <= COVERAGE_DIST)
            for gateway_y in range(GRID_SIZE) for gateway_x in range(GRID_SIZE)
        ]
    ) >= 1

model.optimize()

sensor_x_data = list()
sensor_y_data = list()
for (x, y) in sensor_locations:
    sensor_x_data.append(x)
    sensor_y_data.append(y)
    print('Sensor Location: ({}, {})'.format(x, y))

gateway_count = 0
gateway_x_data = list()
gateway_y_data = list()
for gateway_y in range(GRID_SIZE):
    for gateway_x in range(GRID_SIZE):
        if gateway_locations[gateway_y][gateway_x].x:
            gateway_count += 1
            gateway_x_data.append(gateway_x)
            gateway_y_data.append(gateway_y)

            for (sensor_x, sensor_y) in sensor_locations:
                distance = calc_distance((sensor_x, sensor_y), (gateway_x, gateway_y))
                if distance <= COVERAGE_DIST:
                    plt.plot([gateway_x, sensor_x], [gateway_y, sensor_y], color="g")

            print("Gateway Location: ({}, {})".format(gateway_x, gateway_y))

plt.scatter(sensor_x_data, sensor_y_data, label="Sensors", s=50)
plt.scatter(gateway_x_data, gateway_y_data, label="Gateways", s=20)
plt.xlim(0, GRID_SIZE)
plt.ylim(0, GRID_SIZE)
plt.legend()
plt.plot()
plt.show()
