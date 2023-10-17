import matplotlib.pyplot as plt
import numpy as np
from gradient import Gradient_descent


def f(x):
    return (x**4) / 4


def g(x):
    return (1.5 - np.exp(-x[0]**2 - x[1]**2) - 0.5 *
            np.exp(-((x[0] - 1)**2) - ((x[1] + 2)**2)))


def gradient_f(x):
    return x**3


def gradient_g(x):
    return np.array([2 * x[0] * np.exp(-x[0]**2 - x[1]**2) + (x[0] - 1) *
                     np.exp(-((x[0] - 1)**2) - ((x[1] + 2)**2)),
                     2 * x[1] * np.exp(-x[0]**2 - x[1]**2) + (x[1] + 2) *
                     np.exp(-((x[0] - 1)**2) - ((x[1] + 2)**2))
                     ])


def main():
    func_f = Gradient_descent(f, gradient_f, 1, 0.1, 0.001)
    trajectory_f = func_f.solve(np.array([-2.5]))

    func_g = Gradient_descent(g, gradient_g, 0.5, 0.1, 0.001)
    trajectory_g = func_g.solve(np.array([-1.5, 2]))

    x_values_f = np.linspace(-4, 4, 100)
    x_values_g = np.linspace(-4, 4, 100)
    y_values_f = f(x_values_f)
    y_values_g = np.zeros((100, 100))

    for i in range(100):
        for j in range(100):
            y_values_g[i, j] = g(np.array([x_values_g[i], x_values_g[j]]))

    fig = plt.figure(figsize=(12, 6))

    ax1 = fig.add_subplot(121)
    ax1.plot(x_values_f, y_values_f, label='f(x)')
    ax1.scatter(trajectory_f, f(trajectory_f), c='red', label='Trajectory')
    ax1.set_title('Gradient Descent for f(x)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.legend()

    ax2 = fig.add_subplot(122, projection='3d')
    X, Y = np.meshgrid(x_values_g, x_values_g)
    Z = y_values_g
    ax2.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax2.scatter(trajectory_g[:, 0], trajectory_g[:, 1],
                g(trajectory_g.T), c='red', label='Trajectory')
    ax2.set_title('Gradient Descent for g(x)')
    ax2.set_xlabel('x1')
    ax2.set_ylabel('x2')
    ax2.legend()

    plt.savefig("answer.pdf")
    plt.show()


if __name__ == "__main__":
    main()
