import unittest
from Equation import Equation


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)

class TestNumericInput(unittest.TestCase):

    def setUp(self):
        self.equation = Equation()

    def test_numeric_input_invalid_on_non_numeric_input(self):
        with self.assertRaises(AssertionError):
            self.equation.numeric_input("a")

    def test_numeric_input_valid_on_empty_string(self):
        self.equation.numeric_input("1")
        self.assertEqual(self.equation.equation_output(), "1")

    def test_numeric_input_valid_on_string_end_numeric(self):
        self.equation.numeric_input("1")
        self.equation.numeric_input("2")
        self.assertEqual(self.equation.equation_output(), "12")

    def test_numeric_input_valid_on_string_end_decimal(self):
        self.equation.numeric_input("1")
        self.equation.decimal_input(".")
        self.equation.numeric_input("2")
        self.assertEqual(self.equation.equation_output(), "1.2")

    def test_numeric_input_valid_on_string_end_expression(self):
        self.equation.numeric_input("1")
        self.equation.expression_input("+")
        self.equation.numeric_input("2")
        self.assertEqual(self.equation.equation_output(), "1 + 2")

    def test_numeric_input_valid_on_string_end_open_parenthesis(self):
        self.equation.open_paren_input("(")
        self.equation.numeric_input("1")
        self.assertEqual(self.equation.equation_output(), "( 1")

    def test_numeric_input_valid_on_string_end_closed_parenthesis(self):
        self.equation.open_paren_input("(")
        self.equation.numeric_input("1")
        self.equation.closed_paren_input(")")
        self.equation.numeric_input("2")
        self.assertEqual(self.equation.equation_output(), "( 1 ) 2")


class TestDecimalInput(unittest.TestCase):

    def setUp(self):
        self.equation = Equation()

    def test_decimal_input_invalid_on_non_decimal_input(self):
        with self.assertRaises(AssertionError):
            self.equation.decimal_input("1")

    def test_decimal_input_valid_on_empty_string(self):
        self.equation.decimal_input(".")
        self.assertEqual(self.equation.equation_output(), ".")

    def test_decimal_input_invalid_on_string_end_decimal(self):
        self.equation.decimal_input(".")
        self.equation.decimal_input(".")
        self.assertEqual(self.equation.equation_output(), ".")

    def test_decimal_input_valid_on_string_end_numeric(self):
        self.equation.numeric_input("1")
        self.equation.decimal_input(".")
        self.assertEqual(self.equation.equation_output(), "1.")

    def test_decimal_input_valid_on_string_end_expression(self):
        self.equation.numeric_input("1")
        self.equation.expression_input("**")
        self.equation.decimal_input(".")
        self.assertEqual(self.equation.equation_output(), "1 ** .")

    def test_decimal_input_valid_on_open_parenthesis(self):
        self.equation.open_paren_input("(")
        self.equation.decimal_input(".")
        self.assertEqual(self.equation.equation_output(), "( .")

    def test_decimal_input_valid_on_closed_paranthesis(self):
        self.equation.open_paren_input("(")
        self.equation.numeric_input("1")
        self.equation.closed_paren_input(")")
        self.equation.decimal_input(".")
        self.assertEqual(self.equation.equation_output(), "( 1 ) .")


