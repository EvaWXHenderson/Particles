# Simulation of Particles
An attempt at simulating particles and their interactions in a 2D space, displayed to indicate phase-characterisitcs (e.g. gas-like, liquid-like, solid-like appearance). Number/density of 'particles' being simulated can be chosen (similar to increasing pressure/concentration). Repulsive and attractive forces influence the movement of particles. However, particle acceleration/velocity, as in a vaccum, are not affected by collision with the 'walls' of the display.

Repulsive and attractive forces between 'particles' are calculated based on the Lennard-Jones Potential model (where force is the negative derivative of potential):
<p align="center">
$V(r) = 4ε[(σ/r)^{12} - (σ/r)^6]$    
</p>
<p align="center"> 
$F(r) = dV/dr = ε[2(σ^{12}/r^{13}) - (σ^6/r^7)]$
</p>

5 particles|10 particles|15 particles
--|--|--
![](https://github.com/EvaWXHenderson/Particles/blob/main/readme%20-%20material/Screen%20Recording%202025-08-15%20at%2017.08.51.gif)|![](https://github.com/EvaWXHenderson/Particles/blob/main/readme%20-%20material/B0C7FB56-5DD5-49C5-98AE-70AC33EA50FC.gif)|![](https://github.com/EvaWXHenderson/Particles/blob/main/readme%20-%20material/8B1F33E0-E6ED-4660-A8FB-7937B63FF80E.gif)
<p align="center">
Above: iterations of program with 5, 10, and 15 particles. Particles had mass of 1.67x10<sup>-27</sup> kg (mass of hydrogen atom), with values sigma = 2, epsilon = 4.98x10<sup>-26</sup>.
</p>

## Files
### Particles.py
Contains Particle class and functions for updating of particle positions/velocities/accleration.

Particle mass (in kg) can be changed to emulate specific elements. This should make the repulsive/attractive effects more characteristic to specific elements.

Mass and the Lennard-Jones constants epsilon and sigma can be changed/set up:
- a larger mass will results in a reduced velocity
- a larger epsilon with result in larger 'forces' of attraction between particles
- a larger sigma value increases the distance at which repulsive/attractive forces will affect particles (particles will repel eachother at further distances)

### Display.py
Contains functions and info for the display of information/movement of particles.


Possibly useful printing functions are specified below:    
**print_positions()** - prints particles last position as coordinates    
**print_forces()** - prints particles last force values along the x and y axes as a tuple (Newtons)    
**print_acceleration()** - prints particles last acceleration values along the x and y axes as a tuple (Newtons per Kg)    
**print_potential()** - prints particles last Lennard-Jones Potential (V(x)) values along the x and y axes as a tuple (Joules)    
**print_velocities()** - prints particles last Velocities values along the x and y axes as a tuple (Angstroms per 0.1 seconds)

### Simulator.py
Used to run program.  

The set up simulation is intended to model hydrogen particles (mass = 1.67x10<sup>-27</sup>, sigma = 2, epsilon = 4.98x10<sup>-26</sup>).

## Running Program
To initialise the program (initialisation) and specify the number of particles desired, the particle's mass (kg), the particle's sigma value (Å) and the particle's epsilon value (J):
```
Display.initialise_data(no. particles, mass, sigma, epsilon)
```
To run program, after intialisation, fig/ax can be defined, the run() function can be called, and FuncAnimation used to create the pop-up as below:
```
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
```
*Note: recommended time interval (delt_t) is 0.1, with an interval paratermeter of 10*

## Decceleration
Currently the only complete section of the project. Contains files for running a simulation where particles are made to bounce and decelerate with gravity.

https://github.com/user-attachments/assets/603c88bb-adf8-4a6b-852e-31ebded9f473

**Contains**:    
Gravity_Deceleration.py - main file    
Display_G - file for functions relating to the display    
Sim - file for running program

### Sources:
Sebastian Lague (2025), Coding Adventure: Simulating Fluids. Youtube. Available at: https://youtu.be/rSKMYc1CQHE?si=o2x4cRYxyq534Sty [Accessed 1 Aug. 2025]

Chemistry LibreTexts. (2013). Lennard-Jones Potential. [online] Available at: https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Physical_Properties_of_Matter/Atomic_and_Molecular_Properties/Intermolecular_Forces/Specific_Interactions/Lennard-Jones_Potential [Accessed 12 Aug. 2025]

Physics LibreTexts. (2016). 2.5: Force and Potential Energy. [online] Available at: https://phys.libretexts.org/Under_Construction/Purgatory/2%3A_Applying_Models_to_Mechanical_Phenomena/2.5%3A_Force_and_Potential_Energy [Accessed 12 Aug. 2025]

Notes on thermodynamics and the Lennard-Jones potential. [online] Available at: https://walterfreeman.github.io/phys307/notes/lj-notes.pdf [Accessed 13 Aug. 2025]
