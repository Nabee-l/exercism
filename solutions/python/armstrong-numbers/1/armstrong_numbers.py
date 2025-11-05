def is_armstrong_number(number):
    length = len(str(number))
    num = number
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit**length
        number = number // 10
    if sum == num:
        return True
    return False