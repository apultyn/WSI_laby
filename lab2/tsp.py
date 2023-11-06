from solver import Solver
import numpy as np


class TSP(Solver):
    def __init__(self, cities: list):
        self._cities = cities
        self._epochs = None
        self._starting_population = None
        self._parents = None
        self._mutate_rate = None

    def get_parameters(self):
        """Returns last sollution hyperparameters"""
        return {
            "cities": self._cities,
            "epochs": self._epochs,
            "starting_population": self._starting_population,
            "parents": self._parents,
            "mutate_rate": self._mutate_rate
        }

    def solve(self, epochs, starting_population,
              parents, mutate_rate):
        self._epochs = epochs
        self._starting_population = starting_population
        self._parents = parents
        self._mutate_rate = mutate_rate

        if parents > starting_population:
            raise ValueError("Not enough population for this amount of parents")
        if parents % 2 != 0:
            raise ValueError("Amount of parents must be even number")

        population = []
        for _ in range(starting_population):
            order = np.random.permutation(len(self._cities))
            value = 0
            for i in range(len(order) - 1):
                value += np.sqrt(
                    np.square(self._cities[order[i+1]][0] -
                              self._cities[order[i]][0]) +
                    np.square(self._cities[order[i+1]][1] -
                              self._cities[order[i]][1]))
            value += np.sqrt(
                np.square(self._cities[order[-1]][0] -
                          self._cities[order[0]][0]) +
                np.square(self._cities[order[-1]][1] -
                          self._cities[order[0]][1]))
            population.append((order, value))

        def sort_val(x):
            return x[1]
        population.sort(reverse=True, key=sort_val)

        print(population)
