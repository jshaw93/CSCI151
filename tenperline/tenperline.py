# James Shaw
# CSCI151
# 2/1/22
# tenperline.py

import stdio

count = 0

while not stdio.isEmpty():
    value = stdio.readInt()
    # Output values right aligned for each column in 10 columns max
    if count != 9:
        stdio.writef("  %2d", value)
        count += 1
    else:
        stdio.writef("  %2d\n", value)
        count = 0
