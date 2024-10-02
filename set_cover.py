from random import random, seed
from itertools import accumulate, product
from matplotlib import pyplot as plt
import numpy as np

UNIVERSE_SIZE = 1000
NUM_SETS = 100
DENSITY = 0.2

rng = np.random.Generator(np.random.PCG64([UNIVERSE_SIZE, NUM_SETS, int(10_000 * DENSITY)]))

# DON'T EDIT THESE LINES!

SETS = np.random.random((NUM_SETS, UNIVERSE_SIZE)) < DENSITY
for s in range(UNIVERSE_SIZE):
    if not np.any(SETS[:, s]):
        SETS[np.random.randint(NUM_SETS), s] = True
COSTS = np.power(SETS.sum(axis=1), 1.1)

def valid(solution):
    """Checks wether solution is valid (ie. covers all universe)"""
    return np.all(np.logical_or.reduce(SETS[solution]))


def cost(solution):
    """Returns the cost of a solution (to be minimized)"""
    return COSTS[solution].sum()

def tweak(solution):
    new_solution = solution.copy()
    index = None
    while index is None or np.random.random() < 0.4:
        index = np.random.randint(0, NUM_SETS)
        new_solution[index] = not new_solution[index]
    return new_solution

solution = np.full(NUM_SETS, True)

history = [cost(solution)]
print(f"Initial cost : {cost(solution)}")
if valid(solution):

    for n in range(UNIVERSE_SIZE):
        new_solution = tweak(solution)
        #print(new_solution)
        history.append(cost(new_solution))
        if valid(new_solution) and cost(new_solution) < cost(solution):
            solution = new_solution

    print(f"Final cost : {cost(solution)}")
    print(f"Number of sets used: {solution.sum()}")
    print(f"Last improvement at: {history.index(cost(solution))}")

else:
    print("impossible to find a solution")

plt.figure(figsize=(14, 8))
plt.plot(
    range(len(history)),
    list(accumulate(history, min)),
    color="red",
)
plt.scatter(range(len(history)), history, marker=".")
plt.show()