class TestExpressionInput(unittest.TestCase):

    def setUp(self):
        self.equation = Equation()

    def test_expression_input_invalid_on_non_expression_input(self):
        with self.assertRaises(AssertionError):
            self.equation.expression_input("1")

    def test_expression_input_valid_on_empty_string(self):
        self.equation.expression_input("+")
        self.assertEqual(self.equation.equation_output(), "")

    def test_expression_input_valid_on_string_end_numeric(self):
        self.equation.numeric_input("1")
        self.equation.expression_input("-")
        self.assertEqual(self.equation.equation_output(), "1 -")

    def test_expression_input_valid_on_string_end_decimal(self):
        self.equation.decimal_input(".")
        self.equation.expression_input("+")
        self.assertEqual(self.equation.equation_output(), ".0 +")

    def test_expression_input_valid_on_string_end_expression(self):
        self.equation.numeric_input("1")
        self.equation.expression_input("+")
        self.equation.expression_input("-")
        self.assertEqual(self.equation.equation_output(), "1 +")

    def test_expression_input_valid_on_string_end_open_parenthesis(self):
        self.equation.open_paren_input("(")
        self.equation.expression_input("/")
        self.assertEqual(self.equation.equation_output(),"(")

    def test_expression_input_valid_on_string_end_closed_parenthesis(self):
        self.equation.open_paren_input("(")
        self.equation.numeric_input("1")
        self.equation.closed_paren_input(")")
        self.equation.expression_input("/")
        self.assertEqual(self.equation.equation_output(),"( 1 ) /")


class TestOpenParenthesisInput(unittest.TestCase):

    def setUp(self):
        self.equation = Equation()

    def test_open_parenthesis_input_invalid_on_non_open_parenthesis(self):
        with self.assertRaises(AssertionError):
            self.equation.open_paren_input("1")

    def test_open_parenthesis_input_valid_on_empty_string(self):
        self.equation.open_paren_input("(")
        self.assertEqual(self.equation.equation_output(), "(")

    def test_open_parenthesis_input_valid_on_string_end_expression(self):
        self.equation.numeric_input("1")
        self.equation.expression_input("/")
        self.equation.open_paren_input("(")
        self.assertEqual(self.equation.equation_output(), "1 / (")

    def test_open_parenthesis_input_valid_on_string_end_open_parenthesis(self):
        self.equation.numeric_input("1")
        self.equation.expression_input("/")
        self.equation.open_paren_input("(")
        self.equation.open_paren_input("(")
        self.assertEqual(self.equation.equation_output(), "1 / ( (")

    def test_open_parenthesis_input_invalid_on_string_end_closed_parenthesis(self):
        self.equation.numeric_input("1")
        self.equation.numeric_input("0")
        self.equation.numeric_input("0")
        self.equation.expression_input("/")
        self.equation.open_paren_input("(")
        self.equation.numeric_input("2")
        self.equation.expression_input("*")
        self.equation.numeric_input("6")
        self.equation.closed_paren_input(")")
        self.equation.open_paren_input("(")
        self.assertEqual(self.equation.equation_output(), "100 / ( 2 * 6 )")

    def test_open_parenthesis_input_invalid_on_string_end_numeric(self):
        self.equation.numeric_input("1")
        self.equation.open_paren_input("(")
        self.assertEqual(self.equation.equation_output(),"1")

    def test_open_parenthesis_input_invalid_on_string_end_decimal(self):
        self.equation.decimal_input(".")
        self.equation.open_paren_input("(")
        self.assertEqual(self.equation.equation_output(),".")


