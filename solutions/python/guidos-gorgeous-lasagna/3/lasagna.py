"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(time):
    '''this function takes in time as an argument and subtract it from the total time it takes to give out the remaining time'''
    return EXPECTED_BAKE_TIME - time
    
def preparation_time_in_minutes(num):
    '''takes in the num of layers as an argument and gives out the time needed'''
    return num * PREPARATION_TIME

def elapsed_time_in_minutes(layers, time):
    """ takes the layers and time elapsed to give out the total timed elapsed"""
    return (layers * 2) + time