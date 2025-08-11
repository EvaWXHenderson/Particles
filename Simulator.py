import Display as disp
import Particles as pcl
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

disp.initialise_data(15)

fig, ax = plt.subplots()

def run(somethingUnknown):
    
    pcl.actions()
    disp.data_update()

    #print("x positions:" + str(disp.x[0]))
    #print("y positions:" + str(disp.y[0]))

    ax.clear()
    ax.scatter(disp.x, disp.y, c = "black")
    return ax

anim = FuncAnimation(fig, run, interval = 100)
plt.xticks([]) 
plt.yticks([])
plt.show()