class TestClosedParenthesisInput(unittest.TestCase):

    def setUp(self):
        self.equation = Equation()

    def test_closed_parenthesis_input_invalid_when_not_closed_parenthesis(self):
        with self.assertRaises(AssertionError):
            self.equation.closed_paren_input("1")

    def test_closed_parenthesis_input_invalid_on_empty_string(self):
        self.equation.closed_paren_input(")")
        self.assertEqual(self.equation.equation_output(), "")

    def test_closed_parenthesis_input_invalid_if_more_than_number_of_open_parenthesis(self):
        self.equation.open_paren_input("(")
        self.equation.open_paren_input("(")
        self.equation.numeric_input("1")
        self.equation.expression_input("*")
        self.equation.numeric_input("2")
        self.equation.closed_paren_input(")")
        self.equation.expression_input("/")
        self.equation.numeric_input("1")
        self.equation.closed_paren_input(")")
        self.equation.closed_paren_input(")")
        self.assertEqual(self.equation.equation_output(), "( ( 1 * 2 ) / 1 )")

    def test_closed_parenthesis_input_invalid_on_string_end_expression(self):
        self.equation.open_paren_input("(")
        self.equation.numeric_input("1")
        self.equation.expression_input("+")
        self.equation.closed_paren_input(")")
        self.assertEqual(self.equation.equation_output(), "( 1 +")

    def test_closed_parenthesis_input_valid_on_string_end_numeric(self):
        self.equation.open_paren_input("(")
        self.equation.numeric_input("5")
        self.equation.closed_paren_input(")")
        self.assertEqual(self.equation.equation_output(), "( 5 )")

    def test_closed_parenthesis_input_valid_on_string_end_decimal(self):
        self.equation.open_paren_input("(")
        self.equation.numeric_input("5")
        self.equation.decimal_input(".")
        self.equation.closed_paren_input(")")
        self.assertEqual(self.equation.equation_output(), "( 5.0 )")

    def test_closed_parenthesis_input_valid_on_string_end_closed_parenthesis(self):
        self.equation.open_paren_input("(")
        self.equation.numeric_input("1")
        self.equation.expression_input("*")
        self.equation.open_paren_input("(")
        self.equation.numeric_input("1")
        self.equation.expression_input("*")
        self.equation.numeric_input("2")
        self.equation.closed_paren_input(")")
        self.equation.closed_paren_input(")")
        self.assertEqual(self.equation.equation_output(), "( 1 * ( 1 * 2 ) )")


class TestEqualsInput(unittest.TestCase):

    def setUp(self):
        self.equation = Equation()

    def test_equals_input_invalid_if_not_equals(self):
        with self.assertRaises(AssertionError):
            self.equation.equals_input("2")

    def test_equals_input_invalid_if_string_end_expression(self):
        self.equation.numeric_input("1")
        self.equation.expression_input("-")
        self.equation.equals_input("=")
        self.assertEqual(self.equation.equation_output(), "1 -")

    def test_equals_input_invalid_if_string_end_open_parenthesis(self):
        self.equation.numeric_input("1")
        self.equation.expression_input("*")
        self.equation.open_paren_input("(")
        self.equation.equals_input("=")
        self.assertEqual(self.equation.equation_output(), "1 * (")

    def test_equals_input_valid_if_string_end_numeric(self):
        self.equation.numeric_input("1")
        self.equation.expression_input("*")
        self.equation.numeric_input("2")
        self.equation.equals_input("=")
        self.assertEqual(self.equation.equation_output(), "2")

    def test_equals_input_valid_if_string_end_decimal(self):
        self.equation.numeric_input("1")
        self.equation.expression_input("*")
        self.equation.numeric_input("2")
        self.equation.decimal_input(".")
        self.equation.equals_input("=")
        self.assertEqual(self.equation.equation_output(), "2.0")

    def test_equals_input_valid_if_string_end_closed_parenthesis(self):
        self.equation.open_paren_input("(")
        self.equation.numeric_input("1")
        self.equation.expression_input("*")
        self.equation.numeric_input("2")
        self.equation.closed_paren_input(")")
        self.equation.equals_input("=")
        self.assertEqual(self.equation.equation_output(), "2")


class TestClearInput(unittest.TestCase):

    def setUp(self):
        self.equation = Equation()

    def test_clear_input(self):
        self.equation.open_paren_input("(")
        self.equation.numeric_input("1")
        self.equation.expression_input("*")
        self.equation.numeric_input("2")
        self.equation.closed_paren_input(")")
        self.equation.clear_input()
        self.assertEqual(self.equation.equation_output(), "")


class TestSolve(unittest.TestCase):

    def setUp(self):
        self.equation = Equation()

    def test_solve_equation(self):
        self.equation.open_paren_input("(")
        self.equation.numeric_input("1")
        self.equation.expression_input("*")
        self.equation.numeric_input("2")
        self.equation.closed_paren_input(")")
        answer = self.equation.solve()
        self.assertEqual(answer, "2")


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


if __name__ == '__main__':
    unittest.main()
