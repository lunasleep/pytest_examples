import random
import time

from source.polynomial import wait_10s_then_create_random_polynomial


#Sometimes you want some fixtures across multiple tests.

# Before any tests are run, pytest will first try to find a file
# called "conftest.py" and import it.
 
# Pytest will start by looking in the directory where
# the tests are defined, and then search parent directories
# until it finally reaches the directory where you ran pytest from


def describe_slow_random_polynomial():
    def picks_random_degree():
        # wait_10s_then_create_random_polynomial calls time.sleep(10)
        # However, we never want our tests to actually sleep. We never
        # want tests to be slower.

        # So, in conftest.py, we have an autouse fixture that mocks
        # time.sleep

        before = time.time()
        wait_10s_then_create_random_polynomial()
        after = time.time()
        assert after - before < 1