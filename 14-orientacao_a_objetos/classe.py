"""
Name: Class_euclidean_distances.
Author: CPSdeFarias
"""

from math import sqrt
import matplotlib.pyplot as plt
import numpy as np


class Distance:
    """
    Methods:
    ---------------------
    display_points()
    calculate_distance()
    plot_vetores2D()
    """

    def __init__(self, x0, y0, x1, y1):
        """
        Calculates the euclidean distances between two points and
        draw the corresponding vectors

        Parameters
        ----------
        x0 : float
            x coordinate of the first point
        y0: float
            y coordinate of the first point
        x1 : float
            x coordinate of the first point
        y1: float
            y coordinate of the first point
        """
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.ry = self.y1 - self.y0
        self.rx = self.x1 - self.x0

    def display_points(self):
        print(f'Ponto inicial: ({self.x0},{self.y0})')
        print(f'Ponto final: ({self.x1},{self.y1})')

    def calculate_distance(self):
        return sqrt(self.rx ** 2 + self.ry ** 2)

    def plot_vetores2d(self):
        plt.quiver([0, 0, self.x0], [0, 0, self.y0], [self.x0, self.x1, self.rx],
                   [self.y0, self.y1, self.ry], angles='xy', scale_units='xy', color=['r', 'g', 'b'], scale=1)

        m = np.array([[self.x0, self.y0],
                      [self.x1, self.y1],
                      [self.rx, self.ry]])

        maxes = 1.1 * np.amax(abs(m), axis=0)
        plt.xlim([-maxes[0], maxes[0]])  # set the x axis limits
        plt.ylim([-maxes[1], maxes[1]])  # set the y axis limits
        plt.grid(b=True, which='major')
        plt.show()


# A linha abaixo só será executada se o script classe.py for executado como main
if __name__ == '__main__':
    ponto = Distance(-2.0, -1.0, 1.0, 2.0)
    ponto.display_points()
    print(ponto.calculate_distance())
    ponto.plot_vetores2d()
else:
    print('O módulo Points foi importado com sucesso!')
