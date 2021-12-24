import random

import pytest

from source.polynomial import random_polynomial


# Sometimes, you want to make sure a fixture is run even
# when a test doesns't call for it. This is commonly used
# to make sure tests don't do anything random, talk to
# external services, or access the system clock (which is
# effectively another RNG to a unit test)


@pytest.fixture(autouse=True)
def mock_randomint(mocker):
    mock_randomint = mocker.patch.object(random, "randint")
    mock_randomint.return_value = 4
    return mock_randomint


def describe_random_polynomial():
    def picks_random_degree():  # mock_randomint isn't requested, but happens anyway
        polynomial = random_polynomial()
        assert 4 == polynomial.degree
