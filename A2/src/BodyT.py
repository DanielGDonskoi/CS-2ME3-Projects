## @file BodyT.py
#  @author Daniel Guoussev-Donskoi
#  @brief A class that defines a body of no particular shape
#  @date 2021-02-16
from Shape import Shape

#@brief A helper function that sums up a list of values
#@param A list m of numbers
def sum(m):
    total = 0
    for i in m:
        total = total + i
    return total


def cm(z, m):
    sum1 = sum(m)
    sum2 = 0
    length = len(z)
    for i in range(0, length):
        sum2 = sum2 + (z[i] * m[i])
    final = sum2 / sum1
    return final


def mmom(x, y, m):
    sum1 = 0
    for i in range(0, len(x)):
        sum1 = sum1 + (m[i] * ((x[i] ** 2) + (y[i] ** 2)))
    return sum1

#@brief A class that defines a Body object, 
#@param Inherits from shape like triangle and circle
class BodyT(Shape):
    #@brief A Constructor that creates a Body object
    #@param Takes in coordinate sets of x and y  and the mass of the object
    def __init__(self, x, y, m):
        self.x = x
        self.y = y
        self.m = m
    #@brief A getter function that returns cm_x coordinates and masses
    def cm_x(self):
        x = self.x
        m = self.m
        return cm(x, m)
    #@brief a getter function that returns cm_y coordinates and masses
    def cm_y(self):
        y = self.x
        m = self.m
        return cm(y, m)
    #@brief a Getter function that returns the total mass
    def mass(self):
        m = self.m
        return sum(m)
    #@brief a getter function that returns the momentum from inertia
    def m_inert(self):
        m = self.m
        x = self.x
        y = self.y
        final = mmom(x, y, m) - (sum(m) * ((cm(x, m) ** 2) + (cm(y, m) ** 2)))
        return final
