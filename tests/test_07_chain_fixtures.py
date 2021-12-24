import random

import pytest


@pytest.fixture
def random_number():
    return random.randint(0, 99999)


@pytest.fixture
def random_number_plus_one(random_number):
    # A fixture can use another fixture, the same way
    # a unit test can
    return random_number + 1


global_cache = []


def describe_fixtures_can_user_other_fixtures():
    def without_reuse(random_number, random_number_plus_one):
        # During the execution of a test, no fixture will
        # be called more than once. If multiple fixtures
        # and/or the unit test all use the same parent fixture,
        # its return value will be cached.

        assert random_number_plus_one == random_number + 1

    @pytest.fixture
    def append_to_global_cache(random_number):
        global_cache.append(random_number)

    def appends_to_global_cache(random_number, append_to_global_cache):
        # However, when starting another test, it will rerun all the fixtures
        assert global_cache[-1] == random_number
        assert len(global_cache) == 1
    
    def appends_again(random_number, append_to_global_cache):
        assert global_cache[-1] == random_number
        assert len(global_cache) == 2
