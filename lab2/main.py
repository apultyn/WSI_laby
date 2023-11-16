from tsp import TSP
import numpy as np

solver = TSP([
    [35, 51],
    [113, 213],
    [82, 280],
    [322, 340],
    [256, 352],
    [160, 24],
    [322, 145],
    [12, 349],
    [282, 20],
    [241, 8],
    [398, 153],
    [182, 305],
    [153, 257],
    [275, 190],
    [242, 75],
    [19, 229],
    [303, 352],
    [39, 309],
    [383, 79],
    [226, 343]])

solver2 = TSP([
    [-2, 0],
    [0, 0],
    [-2, 2],
    [2, 0],
    [2, 2],
    [0, 2]])

solver3 = TSP([
    [1, 1],
    [-2, -2],
    [3, -1],
    [-4, 5],
    [3, -2]])


random = []
for _ in range(50):
    x, y = np.random.randint(-300, 300), np.random.randint(-300, 300)
    random.append([x, y])
solver4 = TSP(random)


def main():
    # solver.solve(20000, 10000, 1000, 400, 0.1, 20, 0.5, "task_strong_mutate")
    # solver.solve(20000, 10000, 1000, 400, 0.8, 5, 0.5, "task_often_mutate")
    # solver.solve(20000, 10000, 1000, 400, 0.8, 5, 0.5, "task_often_mutate_2")
    # solver.solve(20000, 10000, 1000, 200, 0.5, 10, 0.5, "low_parents")
    # solver.solve(20000, 10000, 1000, 800, 0.5, 10, 0.5, "high_parents")
    solver4.solve(50000, 20000, 1000, 400, 0.8, 20, 0.5, "50_random_cities")


if __name__ == "__main__":
    main()
