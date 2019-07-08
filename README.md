## `Multiprocessing`
This folder contains two examples of multiprocessing work: with Memory Manager and without

Order of tutorials:

### Process folder
- `1_ex_Process.py` provides basic example how to define and run simultaneously multiple processes
- `2_ex_Process.py` modifies 1st example by applying list comprehension for processes
- `3_ex_Process.py` modifies 1st example by adding a Queue object, which allows to share return values from different processes
- `4_ex_Process.py` modifies 3rd example by illustrating that each function can return value of various types: np.array, pd.DataFrame, str and so on

### Pool folder
- `1_ex_Pool.py` provides basic example for Pool and map function 
- `2_ex_Pool.py` modifies 1st example with adding mp.cpu_count() function
- `3_ex_Pool.py` modifies 2nd example with adding another map function
- `4_ex_Pool_Graph.py` provides example of using Pool for finding paths in Graph for all pairs of nodes 

### example_multiproc_with_manager.py
Illustrates example how to use Memory Manager