## @file test_driver.py
#  @author Daniel Guoussev-Donskoi
#  @brief A driver file made to test modules belonging to the ComplexT and TriangleT classes
#  @date January 21st, 2020
from complex_adt import ComplexT
from triangle_adt import TriangleT, TriType
import math
##TESTS FOR COMPLEX BEGIN HERE
#Example ComplexT objects for tests
a = ComplexT(1.0, 2.0)
b = ComplexT(0.5, -0.5)
c = ComplexT(1.0, 2.0)
d = ComplexT(1.0,0.0)
#Test cases for ComplexT modules
#Only four test cases for real and imag, due to simplicity of modules
if (a.real() == 1.0):
   print("first real test passes")
else:
   print("first real test FAILS")
if (b.real() == 0.5):
   print("second real test passes")
else:
   print("second real test FAILS")
if (a.imag() == 2.0):
   print("first imag test passes")
else:
   print("first imag test FAILS")
if (b.imag() == -0.5):
   print("second imag test passes")
else:
   print("second imag test FAILS")
#Two test cases for get_r, one including negatives, one without
if (a.get_r() == 2.24):
   print("first get_r test passes")
else:
   print("first get_r test FAILS")
if (b.get_r() == 0.71):
   print("second get_r test passes")
else:
   print("second get_r test FAILS")

#Two test cases for get_phi, in two separate quadrants 
if (a.get_phi() == 0.62):
   print("First get_phi test case passes")
else:
   print("First get_phi test case FAILS")
if (d.get_phi() == math.pi):
   print("Second get_phi test case passes")
#Test case for equal 

if (a.equal(c)):
  print("Equal test passes")
else:
  print("Equal test fails")
if (a.equal(b)):
  print("Equal test FAILS")
else:
  print("Equal test passes")
#Test case for conj
conjtest = a.conj()
if (conjtest.equal(ComplexT(1.0,-2.0))):
  print("Conj test passes")
else:
  print("Conj test FAILS")

#Test cases for add, one producing a negative value one without
addtest = a.add(b)
if (addtest.equal(ComplexT(1.5,1.5))):
  print("First add test passes")
else:
  print("First add test FAILS")
addtest2 = a.add(ComplexT(- 2.0, -2.5))
if (addtest2.equal(ComplexT(-1.0,-0.5))):
  print("Second Add test passes")
else:
  print("Second Add test FAILS")

#Test cases for sub, one subtracting a negative

subtest = a.sub(b)
if (subtest.equal(ComplexT(0.5,2.5))):
  print("First sub test passes")
else:
  print("First sub test FAILS")
subtest2 = a.sub(ComplexT(- 2.0, -2.5))
if (subtest2.equal(ComplexT(3.0,4.5))):
  print("Second sub test passes")
else:
  print("Second sub test FAILS")

#Test case for mult

multtest=a.mult(b)
if (multtest.equal(ComplexT(1.5,0.5 ))):
  print("mult test passes")
else:
  print("mult test FAILS")

#Test case for recip
reciptest=a.recip()
if (reciptest.equal(ComplexT(0.2,-0.4))):
  print("recip test passes")
else:
  print("recip test FAILS")

#Test case for div
divtest=a.div(b)
if (divtest.equal(ComplexT(-1.0,3.0))):
  print("div test passes")
else:
  print("div test FAILS")

#Test case for sqrt
sqrttest=a.sqrt()
if (sqrttest.equal(ComplexT(1.27,0.79))):
  print("sqrt test passes")
else:
  print("sqrt test FAILS")

#TESTS FOR TRIANGLE BEGIN HERE
#Example objects for Triangle
triangle = TriangleT(3,4,5)
triangle2 = TriangleT(3,4,8)
triangle3 = TriangleT(3,3,3)
triangle4 = TriangleT(5,12,13)
#Test cases for TriangleT in triangle_adt.py

#Test cases for get_sides
if (triangle.get_sides()==(3,4,5)):
  print("First get_sides test passed")
else:
  print("First get_sides test FAILED")
if (triangle3.get_sides()==(3,3,3)):
  print("Second get_sides test passed")
else:
  print("Second get_sides test FAILED")

#Test cases for equal, one where the two are equal, one where the two are not
if (triangle.equal(triangle3) == False):
  print("First equal test passed")
else:
  print("First equal test FAILED")
if (triangle.equal(TriangleT(3,4,5)) == True):
  print("Second equal test passed")
else:
  print("Second equal test FAILED")

#Test cases for perim, using two separate triangles
if (triangle.perim()==12):
  print("First perim test case passed")
else:
  print("First perim test case FAILED")
if (triangle3.perim()==9):
  print("First perim test case passed")
else:
  print("First perim test case FAILED")

#Test cases for area using heron's formula. 
if (triangle.area()==6):
  print("First area test case passed")
else:
  print("First area test case FAILED")
if (triangle4.area()==30):
  print("Second area test case passed")
else:
  print("Second area test case FAILED")

#Test cases for whether a triangle is possible using the inequality theorem
if (triangle.is_valid() == True):
  print("First is_valid test case passed")
else:
  print("First is_valid test case FAILED")
if (triangle2.is_valid() == False):
  print("Second is_valid test case passed")
else:
  print("Second is_valid test case FAILED")

#Test cases for tri_type, using multiple types of triangles
if (triangle.tri_type() == TriType.right):
  print("First tri_type test case passed")
else:
  print("First tri_type test case FAILED")
if (triangle3.tri_type() == TriType.equilat):
  print("Second tri_type test case passed")
else:
  print("Second tri_type test case passed")
if (TriangleT(2,2,5).tri_type() ==TriType.isoceles):
  print("Third tri_type test case passed")
else:
  print("Third tri_type test case failed")
if (TriangleT(2,7,8).tri_type() == TriType.scalene):
  print("Fourth tri_type test case passed")
else:
  print("Fourth tri_type test case FAILED")
