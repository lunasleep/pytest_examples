from source.arithmetic import add, multiply

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
        def describe_multiply():
            def two_numbers():
                assert 3 == multiply(3, 1)

            def two_other_numbers():
                assert 90 == multiply(10, 9)

        def describe_divide():
            def two_numbers():
                assert 3000 == multiply(30, 10)

            def two_other_numbers():
                assert 40 == multiply(10, 4)
