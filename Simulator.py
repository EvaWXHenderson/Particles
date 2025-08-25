import Display as disp
import Particles as pcl
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

disp.initialise_data(particles=30)

fig, ax = plt.subplots()

def run(x):
    
    pcl.actions()
    disp.data_update()
    
    ax.clear()

    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_xticks([])
    ax.set_yticks([])

    graph = ax.scatter(disp.x, disp.y, c = "black")
    legend1 = "Kinetic energy: " + str(pcl.K_energy_sys) + "(Kg(A/s)^2)"
    #"\n Pressure: " + str(pcl.pressure) + "(N/(A^2))"

    K_energy = mpatches.Patch(color='white', label=legend1)

    ax.legend(handles=[K_energy], loc = 'upper right')
 
    return ax

anim = FuncAnimation(fig, run, frames = 100, interval = 10)
plt.show()

#disp.print_positions()
#disp.print_forces()
#disp.print_acceleration()
#disp.print_potential()
#disp.print_velocities()
#disp.print_kinetic_energy()
#disp.print_pressure()