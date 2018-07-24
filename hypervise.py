
from enum import Enum
import numpy as np


class SearchMethods(Enum):
    random = 1
    tree_parzen_estimators = 2
    tpe = 2


def random_search(objective_func, search_space, iterations):
    aggregate = {}
    lowest = {"params": {}, "value": None}

    # TODO: check types
    for key, value in search_space.items():
        aggregate[key] = np.random.uniform(value["min"], value["max"], size=iterations)

    for key, value in search_space.items():
        lowest["params"][key] = aggregate[key][0]

    lowest["value"] = objective_func(lowest["params"])

    for i in range(1, iterations):
        current = {}
        for key, value in search_space.items():
            current[key] = aggregate[key][i]

        value = objective_func(current)
        if value is None:
            raise Exception(f"Objective function doesn't return a value for {current}")

        if value < lowest["value"]:
            lowest["value"] = value
            lowest["params"] = current.copy()

    return lowest

#
#
# def fmin(func, search_space, iterations, method):
#     if method is SearchMethods.random:
