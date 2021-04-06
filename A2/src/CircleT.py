## @file CircleT.py
#  @author Daniel Guoussev-Donskoi
#  @brief CircleT is a class that initialises a Circle object to be moved through a scene in motion
#  @date 2021-02-16
from Shape import Shape

#@brief CircleT creates a Circle object, defined by it's coordinates, mass and movement from inertia
class CircleT(Shape):
    #@brief Constructor for CircleT, represents a Circle object as a coordinate pair, mass and movement from inertia
    #@param A pair of coordinates, it's radius and it's mass
    #@throws If radius or mass aren't positive, throws a value error
    def __init__(self, x, y, r, m):
        self.x = x
        self.y = y
        self.r = r
        self.m = m
        if (r <= 0) or (m <= 0):
            raise ValueError
    #@brief Sets the x coordinate of the Circle
    def cm_x(self):
        return self.x
    #@brief Sets the y coordinate of the Circle
    def cm_y(self):
        return self.y
    #@brief Sets the mass of the Circle
    def mass(self):
        return self.m
    #@brief Sets the movement from inertia of the Circle
    def m_inert(self):
        m = self.m
        r = self.r
        final = m * (r ** 2) / 2
        return final


