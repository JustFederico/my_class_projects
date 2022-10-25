import math
from check import print_rectangle_properties


class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def get_area(self: float):
        return self.width * self.height

    def get_perimeter(self: float):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return math.sqrt(self.width ** 2 + self.height ** 2)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height


rec1 = Rectangle(9.0, 12)
rec2 = Rectangle(20.0, 15)
rec3 = Rectangle(30.0, 15)


def main():
    print_rectangle_properties(rec1)
    print_rectangle_properties(rec2)
    print_rectangle_properties(rec3)


if __name__ == "__main__":  # main file being executed. Chapter 14 Point 9 sec edition
    main()