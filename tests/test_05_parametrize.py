import pytest
from source.arithmetic import add


# This is for running the same basic test
# with a bunch of different values


def describe_multitest():
    @pytest.mark.parametrize(
        "augend",
        [1, 2, 3, 4, 10, 100, 0, -1],
    )
    def add_to_negative_self_is_zero(augend):
        # The arguments to the unit test is supplied by the wrapper
        assert 0 == augend + -augend

    @pytest.mark.parametrize(
        "augend,append,sum",
        [
            (1, 1, 2),
            (1, 2, 3),
            (5, 5, 10),
        ],
    )
    def add_numbers(augend, append, sum):
        # You can supply multiple arguments at a time using tuples
        assert sum == add(augend, append)
