
from math import pi
from sda_ex_oop_1_mz.figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return pi * self.r * self.r


class Triangle(Figure):
    def __init__(self, high, base):
        self.high = high
        self.base = base

    def get_area(self):
        return (self.high * self.base)/2.0
