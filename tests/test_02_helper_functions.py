from source.arithmetic import add, multiply


def repeated_addition(x, y):
    # This is a function defined outside a describe block.
    # Pytest will ignore it, making it just a regular function.
    # This is a basic way to provide re-usable helpers functions.
    sum = 0
    for _ in range(y):
        sum += x
    return sum


def describe_multiplication():
    def _also_not_a_test():
        # This function will also be ignored by pytest, even
        # though it's within a describe block, because it has
        # a leading underscore.
        assert False

    def is_repeated_addition():
        assert repeated_addition(6, 7) == multiply(6, 7)
