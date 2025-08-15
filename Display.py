import matplotlib.pyplot as plt
import Particles as pcl

x = []
y = []

def coord_update():
    global x, y
    for point in range(len(pcl.p_positions)):
        x.append(pcl.p_positions[point][0])
        y.append( pcl.p_positions[point][1])

def clear():
    global x, y
    x = []
    y = []

def initialise_data(particles = 15):
    pcl.create_particles(particles)

    coord_update()

def data_update():
    clear() # x and y now back to empty lists to be re-updated with new coordinates.
    coord_update()

def print_positions():
    for particle in pcl.particles:
        print("Position:" + str(particle.position))

def print_forces():
    for particle in pcl.particles:
        print("Lennard-Jones force (N):" + str(particle.forces_print))

def print_acceleration():
    for particle in pcl.particles:
        print("Acceleration (N/kg): " + str(particle.acceleration))

def print_potential():
    for particle in pcl.particles:
        print("Potentials (J) : " + str(particle.potentials))

def print_velocities():
    for particle in pcl.particles:
        print("Velocities (A/s): " + str(particle.velocity))