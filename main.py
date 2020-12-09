"""
This script allows the user to select a Hillclimbing algorithm or a Gradient Ascent algorithm. This is then followed by
asking the user what kind of land scape they would like to model.
"""
from GradientAscent import GradientAscent
from HillClimbing import HillClimbing
from hillclimbingTest import HillClimbingTest

""" Setup """
# Ask user what landscape and model to use
landscapeType = input('What kind of landscape do you want? Simple or Complex?').lower()
model = input('What optimization model do you want to use: Gradient Ascent or Hillclimbing?').lower()

# set range of values and learning rate
bottomRange, topRange = -2, 2
learning_rate = 0.01
stop = 1000

""" Run models """
if model == 'gradient ascent':
    GradientAscent(bottomRange, topRange, landscapeType, learning_rate, stop)
elif model == 'hillclimbing':
    HillClimbing(bottomRange, topRange, landscapeType, learning_rate, stop)
    #HillClimbingTest(bottomRange, topRange, landscapeType, learning_rate, stop)
else:
    raise ValueError('There is no model of this type')

