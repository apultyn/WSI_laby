import numpy as np
from solver import Solver


class Gradient_descent(Solver):
    def __init__(self, func, gradient, starting_step,
                 decrease_coefficient, precision):
        self._function = func
        self._gradient = gradient
        self._starting_step = starting_step
        self._decrease_coefficient = decrease_coefficient
        self._precision = precision

    def get_parameters(self):
        return {
            "Function": self._function,
            "Gradient": self._gradient,
            "Starting step": self._starting_step,
            "Decrease coefficient": self._decrease_coefficient,
            "Precision": self._precision
        }

    def solve(self, initial_point):
        trajectory = [initial_point]
        current_point = np.array(initial_point)
        step = self._starting_step

        gradients = np.array(self._gradient(current_point))
        precision_achieved = True

        for value in gradients:
            if np.fabs(value) > self._precision:
                precision_achieved = False
                break

        while not precision_achieved:
            new_current_point = (current_point - step *
                                 self._gradient(current_point))
            if self._function(new_current_point) >= self._function(current_point):
                step *= self._decrease_coefficient
            else:
                current_point = new_current_point
                trajectory.append(current_point)

                for value in self._gradient(current_point):
                    if np.fabs(value) > self._precision:
                        break
                    precision_achieved = True

        return np.array(trajectory)
