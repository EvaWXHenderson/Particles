import Display_G as disp
import Gravity_deceleration as pcl
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

disp.initialise_data(15)

fig, ax = plt.subplots()

def run(somethingUnknown):
    
    pcl.actions()
    disp.data_update()
    
    ax.clear()

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_xticks([])
    ax.set_yticks([])

    ax.scatter(disp.x, disp.y, c = "black")
    return ax

anim = FuncAnimation(fig, run, frames = 100, interval = 10)
plt.show()

disp.print_positions()