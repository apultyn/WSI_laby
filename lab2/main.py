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
for _ in range(20):
    x, y = np.random.randint(-300, 300), np.random.randint(-300, 300)
    random.append([x, y])
solver4 = TSP(random)


def main():
    # solver.solve(1000, 1000, 600, 0.5, 0.7)
    # solver2.solve(10, 10, 4, 0.6, 0.5)
    # solver3.solve(100, 10000, 4000, 0.6, 0.5)
    solver4.solve(10000, 1000, 400, 0.7, 0.5)


if __name__ == "__main__":
    main()
