# James Shaw
# CSCI151
# 1/18/22
# compound.py

import sys
import stdio
import math

args = sys.argv[1:]
if len(args) < 3:
    year_arg = int(input("Input years to compound: "))
    principal_arg = int(input("Input starting value: "))
    int_rate_arg = float(input("Input interest rate as decimal (4% = 0.04): "))
else:
    year_arg = int(args[0])
    principal_arg = int(args[1])
    int_rate_arg = float(args[2])


def compound_interest(years: int, principal: int, rate: float) -> float:
    """
    Calculates the final dollar amount after compounding
    interest over a period of (years) years

    :param years: int of years to compound for
    :param principal: int of beginning value
    :param rate: float of interest rate
    :return: float value of compounded interest, rounded to 2 decimal places
    """
    return round(principal * math.e ** (rate * years), 2)


# Run code using passed in variables
stdio.writeln("{:.2f}".format(
    compound_interest(year_arg, principal_arg, int_rate_arg)))
