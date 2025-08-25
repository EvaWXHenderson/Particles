import random as rand
import math

particles = [] #list of particle objects
p_positions = [] #list of particle positions - updated using position_update() - needs cleared before calling function
p_velocities = [] #list of particle velocities - updated using velocity_update() - needs cleared before calling function

delt_t = 0.1 #change in time (seconds)
K_energy_sys = 0 # (Kg(A/s)^2) - goal to be in joules (Kg(m/s)^2)
T_sys = 0 #Kelvin - currently not accurate
total_force_sys = 0 #Newtons
pressure = 0 
#radius = 3 #(angstroms) #for collisions with other particles acting more as objects/balls where repuslions and attractions not considered

cycle = 0

Particle_info = {"H" : [1.67*10**(-27)],
                 "He" : [6.646*10**(-27)],
                 "Cl" : [10**(-25)]}
class Particle:
    def __init__(self, mass, sigma, epsilon):
        position_x = rand.randint(1, 100)
        position_y = rand.randint(1, 100)
        self.position = (position_x, position_y)

        p_positions.append(self.position)

        self.mass = mass #mass hydrogen (kg)
        self.velocity = (rand.randint(-4, 4), rand.randint(-4, 4)) #velocity (A/delt_t)

        p_velocities.append(self.velocity)

        self.acceleration = (0,0)

        self.potentials = (0,0) #Joules

        self.F_x = 0
        self.F_y = 0
        self.forces = [] #Newtons
        self.total_force_p = 0
        self.forces_print = (0,0) #only needed if trying to check force values
        self.accelerations_print = [] #only needed if trying to check all acceleration values

        self.distances_x = []
        self.distances_y = []

        self.sigma = sigma #(angstroms(A))
        self.epsilon = epsilon #Joules

        self.K_energy = 0

        particles.append(self)

    def position_update(self, t = delt_t):
        self.new_x = self.position[0] + self.velocity[0] * t
        self.new_y = self.position[1] + self.velocity[1] * t
        
        self.position = (self.new_x, self.new_y)
        p_positions.append(self.position)

    def collision_particle(self):
        global particles, radius

        for particle2 in particles:
            if self != particle2:

                dx = self.position[0] - particle2.position[0]
                dy = self.position[1] - particle2.position[1]
                
                distance = (math.sqrt((dx**2)+(dy**2)))

                if distance <= radius:
                    self.velocity = (-(self.velocity[0]), -(self.velocity[1]))
                    particle2.velocity = (-(particle2.velocity[0]), -(particle2.velocity[1]))
    
    def collision_box(self):
        new_velocity_x = (-(self.velocity[0]), (self.velocity[1]))
        new_velocity_y = ((self.velocity[0]), -(self.velocity[1]))

        if self.new_x > 100:
            self.position = (100, self.position[1])
            self.velocity = new_velocity_x

        if self.new_x < 0:
            self.position = (0, self.position[1])
            self.velocity = new_velocity_x

        if self.new_y > 100 or self.new_y < 0:
            self.position = (self.position[0], 100)
            self.velocity = new_velocity_y

        if self.new_y < 0:
            self.position = (self.position[0], 0)
            self.velocity = new_velocity_y           

    def lj_potential(self):
        for particle2 in particles:
            if self != particle2:
                dx = self.position[0] - particle2.position[0]
                dy = self.position[1] - particle2.position[1]
    
        V_x = 4*self.epsilon*(((self.sigma/dx)**12) - ((self.sigma/dx)**6))
        V_y = 4*self.epsilon*(((self.sigma/dy)**12) - ((self.sigma/dy)**6))

        self.potentials = (V_x, V_y)

    def lj_force(self):
        global particles, radius
        
        self.forces = []
        for particle2 in particles:
            if self != particle2:

                dx = self.position[0] - particle2.position[0]
                dy = self.position[1] - particle2.position[1]

                if dx == 0:
                    F_x = 0
                else:
                    F_x = self.epsilon*(2*(self.sigma**12/dx**13) - (self.sigma**6/dx**7)) # Lennard-Jones potential V(r)
                
                if dy == 0:
                    F_y = 0
                else:
                    F_y = self.epsilon*(2*(self.sigma**12/dy**13) - (self.sigma**6/dy**7))
                
                self.forces.append((F_x, F_y)) #newtons

        self.F_x = 0
        self.F_y = 0

        for value in self.forces:
            self.F_x += value[0]
            self.F_y += value[1]

        self.forces_print = (self.F_x, self.F_y) #only needed if trying to check force values
            
    def acceleration_calc(self):
        a_x = self.F_x/self.mass
        a_y = self.F_y/self.mass
        self.acceleration = (a_x, a_y) #(N/kg)

        """acceleration cap to avoid knock-on teleporting errors: """
        if self.acceleration[0] > 10:
            self.acceleration = (10, a_y)
        if self.acceleration[0] < -10:
            self.acceleration = (-10, a_y)

        if self.acceleration[1] > 10:
            self.acceleration = (a_x, 10)
        if self.acceleration[1] < -10:
            self.acceleration = (a_x, -10)

        #self.accelerations.append(self.acceleration_print) #only needed if trying to check all acceleration values
       
    def change_velocity(self, t = delt_t):
        new_velocity_x = self.velocity[0] + (self.acceleration[0] * t)
        new_velocity_y = self.velocity[1] + (self.acceleration[1] * t)

        if new_velocity_x > 10:
            new_velocity_x = 10
        if new_velocity_x < -10:
            new_velocity_x = -10

        if new_velocity_y > 10:
            new_velocity_y = 10
        if new_velocity_y  < -10:
            new_velocity_y  = -10
        
        self.velocity = (new_velocity_x, new_velocity_y) # velocity in A/0.1seconds
        p_velocities.append(self.velocity)

    def kinetic_energy_p(self):
        speed = math.sqrt((self.velocity[0]*10)**2 + (self.velocity[1]*10)**2) #velocities multiplied by 10 to get into angstroms per second?

        self.K_energy = (1/2)*(self.mass)*(speed**2)

