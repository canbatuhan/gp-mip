# gp-mip : Gateway Placement with Mixed-Integer Programming

`gp-mip` is a package written in order to solve the Gateway Placement Problem by approaching it under the concept of Mixed-Integer Programming. In this package, there two main sub-packages namely `functions` and `structs`.


## functions : sub-package

`functions` includes the methods being used in the runtime. In this sub-package, functions are divided into modules according to their usages. Under `functions`, there are 5 different modules,

  - preprocessing.py : functions that read and modify the input accordingly
  - clustering.py : functions that generate, develop and run the module 
  - postprocessing.py : functions that modify the output accordingly and write the results
  - visualization.py : functions that visualize the output of the model
  - helpers.py : small scripts that are used in other modules
