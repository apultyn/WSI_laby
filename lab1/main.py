import numpy as np
from gradient import Gradient
import matplotlib.pyplot as plt


def f(x):
    return (x**4) / 4


def g(x):
    return (1.5 - np.exp(-x[0]**2 - x[1]**2) - 0.5 *
            np.exp(-((x[0] - 1)**2) - ((x[1] + 2)**2)))


def gradient_f(x):
    return x**3


def gradient_g(x):
    return np.array([
        2 * x[0] * np.exp(-x[0]**2 - x[1]**2) + (x[0] - 1) *
        np.exp(-((x[0] - 1)**2) - ((x[1] + 2)**2)),
        2 * x[1] * np.exp(-x[0]**2 - x[1]**2) + (x[1] + 2) *
        np.exp(-((x[0] - 1)**2) - ((x[1] + 2)**2))
    ])


def main():
    first = Gradient(f, gradient_f, 0.5, 0.1, 0.001)
    trajectory_f = first.solve(3.0)

    x_values_f = np.linspace(-4, 4, 100)
    y_values_f = f(x_values_f)

    fig = plt.figure(figsize=(12, 6))

    ax1 = fig.add_subplot(121)
    ax1.plot(x_values_f, y_values_f, label='f(x)')
    ax1.scatter(trajectory_f, f(trajectory_f), c='red', label='Trajectory')
    ax1.set_title('Gradient Descent for f(x)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('f(x)')
    ax1.legend()
    plt.savefig("answer.pdf")


if __name__ == "__main__":
    main()
