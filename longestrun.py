# James Shaw
# CSCI151
# 2/1/22
# longestrun.py

import stdio

best = None
previous = None
count = 0
best_count = 0

while not stdio.isEmpty():
    value = stdio.readInt()

    # Track the longest recurring value during runtime
    # comparing the current value to the previous
    # and comparing the current count of the current value
    # to the highest count currently on record
    if value == previous:
        count += 1
        if count > best_count:
            best_count = count
            best = value
    else:
        count = 1
    previous = value

# Output for 6 consecutive 8s should be:
# Longest run:  6 consecutive 8s
stdio.writeln(
    "Longest run:  " + str(best_count) +
    " consecutive " + str(best) + "s"
)
