## @file complex_adt.py
#  @author Prakarsh Kamal
#  @brief Complex numbers module (class)
#  @date 13 Jan 2021

import math
import cmath

## @brief This class represents complex numbers
#  @details This class represents complex numbers as (x, y) coordinates
#  where x is the real part and y is the imaginary part
class ComplexT:


	## @brief init constructor for class
	#  @details initializing attributes (x, y) of ComplexT class
	#  @param x is real part of complex number
	#  @param y is imaginary part of complex number
	def __init__(self, x, y):
		self.x = x
		self.y = y	



	## @brief getter method real
	#  @return returns real part 'x' of complex number
	def real(self):
		return self.x



	## @brief getter method imag
	#  @return returns imaginary part 'y' of complex number
	def imag(self):
		return self.y



	## @brief getter method get_r
	#  @return returns magnitude of complex number utilizing math.sqrt()
	def get_r(self):
		return math.sqrt(self.x**2 + self.y**2)



	## @brief getter method get_phi
	#  @details assuming that self.x > 0
	#  @return returns argument(angle/phase) of complex number utilizing cmath.phase)
	def get_phi(self):
		i = complex(self.x, self.y)
		return cmath.phase(i)



	## @brief method checks current object with argument
	#  @param i is a new complex number with real and imaginary parts
	#  @return returns boolean value after comparing corresponding parts of current object and argument
	def equal(self, i):
		if (self.x == i.real()) and (self.y == i.imag()):
			return True
		return False

	

	## @brief method returning ComplexT object
	#  @return returns conjugate of complex number	
	def conj(self):
		return ComplexT(self.x, -self.y)



	## @brief method to calculate sum of current object and argument
	#  @param i is a new complex number with real and imaginary parts
	#  @return returns ComplexT object after adding corresponding parts of current object and argument
	def add(self, i):
		return ComplexT(self.x + i.real(), self.y + i.imag())



	## @brief method to calculate difference of current object and argument
	#  @param i is a new complex number with real and imaginary parts
	#  @return returns ComplexT object after subtracting corresponding parts of current object and argument
	def sub(self, i):
		return ComplexT(self.x - i.real(), self.y - i.imag())



	## @brief method to calculate multiplication of current object and argument
	#  @param i is a new complex number with real and imaginary parts
	#  @return returns ComplexT object after properly calculating corresponding parts of current object and argument
	def mult(self, i):
		return ComplexT((self.x * i.real() - self.y * i.imag()), (self.y * i.real() + self.x * i.imag()))

	

	## @brief method to calculate reciprocal of current object
	#  @details assuming current object > 0 (denominator is not 0) 
	#  @return returns ComplexT object after correctly computing reciprocal
	def recip(self):
		denom = (self.x) ** 2 + (self.y) ** 2
		f = self.x / denom
		g = -self.y / denom
		return ComplexT(f, g)



	## @brief method to calculate division of current object and argument
	#  @details assuming that i > 0 (denominator is not 0)
	#  @param i is a new complex number with real and imaginary parts
	#  @return returns ComplexT object after properly calculating the division of current object and argument
	def div(self, i):
		mag = (i.real() ** 2 + i.imag() ** 2)
		r_1 = (self.x * i.real() + self.y * i.imag())
		r_2 = (self.y * i.real() - self.x * i.imag())
		ans_1 = r_1 / mag
		ans_2 = r_2 / mag
		return ComplexT	(ans_1, ans_2) 	 



	## @brief method to calculate positive square root of current object
	#  @details current object is > 0 (not negative) 
	#  @return returns ComplexT object utilizing cmath.sqrt()
	def sqrt(self):
		i = complex(self.x, self.y)
		j = cmath.sqrt(i)
		return ComplexT(j.real, j.imag)

