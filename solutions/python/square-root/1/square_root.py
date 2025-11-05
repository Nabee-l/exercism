def square_root(number):
    if number == 1:
        return 1
    for num in range( number ):
        if num * num == number:
            return num