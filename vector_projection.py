import os
import numpy as np
import matplotlib.pyplot as plt
import imageio
import math


theta = range(0, 360, 5)
deg2rad = math.pi / 180

filenames = []
num = 0

for i in theta:
    num += 1
    
    x = math.cos(i*deg2rad)
    y = math.sin(i*deg2rad)

    plt.arrow(0, 0, x, y, width = 0.025, ec ='blue', fc = 'blue', length_includes_head = True)
    
    plt.text(x*1.3, y*1.3, 'a', fontsize=20, weight='bold')
    # x axis
    plt.arrow(0, 0, 1.4, 0, width = 0.03, ec ='green', fc = 'green', alpha = 0.2, length_includes_head = True)
    plt.text(1.5, 0, 'X', fontsize=20, weight='bold')
    # y axis
    plt.arrow(0, 0, 0, 1.4, width = 0.03, ec ='green', fc = 'green', alpha = 0.2, length_includes_head = True)
    plt.text(0, 1.5, 'Y', fontsize=20, weight='bold')
    # projection length on x axis
    plt.plot([0, x], [0, 0] ,color=(255/255, 0/255, 0/255))
    plt.plot([0, x], [y, y], linestyle='dashed', color = 'magenta', alpha = 0.5)
    # projection length on y axis
    plt.plot([0, 0], [0, y], color=(255/255, 0/255, 0/255))
    plt.plot([x, x], [0, y], linestyle='dashed', color = 'magenta', alpha = 0.5)
    plt.axis('square')
    plt.xlim(-2, 2)
    plt.ylim(-2, 2)

    
    filename = f'{num}.png'
    filenames.append(filename)
    plt.savefig(filename)
    plt.close()


with imageio.get_writer('vector_projection_demo.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)


for filename in set(filenames):
    os.remove(filename)
    
    
    
    
    
    
