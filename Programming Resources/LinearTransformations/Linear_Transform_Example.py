import matplotlib.pyplot as plt
import numpy as np

from Transform import Transform

triangle = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 0, 0]])

def main():
    fig, (ax1, ax2) = plt.subplots(2, 2)
    axs = np.append(ax1, ax2)
    formatMainPlot(fig, axs)
    original(axs[0])
    scale(axs[1])
    rotate(axs[2])
    translate(axs[3])
    fig.tight_layout()
    plt.show()

def original(ax: plt.Axes):
    plot(ax, triangle, "orange")
    ax.set_title("Original")

def scale(ax: plt.Axes):
    plot(ax, triangle)
    T = Transform()
    T.scaleGlobal(2.5)
    A = T.transform(triangle)
    plot(ax, A, "new")
    ax.set_title("Scaled")

def rotate(ax: plt.Axes):
    plot(ax, triangle)
    T = Transform()
    T.rotateAroundZ(0.79)
    A = T.transform(triangle)
    plot(ax, A, "new")
    ax.set_title("Rotated")

def translate(ax: plt.Axes):
    plot(ax, triangle)
    T = Transform()
    T.translate(1.2, 1.2)
    A = T.transform(triangle)
    plot(ax, A, "new")
    ax.set_title("Translated")

''' PLOT FUNCTIONS '''
def plot(ax: plt.Axes, A: np.array, colortype: str='default'):
    x, y = (A[:, 0], A[:, 1])
    color = '#888B8D' if colortype == 'default' else '#F56600'
    ax.plot(x, y, lw=3, color=color)

def formatMainPlot(fig, axs: tuple):
    fig.suptitle("Demonstration of Linear Transformations")
    for ax in axs:
        ax.set_xlim((0, 3))
        ax.set_ylim((0, 3))
        ax.set_aspect('equal', adjustable='box')
        ax.set_yticks([1, 2, 3])
        ax.set_xticks([1, 2, 3])
    
if __name__ == '__main__':
    main()