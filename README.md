# Simulation of Particles
An attempt at simulating particles and their interactions in a 2D space, displayed to indicate phase-characterisitcs (e.g. gas-like, liquid-like, solid-like appearance). Number/density of 'particles' being simulated can be chosen (similar to increasing pressure/concentration). Repulsive and attractive forces influence the movement of particles. However, particle acceleration/velocity, as in a vaccum, are not affected by collision with the 'walls' of the display.

Utilises root-mean-square (RMS) velocities and masses in amu.

Repulsive and attractive forces between 'particles' are calculated based on the Lennard-Jones Potential model (where force is the negative derivative of potential).

## Particles.py
Contains Particle class and functions for updating of particle positions/velocities/accleration.

Particle mass can be changed to emulate specific elements by changing *self.mass* in the Particles class. This should make the repulsive/attractive effects more characteristic to specific elements.

## Display.py
Contains functions and info for the display of information/movement of particles.

### Simulator.py
Used to run program.

### Sources:
Sebastian Lague (2025), Coding Adventure: Simulating Fluids. Youtube. Available at: https://youtu.be/rSKMYc1CQHE?si=o2x4cRYxyq534Sty [Accessed 1 Aug. 2025]

Chemistry LibreTexts. (2013). Lennard-Jones Potential. [online] Available at: https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_(Physical_and_Theoretical_Chemistry)/Physical_Properties_of_Matter/Atomic_and_Molecular_Properties/Intermolecular_Forces/Specific_Interactions/Lennard-Jones_Potential [Accessed 12 Aug. 2025]

Physics LibreTexts. (2016). 2.5: Force and Potential Energy. [online] Available at: https://phys.libretexts.org/Under_Construction/Purgatory/2%3A_Applying_Models_to_Mechanical_Phenomena/2.5%3A_Force_and_Potential_Energy [Accessed 12 Aug. 2025]

Notes on thermodynamics and the Lennard-Jones potential. [online] Available at: https://walterfreeman.github.io/phys307/notes/lj-notes.pdf [Accessed 13 Aug. 2025]
