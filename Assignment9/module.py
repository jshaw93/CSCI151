# James, Tom, Trace
# 3/5/22
# Assignment #9 module
# CSCI151

import stddraw

BAR_CODES = {
    0: "11000",
    1: "00011",
    2: "00101",
    3: "00110",
    4: "01001",
    5: "01010",
    6: "01100",
    7: "10001",
    8: "10010",
    9: "10100"
}

Y_DEFAULT = 0.4


def half_bar(x_coord):
    """Draw a half bar from the given x coordinate

    :param x_coord:
    """
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setPenRadius(.002)
    y = Y_DEFAULT + .1  # sets the beginning y coordinate a
    # certain height above Y_DEFAULT
    stddraw.line(x_coord, y, x_coord, Y_DEFAULT)


def full_bar(x_coord):
    """Draw a full bar from the given x coordinate

    :param x_coord:
    """
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.setPenRadius(.002)
    y = Y_DEFAULT + .2  # sets the beginning y coordinate a
    # certain height above Y_DEFAULT
    stddraw.line(x_coord, y, x_coord, Y_DEFAULT)


def checksum(zip_code):
    """Calculate the checksum of the provided zip code

    :param zip_code:
    :return: Checksum of zip_code
    """
    zip_codes = [int(val) for val in str(zip_code)]
    summation = sum(zip_codes)
    return 10 - (summation % 10)


def encode(zip_code):
    """

    :param zip_code: Example: 59801
    :return: list of encoded string-binary representations of
    half bars (0) and full bars (1) for the given zip code
    """
    # Handles 9 digit zip codes which may be passed in similar to
    # 33701-4313
    if type(zip_code) == str:
        zip_code = int(zip_code.replace('-', ''))

    # Encodes zip code into individual bar code values
    bars = [BAR_CODES[int(val)] for val in str(zip_code)]
    bars.append(BAR_CODES[checksum(zip_code)])
    bars.insert(0, "1")
    bars.append("1")
    return bars
