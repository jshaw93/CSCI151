# James Shaw
# CSCI151
# 2/1/22
# randomintseq.py > part of tenperline.py project

import random
import sys
import stdarray
import stdio

# python randomintseq.py 100 50 > max_int = 100, iterations = 100
max_int = int(sys.argv[1])
iterations = int(sys.argv[2])

result_arr = stdarray.create1D(iterations, 0)

for iteration in range(iterations):
    result_arr[iteration] = str(random.randint(0, max_int - 1))

stdio.write(' '.join(result_arr))
