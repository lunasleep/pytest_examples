import random

from source.polynomial import random_polynomial


def describe_random_polynomial():
    def picks_random_degree(mocker):  # The "mocker" fixture is already defined
        mock_randomint = mocker.patch.object(random, "randint")
        # This will replace random.randint for the duration of the test
        mock_randomint.return_value = 7  # You can set the return value

        mock_randomint.assert_not_called()

        polynomial = random_polynomial()
        assert 7 == polynomial.degree

        mock_randomint.assert_called_once_with(1, 10)

    def picks_random_values(mocker):
        mock_randomint = mocker.patch.object(random, "randint")
        mock_randomint.return_value = 2

        mock_random = mocker.patch.object(random, "random")
        mock_random.side_effect = [0.1, 0.2, 0.3]   # .side_effect can define a sequence of return values

        polynomial = random_polynomial()
        assert "0.3x^2 + 0.2x + 0.1" == str(polynomial)

    def can_cope_with_exceptions(mocker):
        mock_randomint = mocker.patch.object(random, "randint")
        mock_randomint.side_effect = ValueError("Fake valueerror")

        polynomial = random_polynomial()

        assert 5 == polynomial.degree
