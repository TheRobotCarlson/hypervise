from hypervise import random_search
import numpy as np
from hyperopt import fmin, hp, tpe, rand, Trials


def objective_func(x):
    return np.poly1d([1, -2, -28, 28, 12, -26, 100])(x)*0.05


print(random_search(objective_func=objective_func, search_space=[{"x": {"min": 0, "max": 5}}], iterations=1000))

print(fmin(objective_func, space=hp.uniform('x', 0, 5), algo=rand.suggest, max_evals=1000))
