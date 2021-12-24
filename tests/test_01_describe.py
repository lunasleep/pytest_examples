from source.arithmetic import add, multiply


def describe_add():
    # A function named "def describe_*" starts a "describe block."
    # Any functions defined within are run as unit tests. They do
    # not need to be named "test_*" or "*_test" to be tests. This
    # helps you write long, descritive test names.
    # Try making some of them fail to see how they work.
    def two_numbers():
        assert 3 == add(1, 2)
    
    def two_other_numbers():
        assert 12 == add(2, 10)


def describe_multiply():
    def two_numbers():
        assert 3 == multiply(3, 1)

    def two_other_numbers():
        # Generally, assertions should be (expected, actual) vs
        # the seemingly more natural (actual, expected). This is
        # because you know how long the string representation of
        # the expected value will be when it's printed to the log,
        # but in the case of a failure, the actual value might
        # be printed to the log as a giant mountain of text, making
        # it hard to find the expected value
        assert 90 == multiply(10, 9)
