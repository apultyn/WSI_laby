from tsp import TSP


def main():
    solver = TSP([[1, 1], [2, 0], [-1, -1], [-2, 0], [0, 0], [-1, 1], [1, -1]])
    solver.solve(100, 10, 4, 2, 2)


if __name__ == "__main__":
    main()
