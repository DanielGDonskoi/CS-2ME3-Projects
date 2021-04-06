## @file complex_adt.py
#  @author Daniel Guoussev-Donskoi
#  @title ComplexT
#  @date January 21st, 2020

## @brief This class represents a complex number
# @details This class represents a complex number as a an (x,y) pair of
# real and imaginary components respectively
# @details All modules which take an input outside the object itself, assume the 
# input is another ComplexT object composed of two integers
import math
import cmath
class ComplexT:
  #@brief Constructor for ComplexT
  #@details Constructor accepts two parameters for real and imaginary parts
  #@param x, for real number part of a complex number
  #@param y, for imaginary part of a complex number
  def __init__(self, x, y):
    self.__x = x
    self.__y = y
  ##@brief Returns the real part of a complex number
  #@return x integer, for real number
  def real(self):
      return self.__x
  ##@brief Returns the imaginary part of a complex number
  #@return y integer, for imaginary number
  def imag(self):
      return self.__y
  ##@brief Returns the magnitude of the complex number(as int)
  #@return final integer, for modulus/magnitude of complex
  def get_r(self):
      first = (self.__x)**2
      second = (self.__y)**2
      modulus = (first + second)**0.5
      final = round(modulus,2)
      return final
  ##@brief Returns the phase of the complex number(In radians)
  #@return final integer, for phase of complex number in rad
  #@details Assumed x and y were not both zero, which would result in an undefined argument
  def get_phi(self):
      first = (self.__x)
      second = (self.__y)
      if (second == 0 ):
      	return math.pi
      else:
      	denominator = (((first**2)+(second**2))**0.5) + first
      	semifinal = second / denominator
      	final = round(semifinal,2)
      	return final
  ##@brief Compares two ComplexT objects and returns True if their value is same
  #@param compare: A second ComplexT object being compared to the first
  #@return Returns a True or False boolean depending on if the objects match
  def equal(self,compare):
      if (self.__x == compare.__x) & (self.__y == compare.__y):
        return True
      else:
        return False
  #@brief Takes a ComplexT object and returns it's conjugate in the form of a ComplexT object
  #@return Returns a ComplexT object with values that are the conjugate of the original object
  def conj(self):
    final = ComplexT(self.__x,-self.__y)
    return final
  #@brief Takes a ComplexT object and adds it's values to those of another ComplexT object
  #@param other: A second ComplexT object, with an associated real and imaginary part
  #@return Returns a ComplexT object that is the sum of self and the passed parameter object
  def add(self,other):
    newx = self.__x + other.__x
    newy = self.__y + other.__y
    final = ComplexT(newx,newy)
    return final
  #@brief Takes a ComplexT object and subtracts it's values to those of another ComplexT object
  #@param other: A second ComplexT object, with an associated real and imaginary part
  #@return Returns a ComplexT object that is the difference of self and the passed parameter object
  def sub(self,other):
    newx = self.__x - other.__x
    newy = self.__y - other.__y
    final = ComplexT(newx,newy)
    return final   
  #@brief Takes a ComplexT object and another ComplexT object and returns a multiple of both
  #complex numbers represented as a real and imaginary part
  #@param other: A second ComplexT object, representing a complex number
  #@return Returns a ComplexT object that represents the result of multiplying the two
  def mult(self,other):
    a = self.__x* other.__x
    b = (self.__x*other.__y) + (self.__y*other.__x)
    c = (self.__y * other.__y * (-1))
    real = a + c
    imag = b
    final = ComplexT(real,imag)
    return final
  #@brief Takes a complex number and returns it's reciprocal
  #@return Returns a ComplexT object that represents the real and imag parts of the reciprocal
  #@details Assumed that x and y were not both 0, As that would cause a zero division error
  def recip(self):
    x = self.__x
    y = self.__y
    real = (x / ((x**2)+(y**2)))
    imag = -(y / ((x**2)+(y**2)))
    final = ComplexT(real,imag)
    return final
  #@brief Takes a complex number and divides it by another complex number
  #@param other: A second complex number, acting as the divisor
  #@details Assumed the other variable was not 0 + 0i as that would cause a ZeroDivisionError
  #@return Returns a ComplexT object that represents the real and imaginary parts
  def div(self,other):
    a = self.__x
    b = self.__y
    c = other.__x
    d = other.__y
    real = ( ((a * c)+(b * d)) / ((c**2)+(d**2)) )
    imag = ( ((b * c)-(a * d)) / ((c**2)+(d**2)) )
    final = ComplexT(real,imag)
    return final
  #@brief Takes a complex number and returns it's positive square root
  #@return: Returns a ComplexT object that is the square root of the original object
  def sqrt(self):
    x = self.__x
    y = self.__y
    root = cmath.sqrt(complex(x, y))
    real1 = root.real
    imag1 = root.imag
    real = round(real1,2)
    imag = round(imag1,2)
    return ComplexT(real,imag)


