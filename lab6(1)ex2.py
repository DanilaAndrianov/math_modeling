import matplotlib.pyplot as plt
import numpy as np
def parabola_plotter(a=1, b=1, c=0, title="график"):
    x = np.arange(-10, 10, 0.125)
    y = a*(x**2)+b*x+c
    plt.plot(x, y,color='c',label="График парабола")
    plt.xlabel('Ось x')
    plt.ylabel('Ось y')
    plt.title(title)
    plt.legend()
    plt.show
parabola_plotter()


def giperbola_plotter(k=1,title='график'):
    x_min = -30
    x_max = 30
    x=np.arange(x_min, x_max, 0.125)
    y=k/x
    y = np.ma.masked_less(y, x_min)
    y = np.ma.masked_greater(y, x_max)
    plt.plot(x, y,color='r',label="График гипербола")
    plt.xlabel('Ось x')
    plt.ylabel('Ось y')
    plt.title(title)
    plt.grid()
    plt.legend()
    plt.show
giperbola_plotter()
    
        
    