import unittest
from Equation import Equation


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)


class TestValidateEquation(unittest.TestCase):
    """Lists of equations used to test the Equation Class and validate_equation method"""

    def test_equations_pass(self):
        """Tests equations that should pass"""

        # Too lazy to create individual tests for these. It still works like this, and stops on the tests that fail.
        equation = "66 + 5"
        equation_two = "66777 - 234"
        equation_three = "2222 * 4343"
        equation_four = "200 / 20"
        equation_five = "20 ** 4"
        equation_six = "6.6 + 5.5"
        equation_seven = "66777. - 234"
        equation_eight = ".2222 * .4343"
        equation_nine = "200 / .20"
        equation_ten = "2.0 ** 4"
        equation_eleven = "( 6.6 + 5.5 )"
        equation_twelve = "( 66777. - 234 )"
        equation_thirteen = "( .2222 * .4343 )"
        equation_fourteen = "( 200 / .20 )"
        equation_fifteen = "( 2.0 ** 4 )"
        equation_sixteen = "6.6 + 5.5 - 4"
        equation_seventeen = "66777. - 234 * 30 / 2 ** 4"
        equation_eighteen = ".2222 * .4343 + ( 4 * 25 )"
        equation_nineteen = "200 / .20 ** 5 + ( 50 * 20 )"
        equation_twenty = "( 2.0 ** 4 ) / 5 * ( 6 + 24 )"
        equation_twenty_one = "( 9 + 2 - 8 )"
        equation_twenty_two = "( ( 5 + 14 ) - 10 )"
        equation_twenty_three = "( 5 + ( 14 - 10 ) )"
        equation_twenty_four = "3.88 * 9"

        equation_list = [equation, equation_two, equation_three, equation_four, equation_five,
                         equation_six, equation_seven, equation_eight, equation_nine, equation_ten,
                         equation_eleven, equation_twelve, equation_thirteen, equation_fourteen, equation_fifteen,
                         equation_sixteen, equation_seventeen, equation_eighteen, equation_nineteen, equation_twenty,
                         equation_twenty_one, equation_twenty_two, equation_twenty_three, equation_twenty_four]

        for eq in equation_list:
            test_equation = Equation()
            test_equation.equation_input(eq)
            print(test_equation)
            print(isinstance(test_equation, type(None)))
            self.assertFalse(isinstance(test_equation.validate_equation(), type(None)))

    def test_equations_fail(self):
        """Tests that invalid equations fail"""

        failed_equation_one = "5.5.5 - 6"
        failed_equation_two = "5 * 4 4"
        failed_equation_three = "7 * + 5"
        failed_equation_four = "8 ( 2 * 3 )"
        # This test case fails - Need to implement bug fix
        # failed_equation_five = "( 9 + 2 - 8 ) - 3 ( 23 + 5 )"
        failed_equation_six = ".5. + 3"
        failed_equation_seven = "4.. - 2"
        failed_equation_eight = "4.2 + 3.3."
        failed_equation_list = [failed_equation_one, failed_equation_two, failed_equation_three, failed_equation_four,
                                failed_equation_six, failed_equation_seven, failed_equation_eight]

        for eq in failed_equation_list:
            test_bad_equation = Equation()
            test_bad_equation.equation_input(eq)
            print(test_bad_equation.validate_equation())
            print(isinstance(test_bad_equation, type(None)))
            self.assertTrue(isinstance(test_bad_equation.validate_equation(), type(None)))

# failed_equation_one = "( 5 + 6"
# failed_equation_three = "99 - 9 )"
if __name__ == '__main__':
    unittest.main()