"""    def force_p(self):
        self.total_force_p = math.sqrt((self.F_x**2) + (self.F_y**2))
        print("total_force_p" + str(self.total_force_p)) #Newtons"""





def create_particles(mass_p, sigma_p, epsilon_p, number = 15):
    for particles in range(number):
        Particle(mass_p, sigma_p, epsilon_p)

def kinetic_energy_sys():
    global K_energy_sys 

    K_energy_sys = 0

    for particle in particles:
        K_energy_sys += particle.K_energy #goal to be in joules (Kg(m/s)^2)

def temp_sys():
    global T_sys

    T_sys = ((2/3)*(K_energy_sys))/(1.38*10**(-23)) #currently not accurate

"""def force_sys():
    global total_force_sys

    for particle in particles:
        total_force_sys += particle.total_force_p
    print("total_force_sys: " + str(total_force_sys))

def pressure_sys(cycles):
    global pressure, total_force_sys, cycle

    average_force = (total_force_sys/cycles)
    #print("average_force: " + str(average_force))

    pressure = (average_force)/(100**(2)) #N/A^2
    #print("pressure: " + str(pressure))
    total_force_sys = 0 #N

    if pressure > 1000:
        print("Pressure exceeds 1000 N/A^2 with: " + str(pressure) + " on cycle: " + str(cycle))"""

    

def actions():
    global p_positions, p_velocities, particles, cycle

    cycle += 1

    p_positions = []
    p_velocities = []

    for particle in particles:
        particle.position_update() #appends new position to p_positions
    for particle in particles:
        particle.lj_potential() #only needed if trying to check potential values
    for particle in particles:
        particle.lj_force() #calculates forces (repulsive/attractive) for each particle in relation to all other particles
    for particle in particles:
        particle.acceleration_calc() #calculates the acceleration of a particle in response to inter-particle forces
    for particle in particles:
        particle.collision_box()
    for particle in particles:
        #particle.collision_particle() - SHOULDN'T BE NEEDED BECAUSE OF LENNARD-JONES POTENTIAL CONSIDERATION??? - SHOULD HAVE REPULSION ALREADY AT 3A???
        particle.change_velocity() #calculates new velocities based on the updated acceleration

    if cycle%10 == 0:
        for particle in particles:
            particle.kinetic_energy_p()
            #particle.force_p()           
        
        kinetic_energy_sys()
        temp_sys()
        #force_sys()
        #pressure_sys(1)

        