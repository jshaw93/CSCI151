# James Shaw
# CSCI151
# 1/24/22
# boysandgirls.py

import random
import stdio
import stdarray
import sys

simulations = int(sys.argv[1])

# Create array of 20 int objects all set to 0
# Low chance that all 20 spaces will be used, but never 0
child_arr = stdarray.create1D(20, 0)

# Run simulations
while simulations > 0:
    children = {"boy": 0, "girl": 0}
    while children["boy"] < 1 or children["girl"] < 1:
        gender = random.choice(["boy", "girl"])
        children[gender] += 1
    summation = sum(list(children.values()))
    child_arr[summation-2] += 1
    simulations -= 1

freq_sum = sum(child_arr)
# Calculate the sum of frequency * # of children
freq_sum_xm = sum([freq * (index + 2) for index, freq in enumerate(child_arr)])
# Calculate average number of children from frequency distribution
average_children = int(freq_sum_xm / freq_sum)

output = f"""Avg # children: {average_children}
    Trials with 2 children: {child_arr[0]}
    Trials with 3 children: {child_arr[1]}
    Trials with 4 children: {child_arr[2]}
    Trials with 5 or more children: {sum(child_arr[3:])}"""

# Output simulation summary
stdio.writeln(output)
