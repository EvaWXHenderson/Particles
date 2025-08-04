import matplotlib.pyplot as plt
import Particles as pcl

def initialise(particles = 15):
    pcl.create_particles(particles)
    
    for point in range(len(pcl.p_positions)):
        plt.scatter(pcl.p_positions[point][0], pcl.p_positions[point][1])
    
    plt.xticks([]) 
    plt.yticks([])