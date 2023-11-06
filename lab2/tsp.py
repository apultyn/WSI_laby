from solver import Solver
import numpy as np


class TSP(Solver):
    def __init__(self, cities: list):
        self._cities = cities
        self._epochs = None
        self._starting_population = None
        self._parents = None
        self._offsprings = None
        self._dying_amount = None

    def get_parameters(self):
        """Returns last sollution hyperparameters"""
        return {
            "cities": self._cities,
            "epochs": self._epochs,
            "starting_population": self._starting_population,
            "parents": self._parents,
            "offsprings": self._offsprings,
            "dying_amount": self._dying_amount
        }

    def solve(self, epochs, starting_population,
              parents, offsprings, dying_amount):
        self._epochs = epochs
        self._starting_population = starting_population
        self._parents = parents
        self._offsprings = offsprings
        self._dying_amount = dying_amount

        population = []
        for _ in range(starting_population):
            order = np.random.permutation(len(self._cities))
            value = 0
            for i in range(len(order) - 1):
                value += np.sqrt(
                    np.square(self._cities[order[i+1]][0] - self._cities[order[i]][0]) +
                    np.square(self._cities[order[i+1]][1] - self._cities[order[i]][1]))
            value += np.sqrt(
                np.square(self._cities[order[-1]][0] - self._cities[order[0]][0]) +
                np.square(self._cities[order[-1]][1] - self._cities[order[0]][1]))
            population.append((order, value))
        print(population)
