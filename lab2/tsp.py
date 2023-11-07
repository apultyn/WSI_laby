from solver import Solver
import numpy as np


class TSP(Solver):
    def __init__(self, cities: list):
        self._cities = cities
        self._epochs = None
        self._starting_population = None
        self._parents = None
        self._mutate_rate = None
        self._alpha = None

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
              parents, mutate_rate, alpha):
        self._epochs = epochs
        self._starting_population = starting_population
        self._parents = parents
        self._mutate_rate = mutate_rate
        self._alpha = alpha

        def calc_value(order):
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
            return value

        if parents > starting_population:
            raise ValueError("Not enough population for this amount of parents")
        if parents % 2 != 0:
            raise ValueError("Amount of parents must be even number")

        population = []
        for _ in range(starting_population):
            order = np.random.permutation(len(self._cities))
            population.append((order, calc_value(order)))

        population.sort(key=lambda x: x[1])

        for _ in range(epochs):
            parents_list = population[:parents]
            for i in range(0, parents, 2):
                parent1, parent2 = parents_list[i], parents_list[i+1]
                separator = int(len(parent1[0]) * self._alpha)

                head_first = parent1[0][:separator]
                tail_first = parent1[0][separator:]
                tail_second = parent2[0][separator:]

                mapping = {tail_second[i]: tail_first[i] for i in range(len(tail_first))}

                for i in range(len(head_first)):
                    while head_first[i] in tail_second:
                        head_first[i] = mapping[head_first[i]]

                offspring_order = np.concatenate((head_first, tail_second))

                if np.random.random() < self._mutate_rate:
                    j, k = np.random.choice(range(len(parent1[0])), 2, replace=False)
                    offspring_order[j], offspring_order[k] = offspring_order[k], offspring_order[j]
                population.append((offspring_order, calc_value(offspring_order)))
            population.sort(key=lambda x: x[1])
            del population[-(parents // 2):]
            print("New population")

        print("After: ")
        print(population[:10])
