from tsp import TSP


def main():
    solver = TSP([[-20, -20], [-24, -20]])
    solver.solve(100, 30, 8, 4, 4)

if __name__ == "__main__":
    main()
