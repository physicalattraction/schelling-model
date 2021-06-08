# schelling-model
Python Implementation of Schelling segregation Model

Based on: https://www.binpress.com/simulating-segregation-with-python/

## Examples

N | Tolerance | Initial | Final
--- | --- | --- | ---
1 | 30% | ![2 races, 30% intolerance, initial](img/schelling_2_30_01_initial.png) | ![2 races, 30% intolerance, final](img/schelling_2_30_02_final.png)
2 | 50% | ![2 races, 50% intolerance, initial](img/schelling_2_50_01_initial.png) | ![2 races, 50% intolerance, final](img/schelling_2_50_02_final.png)
3 | 80% | ![2 races, 850% intolerance, initial](img/schelling_2_80_01_initial.png) | ![2 races, 80% intolerance, final](img/schelling_2_80_02_final.png)
4 | 30% | ![7 races, 30% intolerance, initial](img/schelling_7_30_01_initial.png) | ![7 races, 30% intolerance, final](img/schelling_7_30_02_final.png)
5 | 30% | ![7 races, 30% intolerance, initial](img/schelling_7_30_03_initial.png) | ![7 races, 30% intolerance, final](img/schelling_7_30_04_final.png)
6 | 30% | ![7 races, 30% intolerance, initial](img/schelling_7_30_05_initial.png) | ![7 races, 30% intolerance, final](img/schelling_7_30_06_final.png)

Parameters:
- In simulations 1, 2 and 3, we have a 50x50 grid with 2 races, 70% occupancy. In simulation 3, we did not reach convergence yet after 100 iterations.
- In simulation 4, we have a 50x50 grid with 7 races, 70% occupancy.
- In simulations 5 and 6, we have a 70x70 grid with 7 races, 40% occupancy. In simulation 5, an agent with no neighbors at all is considered unhappy, in simulation 6 they are considered happy.
