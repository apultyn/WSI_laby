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

    def calc_value(self, order):
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

    def pair(self, parent1, parent2):
        separator = int(len(parent1) * self._alpha)

        head_first = parent1[:separator]
        head_second = parent2[:separator]
        tail_first = parent1[separator:]
        tail_second = parent2[separator:]

        if np.array_equal(head_first, head_second):
            return parent1

        mapping = {tail_second[i]: tail_first[i] for i in range(len(tail_first))}

        for i in range(len(head_first)):
            while head_first[i] in tail_second:
                head_first[i] = mapping[head_first[i]]

        return np.ndarray.tolist(np.concatenate((head_first, tail_second)))

    def solve(self, epochs, starting_population,
              parents, mutate_rate, alpha):
        self._epochs = epochs
        self._starting_population = starting_population
        self._parents = parents
        self._mutate_rate = mutate_rate
        self._alpha = alpha


        if parents > starting_population:
            raise ValueError("Not enough population for this amount of parents")
        if parents % 2 != 0:
            raise ValueError("Amount of parents must be even number")

        population = []
        for _ in range(starting_population):
            order = np.ndarray.tolist(np.random.permutation(len(self._cities)))
            population.append((order, self.calc_value(order)))

        population.sort(key=lambda x: x[1])

        for i in range(epochs):
            print(f"Epoch: {i+1}")
            parents_list = population[:parents]

            for j in range(0, parents, 2):
                parent1, parent2 = parents_list[j][0], parents_list[j+1][0]
                offspring = self.pair(parent1, parent2)
                if np.random.random() < self._mutate_rate:
                    j, k = np.random.choice(range(len(parent1)), 2, replace=False)
                    offspring[j], offspring[k] = offspring[k], offspring[j]
                population.append((offspring, self.calc_value(offspring)))
            population.sort(key=lambda x: x[1])
            del population[-(parents // 2):]

        print("3 shortest ways:")
        for i in range(3):
            print(population[i][0])
