# COMPUTATIONAL INTELLIGENCE LAB1
## SET COVER OPTIMIZATION

The solution provided is a custom version of simulated annealing algorithm. 

## INSTANCES 

The following table shows the instances observed and used for the study.

| Instance | Universe Size | Num Sets | Density |
| -------- | ------------- | -------- | ------- |
| 1        | 100           | 10       | 0.2     |
| 2        | 1_000         | 100      | 0.2     |
| 3        | 10_000        | 1_000    | 0.2     |
| 4        | 100_000       | 10_000   | 0.1     |
| 5        | 100_000       | 10_000   | 0.2     |
| 6        | 100_000       | 10_000   | 0.3     |

## HYPERPARAMETERS

The number of Iteration for each instance experiment is proportional to the size of the universe.
The initial cost for each experiment is related to a initial random group of sets with 75% probability of a True set, this factor is given by empirical trial and error tests.
With the same approach the initial Temperature (0.5) and cooling down factor (1.2) have been chosen for the optimization of the problem.
The constraint of the buffer to decide whether to increase/decrease the Temperature follows instead the 1 out of 5 rule.
The buffer size is proportional to the number of sets.

## SOLUTIONS

The following table shows the best overall results reached by the optimization algorithm for each instance (1-6).    

| Instance | N Iterations | Final Num Sets | Initial Cost | Final Cost | Iteration of last improvement | Optimization Factor |
| -------- | ------------ | -------------- | ------------ | ---------- | ----------------------------- | ------------------- |
| 1        | 100          | 10             | 284          | 284        | 0                             | x 1.00              |
| 2        | 1_000        | 19             | 25_197       | 6_569      | 306                           | x 3.83              |
| 3        | 10_000       | 1_000          | 3_194_701    | 124_012    | 4_527                         | x 25.76             |
| 4        | 100_000      | 77             | 188_380_998  | 1_927_945  | 85_551                        | x 97.71             |
| 5        | 100_000      | 40             | 404_371_199  | 2_154_868  | 61_229                        | x 187.65            |
| 6        | 100_000      | 25             | 628_947_782  | 2_102_807  | 68_688                        | x 299.10            |



