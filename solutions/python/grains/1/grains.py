def square(number):
    if 0 < number < 65:
        return 2**(number-1)
    raise ValueError("square must be between 1 and 64")


def total():
    grains = 0
    for grain in range(1,65):
        grains += square(grain)
    return grains
