# Testing, performance, Memory Management in pandas

## Running magic commands in ipython for checking code performance
```
type ipython in the terminal and then use %run magic to load the python script[%run script.py]
```
## How to use timeit module in the terminal

```
%timeit <function(data)> in ipython kernel
python -m timeit -c "$(cat file_name.py)" in bash terminal
```
## To run the benchmark

```
python -m pytest
```

## To run the profiling

```
%%prun <function(data)> in ipython kernel
%prun -s cumulative <function(data)> 
```
## To run cython file

```
python setup.py build_ext --inplace
```
