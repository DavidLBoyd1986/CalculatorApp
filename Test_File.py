from Equation import Equation
import re

# Test Cases that should pass
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
equation_twenty_three = "( 5 + ( 14 - 10 ))"
equation_twenty_four = "3.88 * 9"

# Test Cases that should fail
failed_equation_one = "( 5 + 6"
failed_equation_two = "5.5.5 - 6"
failed_equation_three = "99 - 9 )"
failed_equation_four = "5 * 4 4"
failed_equation_five = "7 * + 5"
failed_equation_six = "8 ( 2 * 3 )"
failed_equation_seven = "( 9 + 2 - 8 ) - 3 ( 23 + 5 )"
failed_equation_eight = ".5. + 3"
failed_equation_nine = "4.. - 2"
failed_equation_ten = "4.2 + 3.3."

equation_list = [equation, equation_two, equation_three, equation_four, equation_five,
                 equation_six, equation_seven, equation_eight, equation_nine, equation_ten,
                 equation_eleven, equation_twelve, equation_thirteen, equation_fourteen, equation_fifteen,
                 equation_sixteen, equation_seventeen, equation_eighteen, equation_nineteen, equation_twenty,
                 equation_twenty_one, equation_twenty_two, equation_twenty_three, equation_twenty_four]

failed_equation_list = [failed_equation_one, failed_equation_two, failed_equation_three, failed_equation_four,
                        failed_equation_five, failed_equation_six, failed_equation_seven, failed_equation_eight,
                        failed_equation_nine, failed_equation_ten]

print("These test cases should pass...")
for eq in equation_list:
    valid_result = re.fullmatch(
        r'((\(\s)*([0-9]*\s|\.[0-9]*\s|[0-9]*\.[0-9]*\s|\.[0-9]*\s)'
        r'((\+|\-|\*|\/|\**)\s)'
        r'([0-9]*\s?|\.[0-9]*\s?|[0-9]*\.[0-9]*\s?|\.[0-9]*\s?)(\s\)*)?'
        r'((\+|\-|\*|\/|\**)\s)?)+', str(eq)
    )
    if isinstance(valid_result, type(None)):
        print(str(eq) + ' : test failed : ' + str(valid_result))
    if isinstance(valid_result, re.Match):
        print(str(eq) + ' : test passed : ' + str(valid_result))


print("These test cases should fail...")
for eq in failed_equation_list:
    valid_result = re.fullmatch(
        r'((\(\s)*([0-9]*\s|\.[0-9]*\s|[0-9]*\.[0-9]*\s|\.[0-9]*\s)'
        r'((\+|\-|\*|\/|\**)\s)'
        r'([0-9]*\s?|\.[0-9]*\s?|[0-9]*\.[0-9]*\s?|\.[0-9]*\s?)(\s\)*)?'
        r'((\+|\-|\*|\/|\**)\s)?)+', str(eq)
    )
    if type(valid_result) is type(None):
        print(str(eq) + ' : test failed : ' + str(valid_result))
    if type(valid_result) is re.Match:
        print(str(eq) + ' : test passed : ' + str(valid_result))


test_equation = Equation()
test_equation.numeric_input('5')
print(test_equation)