# James, Tom, Trace
# 3/5/22
# Assignment #9 client
# CSCI151

import sys
import module
import stddraw


def tests():
    assert module.checksum(59801) == 7
    assert module.checksum(337014313) == 5
    assert module.encode(59801) == [
        '1', '01010', '10100', '10010',
        '11000', '00011', '10001', '1']


def draw(bars):
    x_coord = 0.2
    for bar in bars:
        for digit in bar:
            if digit == "0":
                module.half_bar(x_coord)
            else:
                module.full_bar(x_coord)
            x_coord += 0.01


if __name__ == "__main__":
    zip_code = sys.argv[1]
    if zip_code == "-t":
        tests()
    else:
        encoded = module.encode(zip_code)
        draw(encoded)
        stddraw.show()
