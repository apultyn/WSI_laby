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
                     np.exp(-((x[0] - 1)**2) - ((x[1] + 2)**2))])


def plot_2D(function, trajectory, x_values, title):
    y_values = function(x_values)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(x_values, y_values, label='f(x)')
    ax.scatter(trajectory, function(trajectory), c='red', label='Trajectory')
    ax.set_title(title)
    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')
    ax.legend()

    plt.show()


def plot_3D(function, trajectory, x_values, title):
    y_values = np.zeros((len(x_values), len(x_values)))

    for i in range(len(x_values)):
        for j in range(len(x_values)):
            y_values[i, j] = function(np.array([x_values[i], x_values[j]]))

    fig = plt.figure(figsize=(12, 6))
    ax = fig.add_subplot(111, projection='3d')
    X, Y = np.meshgrid(x_values, x_values)
    Z = y_values
    ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
    ax.scatter(trajectory[:, 0], trajectory[:, 1], function(trajectory.T),
               c='red', label='Trajectory')
    ax.set_title(title)
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.legend()

    plt.show()


def main():
    func_f = Gradient_descent(f, gradient_f, 1, 0.1, 0.001)
    trajectory_f = func_f.solve(np.array([-2.5]))
    x_values_f = np.linspace(-4, 4, 100)
    plot_2D(f, trajectory_f, x_values_f, 'Gradient Descent for f(x)')

    func_g = Gradient_descent(g, gradient_g, 0.5, 0.1, 0.001)
    trajectory_g = func_g.solve(np.array([-1.5, 2]))
    x_values_g = np.linspace(-4, 4, 100)
    plot_3D(g, trajectory_g, x_values_g, 'Gradient Descent for g(x)')


if __name__ == "__main__":
    main()
