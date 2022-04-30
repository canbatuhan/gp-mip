# Gateway Placement with Mixed-Integer Programming

`gp-mip` is a package written in order to solve the Gateway Placement Problem by approaching it within the concept of Mixed-Integer Programming. In this documentation, libraries of the package will be introduced, and an example execution will be presented.


## Libraries 

### functions

`functions` includes the methods being used in the runtime. In this sub-package, functions are divided into modules according to their usages. Under this sub-package, there are 5 different modules,

  - `preprocessing.py` : reads input and rearranges it in order to used in following steps
  - `clustering.py` : generates an optimization model, develops it and runs 
  - `postprocessing.py` : rearranges the output and writes the results
  - `visualization.py` : visualizes the output taken from the model
  - `helpers.py` : small scripts that are used in other modules

### structs

`structs` includes the classes written in order to develop the optimization model more easily. There are two main classes written for this package,

  - `grid.py` : class in order to represent the grid system that the optimization model runs on
  - `node.py` : class used to represent the elements considered in the model; `Gateway` and `Sensor`


## Example

In the following example, a sensor network is given to the program. Aim in this instance is to determine placement locations for gateways which satisfy the following conditions,
   
   - There must not be a single sensor uncovered
   - All the sensors must be connected to only one gateway
   - Clusters of sensors must satisfy an average score, in overall

It is important to cover all the sensors in the network, since background aim is to have comprehensive data. Sensors are supposed to communicate with only one gateway, otherwise it would cause interference. Also one of the aims is to have high quality data, therefore it is important for the clusters to have an average score greater than the threshold value, which is passed as an argument.


### Input Data

In the given example, there are two input data. With input data, program is able to know the location of all the sensors, and scores for some of the sensors in network. Score of other sensors are assigned to be lowest score in the network, because it is better to simulate worst-case scenario.

  - `sensor_location.tsv` : stores the location of all the sensors in network
  - `sensor_placement.csv` : scores of some of the sensors in the same network

### Output Data

In `gp-mip`, output data is given in three different ways. Since the model is built within the Mixed-Integer Programming concept. The input data is transformed into a integer-based form, by mapping the geograhical location data to a integer in range (0,n). Afterwards, the model run on a nxn grid. At the end of the optimization, result of the model represents the location of the gateways. These data is used to visualize the sensor network and determined locations of gateway. Lastly, this output data is logged as integers, then re-transformed into a geographical location data and logged again. Therefore there are three different output of the program.

  - `img/n_km_coverage_grid.png` : Visual output of the sensor network and the gateway locations
  - `log_coor/n_km_coverage_gateways_coor.txt` : Geographical data of gateway locations
  - `log_unit/n_km_coverage_gateways_unit.txt` : Integer-based data of gateway locations

![An example for visual output](https://github.com/canbatuhan/gp-mip/blob/main/docs/output/img/top_30_sensors/10_km_coverage_grid.png)
