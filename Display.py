import Particles as pcl
import math

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

def initialise_data(particles = 15, mass = 1.67*10**(-27), sigma = 2, epsilon = 4.98*10**(-26)):
    pcl.create_particles(mass, sigma, epsilon, particles)

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

def print_kinetic_energy():
    print("Kinetic energy: " + str(pcl.K_energy_sys) + " (Kg(A/s)^2)") #goal to be in joules (Kg(m/s)^2)

def print_temp_sys():
    print("Temperature: " + str(pcl.T_sys) + " (K)") #currently not accurate
