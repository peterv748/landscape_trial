import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm

matplotlib.use("Qt5Agg")

def plot_landscape(image_temp, elapsed_time):
    """
    plotting the calculated fractal landscape and writing it to file
    """
    
    plt.imshow(image_temp, interpolation='nearest', cmap=cm.gist_rainbow)
    plt.xlabel("fractal landscape generation time: {0}".format(elapsed_time))
    plt.ylabel("value")
    plt.title( "fractal landscape generation")
    plt.savefig("fractal_landscape.png")
    plt.show()
    plt.close()

if __name__ == "__main__":
    import numpy as np

    MAXIMUM_ITERATIONS = 300
    
    image = np.zeros([4096,4096])
   
    TIME_ELAPSED = 10
    plot_landscape(image,TIME_ELAPSED)
