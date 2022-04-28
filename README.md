# Gateway Placement with Mixed-Integer Programming

`gp-mip` is a package written in order to solve the Gateway Placement Problem by approaching it under the concept of Mixed-Integer Programming. In this documentation, libraries of the package will be introduced, and an example execution will be presented.


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


