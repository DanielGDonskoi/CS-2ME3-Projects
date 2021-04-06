## @file triangle_adt.py
#  @author Daniel Guoussev-Donskoi
#  @brief A class that simulates a triangle, and several related methods
#  @details A class simulating a triangle is initialised, with 3 variables 
#  @details The class assumes a, b and c are valid positive integer inputs
#  representing it's sides
#  @date January 21st, 2020
import math
from enum import Enum
#@brief A class that enumerates the 4 types of triangle in the requirements
#@details The 4 types are, equilateral, isoceles, scalene and right
class TriType(Enum):
  equilat = "equilat"
  isoceles = "isoceles"
  scalene = "scalene"
  right = "right"
class TriangleT:
  #@brief Constructor for TriangleT
  #@param a,b,c: 3 integer sides of triangle
  def __init__(self, a, b ,c):
    self.__a = a
    self.__b = b
    self.__c = c
  #@brief Function to return sides of a TriangleT object 
  #@return final: Returns as tuple of integer sides of the TriangleT object  
  def get_sides(self):
    a = self.__a
    b = self.__b
    c = self.__c
    final = (a,b,c)
    return final
  #@brief Function to check if two triangles are equal
  #@return Returns a boolean based on whether the two triangle objects are the same or not 
  def equal(self,other):
    a = self.__a
    b = self.__b
    c = self.__c
    d = other.__a
    e = other.__b
    f = other.__c
    if ((a == d) & (b == e) & (c == f)):
        return True
    else:
        return False
  #@brief Function to return the perimeter of a triangle, as the sum of it's sides
  #@return Returns an integer in final, that is the sum of the sides of a TriangleT object
  def perim(self):
    a = self.__a
    b = self.__b
    c = self.__c
    final = a + b + c
    return final
  #@brief Function to calculate the area of a triangle using Heron's formula
  #@return Returns an integer in area, that is the calculated area of the TriangleT object
  def area(self):
      a = self.__a
      b = self.__b
      c = self.__c
      s= (a + b + c ) / 2
      areabeforesqrt = (s * (s - a) * (s - b) * (s - c))
      area = (areabeforesqrt ** 0.5)
      return area
  #@brief Function to determine if a triangle forms a triangle, using the inequality theorem
  #@return Returns True if the sides form a valid triangle, False if they do not
  def is_valid(self):
      a = self.__a
      b = self.__b
      c = self.__c
      if (a + b > c ) & ( a + c > b ) & ( b + c > a ):
          return True
      else:
          return False
  #@brief Function to determine which of the enumerated types a TriangleT type falls under
  #@details The triangle can be a TriType of types equilateral, right, isoceles or scalene
  #@details In the event a triangle is both right and isoceles, it is treated as right
  #@return Returns an enumerated TriType object
  def tri_type(self):
      a = self.__a
      b = self.__b
      c = self.__c
      if (a == b == c):
          return TriType.equilat
      elif ( a ** 2 + b **2 == c ** 2):
          return TriType.right
      elif ( a == b != c ) or (b == c != a) or (a == c != b):
          return TriType.isoceles
      else:
          return TriType.scalene
