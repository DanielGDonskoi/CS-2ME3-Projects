## @file Shape.py
#  @author Daniel Guoussev-Donskoi
#  @brief Contains a generic Shape type, to be inherited by others
#  @date 2021-02-16
from abc import ABC, abstractmethod

#@brief Shape is a class that implements a shape object containing an x and y coordinate pair
# as well as a mass and inertia variable which is then inherited by other objects

class Shape(ABC):
    #@brief Abstract method to initialises cm_x, inherited by other methods
    @abstractmethod
    def cm_x(self):
        pass
    #@brief Abstract method to intialise cm_y for y coordinate, inherited by other methods
    @abstractmethod
    def cm_y(self):
        pass
    #@brief Abstract method to initialise mass, inherited by other methods
    @abstractmethod
    def mass(self):
        pass
    #@brief Abstract method to initialise objects at inertia, inherited by other methods
    @abstractmethod
    def m_inert(self):
        pass
