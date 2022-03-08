import numpy as np
import mip.model
import mip.constants

from structs import Grid, Sensor

def generate_model(grid:Grid, sensors:list) -> dict:
    """
        Description:
            Generates a model and the variable matrices
            which will be used for optimizing

        Arguments:
            - grid : `Grid` grid that the sensors are located on
            - sensors : `list` array storing the sensors

        Return:
            - `dict` : package storing the model and
            the model variables
    """
    model = mip.model.Model() # Model is generated

    # Potential gateway locations on the grid 
    gateway_locations = [
        [
            model.add_var(
                var_type=mip.constants.BINARY
                ) for _ in range(grid.get_width())
        ] for _ in range(grid.get_height())
    ]

    # Number of clusters included for each sensor
    number_of_clusters = [
        model.add_var(
            lb=0, ub=mip.constants.INT_MAX,
            var_type=mip.constants.INTEGER
        ) for sensor in sensors
    ]

    # Send the variables as package (there will be changes in further steps)
    package = {
        'model': model,
        'gateway_locations': gateway_locations,
        'number_of_clusters': number_of_clusters,
    }

    return package
