"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO: define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(time):
    '''this function takes in time as an argument and subtract it from the total time it takes to give out the remaining time'''
    return EXPECTED_BAKE_TIME - time
    



#TODO: Define the 'preparation_time_in_minutes()' function below.
# To avoid the use of magic numbers (see: https://en.wikipedia.org/wiki/Magic_number_(programming)), you should define a PREPARATION_TIME constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations, and make changes to your code.
def preparation_time_in_minutes(num):
    '''takes in the num of layers as an argument and gives out the time needed'''
    return num * PREPARATION_TIME



#TODO: define the 'elapsed_time_in_minutes()' function below.
def elapsed_time_in_minutes(layers, time):
    """ takes the layers and time elapsed to give out the total timed elapsed"""
    return (layers * 2) + time



# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
