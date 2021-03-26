import re

class Equation:
    """A class that creates, holds, and parses an equation to produce a result"""
    def __init__(self):
        self.equation = ""

    def __repr__(self):
        return self.equation

    def equation_input(self, equation):
        """This method only exists to run tests on self.validate_equation()"""
        self.equation = equation

    def equation_output(self):
        """This method is used to output the equation to the screen"""
        return self.equation

    def numeric_input(self, num_input):
        """Handles numeric input"""
        if num_input not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            raise AssertionError("Numeric Input is not an number.")
        elif self.equation == "":
            self.equation += str(num_input)
        elif self.equation.endswith(("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".")):
            self.equation += str(num_input)
        elif self.equation.endswith(("+", "-", "*", "/", "(", ")", "**")):
            self.equation += (" " + str(num_input))
        else:
            print("Invalid Input")

    def decimal_input(self, dec_input):
        """Handles decimal input"""
        if dec_input != ".":
            raise AssertionError("Decimal Input is not a decimal")
        elif self.equation == "":
            self.equation += str(dec_input)
        elif str(dec_input) in self.equation.split(' ')[-1]:
            print("Invalid Input")
        elif self.equation.endswith(("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")):
            self.equation += str(dec_input)
        elif self.equation.endswith(("+", "-", "*", "/", "(", ")", "**")):
            self.equation += (" " + str(dec_input))
        else:
            print("Invalid Input")

    def expression_input(self, exp_input):
        """Handles expression input"""
        if exp_input not in ['+', '-', '*', '/', '**']:
            raise AssertionError("Expression Input is not a valid expression")
        elif self.equation == "":
            print("Equation must start with a number, decimal, or open parenthesis")
        elif self.equation.endswith(("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ")")):
            self.equation += (" " + str(exp_input))
        elif self.equation.endswith('.'):
            self.equation += ("0 " + str(exp_input))
        elif self.equation.endswith(("+", "-", "*", "/", "(", "**")):
            print("Invalid Input")
        else:
            print("Invalid Input")

    def open_paren_input(self, op_input):
        """Handles the open parenthesis input"""
        if op_input != "(":
            raise AssertionError("Open Parenthesis input is not a OpenParenthesis")
        elif self.equation == "":
            self.equation += "("
        elif self.equation.endswith(('+', '-', '*', '/', '**', '(')):
            self.equation += (" " + str(op_input))
        elif self.equation.endswith(("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".")):
            print("Invalid Input")

    def closed_paren_input(self, cp_input):
        """Handles the closed parenthesis input"""
        if cp_input != ")":
            raise AssertionError("Closed Parenthesis input is not a Closed Parenthesis")
        elif self.equation == "":
            print("Equation must start with a number, decimal, or open parenthesis")
        elif (self.equation.count(')')+1) > self.equation.count('('):
            print("Invalid Input - Can't add more closed parenthesis than there are open parenthesis")
        elif self.equation.endswith(('+', '-', '*', '/', '**')):
            print("Invalid Input")
        elif self.equation.endswith(("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ')')):
            self.equation += (" " + str(cp_input))

    def equals_input(self, equals_input):
        """Handles the equals input"""
        if equals_input != '=':
            raise AssertionError("Equals Input is not an equals sign")
        elif self.equation.endswith(("+", "-", "*", "/", "(", "**")):
            print("The equation is not in a valid form: Syntax Error")
        else:
            self.equation = self.validate_equation()

    def clear_input(self):
        """Handles the "clear" input and clears all the input"""
        self.equation = ""

    def solve(self):
        """Solves the equation and returns the answer"""
        answer = eval(self.equation)
        return str(answer)

    def validate_equation(self):
        """Validate if the equation is valid"""
        # Check if all open parenthesis are closed
        open_parens = self.equation.count('(')
        closed_parens = self.equation.count(')')
        if open_parens != closed_parens:
            print("The equation is not in a valid form: Parenthesis Problem")
            return self.equation

        # Check the rest of the syntax and solve the equation if it's valid
        valid_result = re.fullmatch(
            r'((\(\s)*([0-9]*\s|\.[0-9]*\s|[0-9]*\.[0-9]*\s|\.[0-9]*\s)'
            r'((\+|\-|\*|\/|\**)\s)'
            r'([0-9]*\s?|\.[0-9]*\s?|[0-9]*\.[0-9]*\s?|\.[0-9]*\s?)(\s\))*?'
            r'((\+|\-|\*|\/|\**)\s)?)+', self.equation
        )
        if isinstance(valid_result, type(None)):
            print("The equation is not in a valid form: Syntax Error")
        if isinstance(valid_result, re.Match):
            try:
                return self.solve()
            except SyntaxError:
                print("The equation is not in a valid form: Missed Test Case")
