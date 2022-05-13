# James Shaw
# CSCI151
# 4/21/22
# rectangle.py

import random
import stddraw


class Rectangle:
    # Construct self with center (x, y), width w, and height h.
    def __init__(self, x, y, w, h):
        self._x = x
        self._y = y
        self._width = w
        self._height = h

    # Return the area of self.
    def area(self):
        return self._width * self._height

    # Return the perimeter of self.
    def perimeter(self):
        return self._width * 2 + self._height * 2

    # Return an array of coordinates for all sides, rounded to
    # the 100th place
    def coordinates(self):
        min_x = self._x - self._width / 2
        max_x = self._x + self._width / 2
        min_y = self._y - self._height / 2
        max_y = self._y + self._height / 2
        return [round(min_x, 2), round(max_x, 2),
                round(min_y, 2), round(max_y, 2)]

    # Return True if self intersects other, and False otherwise.
    def intersects(self, other):
        rec1_x1, rec1_x2, rec1_y1, rec1_y2 = self.coordinates()
        rec2_x1, rec2_x2, rec2_y1, rec2_y2 = other.coordinates()
        return rec1_x2 >= rec2_x1 and rec2_x2 >= rec1_x1 and \
            rec1_y2 >= rec2_y1 and rec2_y2 >= rec1_y1 and not \
            self._strict_contains(other)

    # Return True if other is inside of self, and False
    # otherwise.  Allows coincident lines
    def contains(self, other):
        rec1_x1, rec1_x2, rec1_y1, rec1_y2 = self.coordinates()
        rec2_x1, rec2_x2, rec2_y1, rec2_y2 = other.coordinates()
        return rec1_x1 <= rec2_x1 <= rec2_x2 <= rec1_x2 and \
            rec1_y1 <= rec2_y1 <= rec2_y2 <= rec1_y2

    # Same as contains() but more strictly contained, does
    # not allow coincident lines
    def _strict_contains(self, other):
        rec1_x1, rec1_x2, rec1_y1, rec1_y2 = self.coordinates()
        rec2_x1, rec2_x2, rec2_y1, rec2_y2 = other.coordinates()
        return rec1_x1 < rec2_x1 <= rec2_x2 < rec1_x2 and \
            rec1_y1 < rec2_y1 <= rec2_y2 < rec1_y2

    # Compiles a list of line segments for draw()
    def _lines(self):
        coords = self.coordinates()
        return [(coords[0], coords[2], coords[0], coords[3]),
                (coords[0], coords[3], coords[1], coords[3]),
                (coords[1], coords[2], coords[1], coords[3]),
                (coords[0], coords[2], coords[1], coords[2])]

    # Draw self on stddraw.
    def draw(self):
        stddraw.setPenRadius(0.002)
        for line in self._lines():
            stddraw.line(line[0], line[1], line[2], line[3])


if __name__ == "__main__":
    import sys
    import stdio
    n = int(sys.argv[1])
    lo = round(float(sys.argv[2]), 2)
    hi = round(float(sys.argv[3]), 2)
    rectangles = []
    areas = []
    perimeters = []

    for i in range(n):
        # Generates n rectangles within the bounds of lo, hi
        # rounds to 2 decimal places to allow coincident lines
        x = round(random.uniform(lo, hi), 2)
        y = round(random.uniform(lo, hi), 2)
        width = round(random.uniform(lo, hi), 2)
        height = round(random.uniform(lo, hi), 2)
        rectangle = Rectangle(x, y, width, height)
        rectangles.append(rectangle)
        areas.append(rectangle.area())
        perimeters.append(rectangle.perimeter())

    stdio.writeln("Average area: {:.2f}".format(
        sum(areas) / len(areas))
    )
    stdio.writeln("Average perimeter: {:.2f}".format(
        sum(perimeters) / len(perimeters))
    )

    intersect = 0
    contained = 0
    # Calculate intersects and contains between rectangle pairs
    # ignores if the rectangle pair is the same object
    for rectangle in rectangles:
        for rec1 in rectangles:
            if rectangle is rec1:
                continue
            if rectangle.intersects(rec1):
                intersect += 1
            if rectangle.contains(rec1):
                contained += 1

    stdio.writeln("Total intersects: " + str(intersect))
    stdio.writeln("Total contained rectangles: " + str(contained))

    for rectangle in rectangles:
        rectangle.draw()

    stddraw.show()
