# James Shaw
# CSCI151
# 1/24/22
# dice.py
# Question answer: approximately 1,000,000

import stdarray
import stdio
import sys
import random

throws = int(sys.argv[1])

# Generate actual probabilities
probabilities = stdarray.create1D(13, 0.0)
for dice_sum in range(1, 7):
    for j in range(1, 7):
        probabilities[dice_sum + j] += 1.0
for k in range(2, 13):
    probabilities[k] /= 36.0

stdio.writeln("Exact results")
# Output exact results for each sum
for dice_sum in range(2, 13):
    stdio.writeln(
        f"Probability the sum of die is {dice_sum}: {probabilities[dice_sum]}"
    )

stdio.writeln("\nEmpyrical results")

rolls = stdarray.create1D(13, 0)

# Simulate dice throws
for _ in range(throws):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    summation = die1 + die2
    rolls[summation] += 1

# Output empyrical results for each sum
for dice_sum in range(2, 13):
    percentage = rolls[dice_sum] / throws
    stdio.writeln(f"Results the sum of die is {dice_sum}: {percentage}")

stdio.writeln("\nDifference")
# Output differences between exact results and empyrical results
for dice_sum in range(2, 13):
    percentage = rolls[dice_sum] / throws
    diff = probabilities[dice_sum] - percentage
    stdio.writeln("Difference when sum is {}: {:.3f}".format(dice_sum, diff))
