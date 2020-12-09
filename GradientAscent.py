"""
This file contains code to run the Gradient Ascent algorithm. This is split in to two main parts which uses
the simple and complex landscapes
"""

from Functions import *
import numpy as np
import matplotlib.pyplot as plt

def GradientAscent(bottomRange, topRange, function, learning_rate, stopping):
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
        stop = 0
        diffx, diffy = 1, 1
        while diffx > 0.00009 or diffy > 0.00009:
            # calculate x and y gradients
            gradient = SimpleLandscapeGrad(x, y)

            # calculate new x and y positions
            newxy = np.array([x + learning_rate * gradient[0], y + learning_rate * gradient[1]])

            # check if in bounds
            newxy = np.maximum(newxy, [bottomRange, bottomRange])
            newxy = np.minimum(newxy, [topRange, topRange])

            # difference in x and y values from previous iteration
            diffx, diffy = abs(newxy[0] - x), abs(newxy[1] - y)
            print(diffx, diffy)
            # calculate difference between before and after positions then assign the new x and y value
            x, y = newxy[0], newxy[1]

            # show on graph
            z = SimpleLandscape(x, y)
            ax.scatter(x, y, z, marker="o", color="black")

            # update stop
            stop += 1
            if stop == stopping:
                print('Stoped due to going nowhere')
                break

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
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        xx, yy = np.meshgrid(np.arange(bottomRange, topRange, 0.1), np.arange(bottomRange, topRange, 0.1), sparse=False)
        z = ComplexLandscape(xx, yy)
        ax.plot_surface(xx, yy, z, cmap='RdBu')
        # plt.show()

        """ Pick start position """
        # create random start point
        x, y = np.random.uniform(bottomRange, topRange), np.random.uniform(bottomRange, topRange)
        z = ComplexLandscape(x, y)
        ax.scatter(x, y, z, marker="o", color="black")
        plt.xlabel('x'), plt.ylabel('y')
        plt.show()

        """ initialize first step """
        gradient = ComplexLandscapeGrad(x, y)

        # calculate new x and y positions
        newxy = np.array([x + learning_rate * gradient[0], y + learning_rate * gradient[1]])

        # check if in bounds
        newxy = np.maximum(newxy, [bottomRange, bottomRange])
        newxy = np.minimum(newxy, [topRange, topRange])

        # calculate difference between before and after positions then assign the new x and y value
        x, y = newxy[0], newxy[1]

        # show on graph
        z = ComplexLandscape(x, y)
        ax.scatter(x, y, z, marker="o", color="black")

        diffx, diffy = 1, 1

        """ run through untill max is found """
        while diffx > 0 or diffy > 0:
            # calculate x and y gradients
            gradient = ComplexLandscapeGrad(x, y)

            # calculate new x and y positions
            newxy = np.array([x + learning_rate * gradient[0], y + learning_rate * gradient[1]])

            # check if in bounds
            newxy = np.maximum(newxy, [bottomRange, bottomRange])
            newxy = np.minimum(newxy, [topRange, topRange])

            # calculate diffx and diffy
            diffx, diffy = abs(newxy[0] - x), abs(newxy[1] - y)
            print('diffx', diffx, 'diffy', diffy)
            # calculate difference between before and after positions then assign the new x and y value
            x, y = newxy[0], newxy[1]

            # show on graph
            z = ComplexLandscape(x, y)
            ax.scatter(x, y, z, marker="o", color="black")

        """ Present finishing position """
        print('The maximum is at: x =', x, ' y =', y, 'z =', z,)
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
