def is_prime(number):
    if number  <=1:
        return False
    elif number == 2:
        return True
    else:
        for y in range(2, int(number**0.5) + 1):
            if number % y == 0:
                return False
            return True
