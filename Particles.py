import random as rand

particles = []
p_positions = []
p_velocities = []

delt_t = 0.001 #change in time (seconds)

Particle_info = {"H" : (1.008, 1930),
                 "He" : (4, 1352),
                 "Cl" : (35.453, 0.32104 )}

class Particle:
    def __init__(self):
        self.position_x = rand.randint(1, 100)
        self.position_y = rand.randint(1, 100)
        self.position = (self.position_x, self.position_y)

        p_positions.append((self.position_x, self.position_y))

        self.mass = 1.008 #mass hydrogen (amu)
        self.velocity = 1.93 #RMS velocity (m/delt_t)

        p_velocities.append(self.velocity)

        self.acceleration = ""
        self.velocity_damp = ""

        particles.append(self)

    def position_update(self, t = delt_t):
        self.new_x = self.position_x + self.velocity * t
        self.new_y = self.position_y + self.velocity * t
        
        self.position = (self.new_x, self.new_y)
        p_positions.append(self.position)

    def velocity_update(self, t = delt_t):
        self.new_velocity = self.velocity + (self.acceleration * t)
        
        self.velocity = self.new_velocity
        p_velocities.append(self.velocity)

def create_particles(number = 15):
    for particles in range(number):
        Particle()

def interval_actions():
    global particles

    p_positions = []
    p_velocities = []

    for particle in particles:
        particle.position_update() #appends new position to p_positions
        particle.velocity_update() #appends new velocities to p_velocities
