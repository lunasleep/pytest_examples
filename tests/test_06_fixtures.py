import pytest
from source.polynomial import Polynomial


@pytest.fixture  # This wrapper turns a function into a fixture
def quadratic():
    return Polynomial([2, 3, 4])


@pytest.fixture
def cubic():
    return Polynomial([2, -2, 4, 5])


def describe_Polynomial():
    @pytest.fixture  # Fixtures can also be scoped to within describe blocks
    def zero():
        return Polynomial([])

    def qudratic_degree(quadratic):
        # When a unit test takes an argument, pytest checks for fixtures with that name
        # If it finds one, it will call that fixture and pass its return value into
        # the unit test.
        assert 2 == quadratic.degree

    def cubic_degree(cubic):
        assert 3 == cubic.degree

    def constand_degree():
        assert 0 == Polynomial([2]).degree

    def zero_degree(zero):
        assert 0 == zero.degree

    def repr(quadratic):
        print(quadratic._coefficients)
        assert "2x^2 + 3x + 4" == str(quadratic)

    def repr_zero(zero):
        assert 0 == len(zero._coefficients)
        assert "0" == str(zero)

    def add_polynomials(quadratic, cubic):
        assert "2x^3 + 7x + 9" == str(quadratic + cubic)


    @pytest.mark.parametrize("degree1,degree2",
        [
            (1, 1),
            (1, 2),
            (6, 1),
            (4, 3),
        ],
    )
    def preserve_highest_degree(degree1, quadratic, degree2):
        deg1poly = Polynomial([3] * (degree1 + 1))
        assert deg1poly.degree  == degree1

        deg2poly = Polynomial([2] * (degree2 + 1))
        assert deg2poly.degree  == degree2

        assert (deg1poly + deg2poly + quadratic).degree == max(deg1poly.degree, deg2poly.degree, 2)
        # You can mix fixtures and parametrize, in any order
