from cmath import sqrt
from abc import ABC, abstractmethod

class DiscriminantStrategy(ABC):
    @abstractmethod
    def calculate_discriminant(self, a, b, c):
        pass


class OrdinaryDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        return b ** 2 - 4 * a * c


class RealDiscriminantStrategy(DiscriminantStrategy):
    def calculate_discriminant(self, a, b, c):
        discriminant = b ** 2 - 4 * a * c
        return discriminant if discriminant >= 0 else float('nan')


class QuadraticEquationSolver:
    def __init__(self, strategy):
        self.strategy = strategy


    def solve(self, a, b, c):
        d = self.strategy.calculate_discriminant(a, b, c)
        root_d = sqrt(d)
        sol1 = (-b + root_d) / (2 * a)
        sol2 = (-b - root_d) / (2 * a)
        return sol1, sol2

solver = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
print(solver.solve(1, 10, 16))

solver = QuadraticEquationSolver(RealDiscriminantStrategy())
print(solver.solve(1, 4, 5))

solver = QuadraticEquationSolver(OrdinaryDiscriminantStrategy())
print(solver.solve(1, 4, 5))