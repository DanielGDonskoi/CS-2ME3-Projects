## @file TriangleT.py
#  @author Daniel Guoussev-Donskoi
#  @brief A class that defines an equilateral triangle
#  @date 2021-02-16
from Shape import Shape

#@brief A class that inherits shape and defines an equilateral triangle using coordinates, side length and mass
class TriangleT(Shape):
    #@brief A constructor that takes x and y coords, side length and mass to initialise a triangle
    #@param x and y coordinates, side length, mass
    #@throws Throws an exception if side length or mass aren't positive, giving a Value Error
    def __init__(self, x, y, s, m):
        self.x = x
        self.y = y
        self.s = s
        self.m = m
        if (s <= 0 or m <= 0):
            raise ValueError
    #@brief Getter for x coordinate
    def cm_x(self):
        return self.x
    #@brief Getter for y coordinate
    def cm_y(self):
        return self.y
    #@brief Getter for mass
    def mass(self):
        return self.m
    #@brief Getter for movement from inertia
    def m_inert(self):
        m = self.m
        s = self.s
        final = m * (s ** 2) / 12
        return final
