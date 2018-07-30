
from enum import Enum
import numpy as np


class SearchMethods(Enum):
    random = 1
    tree_parzen_estimators = 2
    tpe = 2


def random_search(objective_func, search_space, iterations):
    aggregate = []
    lowest = {"params": {}, "value": None, "eval": []}

    for item in search_space:
        aggregate.append({})
        # TODO: check types
        for key, value in item.items():
            aggregate[-1][key] = np.random.uniform(value["min"], value["max"], size=iterations)

    for item in aggregate:
        val = None
        for key, value in item.items():
            val = value[0]
            lowest["params"][key] = value[0]

        lowest["eval"].append(val)

    # print(lowest["eval"])

    lowest["value"] = objective_func(lowest["eval"])

    for i in range(1, iterations):
        current = {"eval": [], "params": {}}

        for item in aggregate:
            val = None
            for key, value in item.items():
                val = value[0]
                current["params"][key] = value[0]

                current["eval"].append(val)

        value = objective_func(current["eval"])
        if value is None:
            raise Exception(f"Objective function doesn't return a value for {current}")

        if value < lowest["value"]:
            lowest["value"] = value
            lowest["params"] = current["params"].copy()
            lowest["eval"] = current["eval"].copy()

    return lowest["params"]

#
#
# def fmin(func, search_space, iterations, method):
#     if method is SearchMethods.random:
