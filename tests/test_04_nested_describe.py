from source.arithmetic import add, subtract


def describe_arithmetic():
    def describe_add():
        # You can nest "describe" blocks. A "def describe_" function
        # inside another "def describe_" function is the exception
        # to the rule that any function in a describe block is
        # a unit test.
        def two_numbers():
            assert 3 == add(1, 2)
        
        def two_other_numbers():
            assert 12 == add(2, 10)

    def describe_subtract():
        def two_numbers():
            assert 2 == subtract(3, 1)

        def two_other_numbers():
            assert 1 == subtract(10, 9)
