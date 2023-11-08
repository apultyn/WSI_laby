from solver import Solver
import matplotlib.pyplot as plt
import numpy as np


class TSP(Solver):
    def __init__(self, cities: list):
        self._cities = cities
        self._epochs = None
        self._limit = None
        self._starting_population = None
        self._parents = None
        self._mutate_rate = None
        self._mutate_amount = None
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

        mapping = {tail_second[i]: tail_first[i]
                   for i in range(len(tail_first))}

        for i in range(len(head_first)):
            while head_first[i] in tail_second:
                head_first[i] = mapping[head_first[i]]

        return np.ndarray.tolist(np.concatenate((head_first, tail_second)))

    def plot_result(self, order):
        x = [self._cities[i][0] for i in order]
        y = [self._cities[i][1] for i in order]

        # Connect the last and first points to form a closed loop
        x.append(x[0])
        y.append(y[0])

        plt.plot(x, y, marker='o', linestyle='-')
        plt.title('Shortest Way')
        plt.show()

    def plot_evolution(self, shortest, epochs):
        plt.plot(range(1, epochs + 2), shortest)
        plt.title('Evolution of Shortest Way Length')
        plt.xlabel('Epochs')
        plt.ylabel('Shortest Way Length')
        plt.show()

    def solve(self, epochs, limit, starting_population,
              parents, mutate_rate, mutate_amount, alpha):
        self._epochs = epochs
        self._limit = limit
        self._starting_population = starting_population
        self._parents = parents
        self._mutate_rate = mutate_rate
        self._mutate_amount = mutate_amount
        self._alpha = alpha

        if parents > starting_population:
            raise ValueError(
                "Not enough population for this amount of parents")
        if parents % 2 != 0:
            raise ValueError("Amount of parents must be even number")

        population = []
        for _ in range(starting_population):
            order = np.ndarray.tolist(np.random.permutation(len(self._cities)))
            population.append((order, self.calc_value(order)))

        population.sort(key=lambda x: x[1])

        shortest_list = [population[0][1]]
        shortest_prev = None
        count_repeated = 0
        count = epochs

        for i in range(epochs):
            print(f"Epoch: {i+1}")
            parents_list = population[:parents]

            for j in range(0, parents, 2):
                parent1, parent2 = parents_list[j][0], parents_list[j+1][0]
                offspring = self.pair(parent1, parent2)
                if np.random.random() < self._mutate_rate:
                    for _ in range(np.random.randint(0, self._mutate_amount)):
                        j, k = np.random.choice(
                            range(len(parent1)), 2, replace=False)
                        offspring[j], offspring[k] = offspring[k], offspring[j]
                population.append((offspring, self.calc_value(offspring)))
            population.sort(key=lambda x: x[1])

            shortest = population[0][1]
            shortest_list.append(shortest)

            if shortest_prev is None or shortest < shortest_prev:
                shortest_prev = shortest
                count_repeated = 1
            else:
                count_repeated += 1
            if count_repeated > limit:
                count = i + 1
                break

            del population[-(parents // 2):]

        self.plot_result(population[0][0])
        self.plot_evolution(shortest_list, count)
