"""
This file contains code to run the Hill Climbing algorithm. This is split in to two main parts which uses
the simple and complex landscapes
"""

from Functions import *
import numpy as np
import matplotlib.pyplot as plt
import random

def HillClimbing(bottomRange, topRange, function, learning_rate):
    """
    This function runs the gradient ascent algorithm using either the simple or complex landscape
    BottomRange = lower limit of function
    topRange = upper limit of function
    function = select what function type you want. simple or complex
    learning_rate = stepsize of itarations
    stopping = how many iterations until break
    """
    # Run simple landscape
    if function == 'simple':
        """ Create graph """
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        xx, yy = np.meshgrid(np.arange(bottomRange, topRange, 0.1), np.arange(bottomRange, topRange, 0.1), sparse=False)
        z = SimpleLandscape(xx, yy)
        ax.plot_surface(xx, yy, z, cmap='RdBu')

        """ Pick start position """
        # create random start point
        x, y = np.random.uniform(bottomRange, topRange), np.random.uniform(bottomRange, topRange)
        z = SimpleLandscape(x, y)
        ax.scatter(x, y, z, marker="o", color="black")
        plt.xlabel('x'), plt.ylabel('y')
        plt.show()

        """ Loop until condition is meet """
        diffx, diffy = 1, 1
        while diffx > 0.0001 or diffy > 0.0001:
            # calculate new x and y positions by selecting a random position which is higher than the current position
            a = True
            while a == True:
                newx = x + np.random.uniform(-learning_rate, learning_rate)
                newy = y + np.random.uniform(-learning_rate, learning_rate)
                newz = SimpleLandscape(newx, newy)

                if newz > z:
                    newxy = np.array([newx, newy])
                    z = newz
                    a = False

            # check if in bounds
            newxy = np.maximum(newxy, [bottomRange, bottomRange])
            newxy = np.minimum(newxy, [topRange, topRange])

            # difference in x and y values from previous iteration
            diffx, diffy = abs(newxy[0] - x), abs(newxy[1] - y)

            # calculate difference between before and after positions then assign the new x and y value
            x, y = newxy[0], newxy[1]
            # show on graph
            z = SimpleLandscape(x, y)

        print('The maximum is at: x =', x, ' y =', y, 'z =', z)
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        xx, yy = np.meshgrid(np.arange(bottomRange, topRange, 0.1), np.arange(bottomRange, topRange, 0.1), sparse=False)
        z = SimpleLandscape(xx, yy)
        ax.plot_surface(xx, yy, z, cmap='RdBu')
        z = SimpleLandscape(x, y)
        ax.scatter(x, y, z, marker="o", color="black")
        plt.xlabel('x'), plt.ylabel('y'), plt.title('Gradient ascent finishing position using complex landscape')
        plt.show()

    # run complex landscape
    elif function == 'complex':

        """ Create initial plot """
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        xx, yy = np.meshgrid(np.arange(bottomRange, topRange, 0.1), np.arange(bottomRange, topRange, 0.1), sparse=False)
        z = ComplexLandscape(xx, yy)
        ax.plot_surface(xx, yy, z, cmap='RdBu')

        """ Pick start position """
        # create random start point
        x, y = np.random.uniform(bottomRange, topRange), np.random.uniform(bottomRange, topRange)
        z = ComplexLandscape(x, y)
        ax.scatter(x, y, z, marker="o", color="black")
        plt.xlabel('x'), plt.ylabel('y')
        plt.show()

        """ Loop until condition is meet """
        diffx, diffy = 1, 1
        while diffx > 0.0001 or diffy > 0.0001:
            # calculate new x and y positions by selecting a random position which is higher than the current position
            a = True
            while a == True:
                newx = x + np.random.uniform(-learning_rate, learning_rate)
                newy = y + np.random.uniform(-learning_rate, learning_rate)
                newz = ComplexLandscape(newx, newy)

                if newz > z:
                    newxy = np.array([newx, newy])
                    z = newz
                    a = False

            # check if in bounds
            newxy = np.maximum(newxy, [bottomRange, bottomRange])
            newxy = np.minimum(newxy, [topRange, topRange])
            print(newxy)
            # difference in x and y values from previous iteration
            diffx, diffy = abs(newxy[0] - x), abs(newxy[1] - y)

            # calculate difference between before and after positions then assign the new x and y value
            x, y = newxy[0], newxy[1]

        print('The maximum is at: x =', x, ' y =', y, 'z =', z)
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        xx, yy = np.meshgrid(np.arange(bottomRange, topRange, 0.1), np.arange(bottomRange, topRange, 0.1), sparse=False)
        z = ComplexLandscape(xx, yy)
        ax.plot_surface(xx, yy, z, cmap='RdBu')
        z = ComplexLandscape(x, y)
        ax.scatter(x, y, z, marker="o", color="black")
        plt.xlabel('x'), plt.ylabel('y'), plt.title('Gradient ascent finishing position using complex landscape')
        plt.show()
    else:
        raise ValueError('No landscape of this type')