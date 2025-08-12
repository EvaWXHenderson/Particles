# Simulation of Particles
An attempt at simulating particles and their interactions, displayed to indicate phase-characterisitcs (e.g. gas-like, liquid-like, solid-like appearance). Particles modelled are intended to resemble hydrogen molecules, gravity not taken into account.

Utilises root-mean-square (RMS) velocities and masses in amu.

## Main
### Particles.py
Contains Particle class and functions for updating of particle positions/velocities/accleration.

### Display.py
Contains functions and info for the display of information/movement of particles.

### Simulator.py
Used to run program.

## Decceleration
Currently the only complete section of the project. Contains files for running a simulation where particles are made to bounce and decelerate with gravity.

<video src="https://github.com/EvaWXHenderson/Particles/blob/main/Deceleration_Gravity/recording/Screen%20Recording%202025-08-12%20at%2016.08.11.mov" width=180 />
  
Contains:
gravity_deceleration.py - main file    
display_g - file for functions relating to the display    
sim_g - file for running program

## Sources:
Sebastian Lague (2025), Coding Adventure: Simulating Fluids. Youtube. Available at: https://youtu.be/rSKMYc1CQHE?si=o2x4cRYxyq534Sty [Accessed 1 Aug. 2025]
