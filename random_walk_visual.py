from random_walk import RandomWalk

import matplotlib.pyplot as plt

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()

    # set plotting window size
    plt.figure(dpi =128, figsize=(8, 5))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth = 1, c = 'purple')
    
    plt.show()
    
    keep_running = input("Make another walk?(y/n)")
    if keep_running == 'n':
        break




