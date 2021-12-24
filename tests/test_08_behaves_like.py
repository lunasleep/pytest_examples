import pytest
import pytest_describe

from source.arithmetic import add, multiply
from source.polynomial import Polynomial


def a_commutative_operation():
    # This top-level function is not a describe block.
    # That means the functions in it will not be run as tests.
    @pytest.mark.parametrize(
        "int1,int2",
        [
            (0, 1),
            (1, 10),
            (1, -1),
            (1, 10000000),
            (0, 10000000),
            (-10000000, 10000000),
        ]
    )
    def with_integers(int1, int2, operation):
        assert operation(int1, int2) == operation(int2, int1)

    @pytest.mark.parametrize(
        "float1,float2",
        [
            (0, 1.3),
            (1, 10.5),
            (13.8, -1.4),
            (1, 1.4e100),
            (0.25, 1e100),
            (1e-100, 1e100),
        ]
    )
    def with_floats(float1, float2, operation):
        assert operation(float1, float2) == operation(float2, float1)

    @pytest.mark.parametrize(
        "poly1,poly2",
        [
            (Polynomial(), Polynomial([1])),
            (Polynomial([1, 2, 3]), Polynomial([5, 5, 5])),
            (Polynomial(list(range(100))), Polynomial([1])),
            (Polynomial(list(range(100))), Polynomial(list(range(100)))),
        ]
    )
    def with_floats(poly1, poly2, operation):
        assert operation(poly1, poly2) == operation(poly2, poly1)

def an_associative_operation():
    @pytest.mark.parametrize(
        "int1,int2,int3",
        [
            (0, 1, 2),
            (0, 0, 0),
            (1, 10, 100),
            (1, -1, -100),
            (1, 10000000, -50),
            (0, 10000000, -80),
            (-10000000, 10000000, 0),
        ]
    )
    def with_integers(int1, int2, int3, operation):
        assert operation(int1, operation(int2, int3)) == operation(operation(int1, int2), int3)

    @pytest.mark.parametrize(
        "float1,float2,float3",
        [
            (0, 1.3, 1.1),
            (0., 0., 0.),
            (1, 10.5, 111.111),
            (13.8, -1.4, -9999.9999),
            (1, 1.4e100, 0),
            (0.25, 1e100, 0),
            (1e-100, 1e100, 0),
        ]
    )
    def with_floats(float1, float2, float3, operation):
        assert operation(float1, operation(float2, float3)) == operation(operation(float1, float2), float3)

    @pytest.mark.parametrize(
        "poly1,poly2,poly3",
        [
            (Polynomial(), Polynomial([1]), Polynomial([1, 2, 3])),
            (Polynomial([1, 2, 3]), Polynomial([5, 5, 5]), Polynomial([1])),
            (Polynomial(list(range(100))), Polynomial([1]), Polynomial()),
            (Polynomial(list(range(100))), Polynomial(list(range(100))), Polynomial()),
        ]
    )
    def with_polynomials(poly1, poly2, poly3, operation):
        assert operation(poly1, operation(poly2, poly3)) == operation(operation(poly1, poly2), poly3)

@pytest_describe.behaves_like(a_commutative_operation)
@pytest_describe.behaves_like(an_associative_operation)
def describe_multiplication():
    # However, you can use the @pytest.behaves_like() wrapper
    # It will "import" all the tests and fixtures in a top-level block
    # and append them to the current block.
    # They will then use whatever fixtures are defined in the current block.
    @pytest.fixture
    def operation():
        return multiply

@pytest_describe.behaves_like(a_commutative_operation)
@pytest_describe.behaves_like(an_associative_operation)
def describe_multiplication():
    @pytest.fixture
    def operation():
        return add

