## @file triangle_adt.py
#  @author Prakarsh Kamal
#  @brief Triangle module (class)
#  @date 18 Jan 2021

import math
import enum

## @brief This class represents types of triangles
#  @details initializing 4 types of triangles using enum
class TriType(enum.Enum):
	equilat = 1
	isoceles = 2
	scalene = 3
	right = 4


## @brief This class represents triangles
#  @details This class represents triangles as integer arguments
#  where each argument is the length of the side of the triangle
class TriangleT:



	## @brief init constructor for class
	#  @details initializing attributes (a, b, c) for TriangleT class
	#  For input to be valid triangle, all side lengths must be > 0
	#  @param a is length of side of triangle
	#  @param b is length of side of triangle
	#  @param c is length of side of triangle
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c



	## @brief getter method get_sides
	#  @details assuming input is a valid triangle
	#  @return returns tuple of integers where each element 
	#  is the length of side of triangle
	def get_sides(self):
		return (self.a, self.b, self.c)


	
	## @brief method checks current object with argument
	#  @details assuming that input is a valid triangle
	#  @param z is a new triangle with three sides
	#  @return returns Boolean value after comparing side lengths of current object and argument
	def equal(self, z):
		if ((self.a == z.a or self.a == z.b or self.a == z.c) 
		and (self.b == z.b or self.b == z.a or self.b == z.c) 
		and (self.c == z.c or self.c == z.a or self.c == z.b)):
			return True
		return False



	## @brief method calculating perimeter
	#  @details assuming that input is a valid triangle
	#  @return returning perimeter of triangle which is sum of all 3 sides as an integer
	def perim(self):
		return self.a + self.b + self.c		



	## @brief method calculating perimeter
	#  @details assuming that input is a valid triangle
	#  @return returning area of triangle implementing Heron's formula and utilizing math.sqrt()
	def area(self):
		semi = self.perim() / 2
		return math.sqrt( semi * (semi - self.a) * (semi - self.b) * (semi - self.c) )



	## @brief method to validate if object is triangle
	#  @details assuming that input is a valid triangle
	#  @return returns Boolean value if sum of two sides is greater than third
	def is_valid(self):
		if ( ((self.a + self.b) > self.c) and ((self.b + self.c) > self.a) and ((self.a + self.c) > self.b) ):
			return True
		return False		



	## @brief method to check type of triangle
	#  @details assuming that input is a valid triangle
	#  @return returns type of triangle based on relative properties
	def tri_type(self):
		if (self.a == self.b and self.a == self.c and self.b == self.c):
			return TriType.equilat
		elif ((self.a == self.b and self.a != self.c) 
		or (self.b == self.c and self.b != self.a)
		or (self.c == self.a and self.c != self.b)):
			return TriType.isoceles
		elif ((self.a ** 2 + self.b ** 2 == self.c ** 2) 
		or (self.a ** 2 + self.c ** 2 == self.b ** 2) 
		or (self.b ** 2 + self.c ** 2 == self.a ** 2)):
			return TriType.right
		else:
			return TriType.scalene

