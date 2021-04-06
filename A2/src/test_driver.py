## @file test_driver.py
#  @author Daniel Guoussev-Donskoi
#  @brief A test file made to use pytest to examine how the functions behave in edge cases
#  @date
#  @details
import pytest
from CircleT import CircleT
from TriangleT import TriangleT
from BodyT import BodyT
from Scene import Scene

class TestCircleT:


	Circle1 = CircleT(1.0, 10.0, 0.5, 1.0)
	Circle2 = CircleT(2.0, 12.0, 0.5, 1.0)

	def test_cm_x(self):
		Circle1 = CircleT(1.0, 10.0, 0.5, 1.0)
		Circle2 = CircleT(2.0, 12.0, 0.5, 1.0)
		assert Circle1.cm_x() == 1.0
		assert Circle2.cm_x() == 2.0

	def test_cm_y(self):
		Circle1 = CircleT(1.0, 10.0, 0.5, 1.0)
		Circle2 = CircleT(2.0, 12.0, 0.5, 1.0)
		assert Circle1.cm_y() == 10.0
		assert Circle2.cm_y() == 12.0

	def test_mass(self):
		Circle1 = CircleT(1.0, 10.0, 0.5, 1.2)
		Circle2 = CircleT(2.0, 12.0, 0.6, 1.0)
		assert Circle1.mass() == 1.2
		assert Circle2.mass() == 1.0
	
	def test_m_inert(self):
		Circle1 = CircleT( 1.0, 10.0, 0.5, 1.2)			
		Circle2 = CircleT( 2.0, 12.0, 0.6, 1.0)
		assert Circle1.m_inert() == 0.15
		assert Circle2.m_inert() == 0.18			
	def test_Circle_Errors(self):
		with pytest.raises(ValueError):
			Circle3 = CircleT( 1.0, 10.0, -0.5, -1.2)
		with pytest.raises(ValueError):
			Circle3 = CircleT( 1.0, 10.0, -0.5, 1.2)
class TestTriangleT:


	Triangle1 = TriangleT(1.0, -10.0, 5, 17.5)
	Triangle2 = TriangleT(2.0, -5.0, 4, 18)
	
	def test_cm_x(self):
		Triangle1 = TriangleT(1.0, -10.0, 5, 17.5)
		Triangle2 = TriangleT(2.0, -5.0, 4, 18)
		assert Triangle1.cm_x() == 1.0
		assert Triangle2.cm_x() == 2.0

	def test_cm_y(self):
		Triangle1 = TriangleT(1.0, -10.0, 5, 17.5)
		Triangle2 = TriangleT(2.0, -5.0, 4, 18)
		assert Triangle1.cm_y() == -10.0
		assert Triangle2.cm_y() == -5.0
		
	def test_mass(self):
		Triangle1 = TriangleT(1.0, -10.0, 5, 17.5)
		Triangle2 = TriangleT(2.0, -5.0, 4, 18)
		assert Triangle1.mass() == 17.5
		assert Triangle2.mass() == 18
	def test_Triangle_Errors(self):
		with pytest.raises(ValueError):
			Triangle3 = TriangleT( 1.0, 10.0, - 5, 17.5)
		with pytest.raises(ValueError):
			Triangle4 = TriangleT( 1.0, 10.0, 5, -17.5)
	def test_m_inert(self):
		Triangle1 = TriangleT(1.0,-10.0,5,17.5)
		Triangle2 = TriangleT(2.0,-5.0,4,18)
		assert Triangle1.m_inert() ==36.458333333333336
		assert Triangle2.m_inert() ==24.0
