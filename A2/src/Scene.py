## @file Scene.py
#  @author Daniel Guoussev-Donskoi
#  @brief A Scene method that simulates the movement of an object 
#  @date 2021-02-16
#  @details This class simulates a Scene where an object moves through space over time
from scipy.integrate import odeint

#@brief A Scene class
class Scene:
	#@brief A constructor for Scene, which initialises it
	#@param Takes in a Shape, and a set of unbalanced force functions and initial velocities
	def __init__(self,s,Fx,Fy,vx,vy):
		self.s = s
		self.Fx = Fx
		self.Fy = Fy
		self.vx = vx
		self.vy =vy
	#@brief A getter function to get the shape passed to the Scene
	def get_shape(self):
		s = self.s
		return s
	#@brief A getter function to get the force functions passed to the Scene
	def get_unbal_forces(self):
		Fx = self.Fx
		Fy = self.Fy
		return Fx,Fy
	#@brief A getter function to get the initial velocity passed to the Scene
	def get_init_velo(self):
		vx = self.vx
		vy = self.vy
		return vx,vy
	#@brief A setter function to set the shape used by a Scene object to a new shape
	#@param the new shape being set
	def set_shape(self,change):
		self.s = change
	#@brief A setter function to set the unbalanced forces to new ones
	#@param the new unbalanced forces being set
	def set_unbal_forces(self,changefx,changefy):
		self.Fx = changefx
		self.Fy = changefy
	#@brief A setter function to set the initial velocities to new ones
	#@param The new initial velocities being passed to set_init
	def set_init_velo(self,changevx,changevy):
		self.vx = changevx
		self.vy = changevy
	#@brief A simulation function, to simulate movement through the scene
	#@param the ending position of the object, as well as the number of moves to get there
	def sim(self,finalpos,moves):
		times = []
		for j in range(0,moves):
			times.append((j * finalpos)/(moves - 1))
		final = odeint(self.__ode, [self.s.cm_x(),self.s.cm_y(),self.vx,self.vy],times)
		return times, final
	
	def __ode(self,w,t):
        	return [w[2],w[3], self.Fx(t)/self.s.mass(), self.Fy(t)/self.s.mass()]
