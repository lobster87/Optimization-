"""
This file contains functions for both Gradient Ascent and Hill Climbing algorithms
"""

import numpy as np
import matplotlib.pyplot as plt

def ComplexLandscape(x, y):
    return 4 * (1 - x) ** 2 * np.exp(-(x ** 2) - (y + 1) ** 2) - 15 * (x / 5 - x ** 3 - y ** 5) * np.exp(
        -x ** 2 - y ** 2) - (1. / 3) * np.exp(-(x + 1) ** 2 - y ** 2) - 1 * (
                       2 * (x - 3) ** 7 - 0.3 * (y - 4) ** 5 + (y - 3) ** 9) * np.exp(-(x - 3) ** 2 - (y - 3) ** 2)


# Definition of gradient of Complex landscape
def ComplexLandscapeGrad(x, y):
    g = np.zeros(2)
    g[0] = -8 * np.exp(-(x ** 2) - (y + 1) ** 2) * ((1 - x) + x * (1 - x) ** 2) - 15 * np.exp(-x ** 2 - y ** 2) * (
                (0.2 - 3 * x ** 2) - 2 * x * (x / 5 - x ** 3 - y ** 5)) + (2. / 3) * (x + 1) * np.exp(
        -(x + 1) ** 2 - y ** 2) - 1 * np.exp(-(x - 3) ** 2 - (y - 3) ** 2) * (
                       14 * (x - 3) ** 6 - 2 * (x - 3) * (2 * (x - 3) ** 7 - 0.3 * (y - 4) ** 5 + (y - 3) ** 9))
    g[1] = -8 * (y + 1) * (1 - x) ** 2 * np.exp(-(x ** 2) - (y + 1) ** 2) - 15 * np.exp(-x ** 2 - y ** 2) * (
                -5 * y ** 4 - 2 * y * (x / 5 - x ** 3 - y ** 5)) + (2. / 3) * y * np.exp(
        -(x + 1) ** 2 - y ** 2) - 1 * np.exp(-(x - 3) ** 2 - (y - 3) ** 2) * (
                       (-1.5 * (y - 4) ** 4 + 9 * (y - 3) ** 8) - 2 * (y - 3) * (
                           2 * (x - 3) ** 7 - 0.3 * (y - 4) ** 5 + (y - 3) ** 9))
    return g


# Definition of Simple landscape
def SimpleLandscape(x, y):
    return np.where(1 - np.abs(2 * x) > 0, 1 - np.abs(2 * x) + x + y, x + y)


# Definition of gradient of Simple landscape
def SimpleLandscapeGrad(x, y):
    g = np.zeros(2)
    if 1 - np.abs(2 * x) > 0:
        if x < 0:
            g[0] = 3
        elif x == 0:
            g[0] = 0
        else:
            g[0] = -1
    else:
        g[0] = 1
    g[1] = 1
    return g

def DrawSurface(fig, varxrange, varyrange, function):
    """Function to draw a surface given x,y ranges and a function."""
    ax = fig.gca(projection='3d')
    xx, yy = np.meshgrid(varxrange, varyrange, sparse=False)
    z = function(xx, yy)
    ax.plot_surface(xx, yy, z, cmap='RdBu') # color map can be adjusted, or removed!
    fig.canvas.draw()
    return ax