"""
This script allows the user to select a Hillclimbing algorithm or a Gradient Ascent algorithm. This is then followed by
asking the user what kind of land scape they would like to model.
"""
from GradientAscent import GradientAscent
from HillClimbing import HillClimbing

""" Setup """
# Ask user what landscape and model to use
landscapeType = input('What kind of landscape do you want? Simple or Complex?').lower()
model = input('What optimization model do you want to use: Gradient Ascent or Hillclimbing').lower()

# set range of values and learning rate
bottomRange, topRange = -2, 2
learning_rate = 0.01  # 0.01 for hillclimbing and 0.01 for gradient ascent

# start point grid

"""Run models """
if model == 'gradient ascent':
    result = GradientAscent(bottomRange, topRange, landscapeType, learning_rate) # need to comment out start for some runs
elif model == 'hillclimbing':
    result = HillClimbing(bottomRange, topRange, landscapeType, learning_rate)
else:
    raise ValueError('There is no model of this type')



