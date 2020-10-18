import matplotlib.pyplot as plt
import matplotlib.animation as animation

def save_gif(training_progress_images, filename):
    fig = plt.figure()
    
    ims = []
    for i in range(len(training_progress_images)):
        im = plt.imshow(training_progress_images[i], animated=True, cmap="gray")
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=100, blit=True, repeat_delay=1000)
    
    ani.save(filename, writer="imagemagick")