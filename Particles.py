import random as rand
import math

particles = [] #list of particle objects
p_positions = [] #list of particle positions - updated using position_update() - needs cleared before calling function
p_velocities = [] #list of particle velocities - updated using velocity_update() - needs cleared before calling function

delt_t = 0.1 #change in time (seconds)
radius = 3

Particle_info = {"H" : (1.008, 1930),
                 "He" : (4, 1352),
                 "Cl" : (35.453, 0.32104 )}

class Particle:
    def __init__(self):
        position_x = rand.randint(1, 100)
        position_y = rand.randint(1, 100)
        self.position = (position_x, position_y)

        p_positions.append(self.position)

        self.mass = 1.008 #mass hydrogen (amu)
        self.velocity = (rand.randint(-4, 4), rand.randint(-4, 4)) #RMS velocity (m/delt_t)

        p_velocities.append(self.velocity)

        self.acceleration = ""
        self.velocity_damp = ""

        particles.append(self)

    def position_update(self, t = delt_t):
        self.new_x = self.position[0] + self.velocity[0] * t
        self.new_y = self.position[1] + self.velocity[1] * t
        
        self.position = (self.new_x, self.new_y)
        p_positions.append(self.position)

    def collision(self):
        global particles, radius

        for particle2 in particles:
            if self != particle2:

                dx = self.position[0] - particle2.position[0]
                dy = self.position[1] - particle2.position[1]
                distance = (math.sqrt((dx**2)+(dy**2)))

                if distance <= radius:
                    self.velocity = (-(self.velocity[0]), -(self.velocity[1]))
                    particle2.velocity = (-(particle2.velocity[0]), -(particle2.velocity[1]))
    
    def change_velocity(self):
        new_velocity = (-(self.velocity[0]), -(self.velocity[1]))

        if self.new_x > 100 or self.new_y > 100:
            self.velocity = new_velocity

        if self.new_x < 0 or self.new_y < 0:
            self.velocity = new_velocity

    def velocity_update(self, t = delt_t):
        self.new_velocity = self.velocity + (self.acceleration * t)
        
        self.velocity = self.new_velocity
        p_velocities.append(self.velocity)

def create_particles(number = 15):
    for particles in range(number):
        Particle()

def actions():
    global p_positions, p_velocities, particles

    p_positions = []
    p_velocities = []

    for particle in particles:
        particle.position_update() #appends new position to p_positions
        particle.change_velocity()
        particle.collision()
        # particle.velocity_update() #appends new velocities to p_velocities
