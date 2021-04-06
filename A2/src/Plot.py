## @file Plot.py
#  @author Daniel Guoussev-Donskoi
#  @brief A plot module that plots the Scene depicted in Scene.py
#  @date 2021-02-16
#  @details Uses matplotlib to illustrate a set of coordinates, based on the velocities of objects passed to it
import matplotlib.pyplot as plt

#@brief A plot function that takes in both a scene and a time to plot it over
#@param The scene passed to the function, and the time over which to plot it
def plot(w, t):
    x = []
    y = []
    for i in range(len(w)):
        x.append(w[i][0])
        y.append(w[i][1])
    fig, axs = plt.subplots(3)
    fig.suptitle("Motion")
    fig.tight_layout()
    axs[0].plot(t, x)
    axs[0].set_ylabel("x(m)")
    axs[0].set_xlabel("t(s)")
    axs[1].plot(t, y)
    axs[1].set_ylabel("x(m)")
    axs[1].set_xlabel("t(s)")
    axs[2].plot(x, y)
    axs[2].set_ylabel("x(m)") 
    axs[2].set_xlabel("t(s)") 

