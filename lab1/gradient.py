import numpy as np
from solver import Solver


class Gradient(Solver):
    def __init__(self, function, gradient, starting_step,
                 decrease_coefficient, precision):
        super().__init__()
        self._function = function
        self._gradient = gradient
        self._starting_step = starting_step
        self._decrease_coefficient = decrease_coefficient
        self._precision = precision

    def get_parameters(self):
        return {
            "Function": self._function,
            "Starting step": self._starting_step,
            "Decrease coefficient": self._decrease_coefficient,
            "Precision": self._precision
        }

    def solve(self, initial_point):
        trajectory = [initial_point]
        current_point = initial_point
        step = self._starting_step

        while np.fabs(self._gradient(current_point)) > self._precision:
            new_current_point = current_point - step * self._gradient(current_point)
            if self._function(new_current_point) >= self._function(current_point):
                step *= self._decrease_coefficient
            else:
                current_point = new_current_point
                trajectory.append(current_point)

        return np.array(trajectory)
