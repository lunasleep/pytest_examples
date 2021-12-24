import random
import time


def random_polynomial():
    new_polynomial = Polynomial()
    try:
        degree = random.randint(1, 10)
    except ValueError:
        degree = 5

    for _ in range(degree + 1):
        new_polynomial._coefficients.append(random.random())

    new_polynomial._truncate()
    return new_polynomial


def wait_10s_then_create_random_polynomial():
    # For some reason, imagine we need this in production
    time.sleep(10)
    return random_polynomial()


class Polynomial:
    def __init__(self, coefficients=None):
        if coefficients is None:
            coefficients = []
        self._coefficients = coefficients
        self._coefficients.reverse()
        self._truncate()

    def copy(self):
        new_polynomial = Polynomial()
        new_polynomial._coefficients = self._coefficients * 1
        return new_polynomial

    def _truncate(self):
        while len(self._coefficients) > 0 and self._coefficients[-1] == 0:
            self._coefficients = self._coefficients[:-1]

    def evaluate(self, x):
        sum = 0
        for i in range(len(self._coefficients)):
            sum += self._coefficients[-i] * (x ** i)
        return sum

    @property    
    def degree(self):
        return len(self._coefficients) - 1 if len(self._coefficients) > 0 else 0

    def __add__(self, other_polynomail):
        new_polynomial = self.copy()
        print(new_polynomial._coefficients)
        print(other_polynomail._coefficients)
        for i in range(max(len(new_polynomial._coefficients), len(other_polynomail._coefficients))):
            if i >= len(other_polynomail._coefficients):
                break
            if i >= len(new_polynomial._coefficients):
                new_polynomial._coefficients.append(0)
            new_polynomial._coefficients[i] += other_polynomail._coefficients[i]
        return new_polynomial

    def __mul__(self, other_polynomial):
        new_coefficients = [0] * (self.degree + other_polynomial.degree)
        for i in range(len(self._coefficients)):
            for j in range(len(other_polynomial._coefficients)):
                new_coefficients[i + j] += self._coefficients[i] * other_polynomial._coefficients[j]

    def __repr__(self):
        if len(self._coefficients) == 0:
            return "0"
        repr = []
        for i in range(len(self._coefficients)):
            if self._coefficients[i] == 0:
                continue
            c = str(abs(self._coefficients[i])) if self._coefficients[i] != 1 else ""
            operand = "+" if self._coefficients[i] > 0 else "-"
            variable = "x" if i > 0 else ""
            exp = f"^{i}" if i > 1 else ""
            new_term = f"{operand} {c}{variable}{exp}"
            repr.append(new_term)
        repr.reverse()
        return(" ".join(repr)[2:])

    def __eq__(self, other_polynomial):
        return (
            isinstance(other_polynomial, Polynomial)
            and self._coefficients == other_polynomial._coefficients
        )