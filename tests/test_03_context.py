from source.arithmetic import add, subtract

# 'context' is a synonym for 'describe'

def describe_arithmetic():
    def context_value_increasing_functions():
        def describe_add():
            def two_numbers():
                assert 3 == add(1, 2)
            
            def two_other_numbers():
                assert 12 == add(2, 10)

        def describe_multiply():
            def two_numbers():
                assert 2 == add(1, 2)
            
            def two_other_numbers():
                assert 20 == add(2, 10)

    def context_value_decreasing_functions():
        def describe_subtract():
            def two_numbers():
                assert 2 == subtract(3, 1)

            def two_other_numbers():
                assert 1 == subtract(10, 9)

        def describe_divide():
            def two_numbers():
                assert 3 == subtract(30, 10)

            def two_other_numbers():
                assert 2.5 == subtract(10, 4)
