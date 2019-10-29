def bears(n):
    if n < 42:
        return False

    if n == 42:
        return True

    if n % 5 == 0:          # check if multiple of 5
        if n > 84:          # check if greater than 42
            return bears(n - 42)

    if (n % 2) == 0:          # check if n is even
        if n > 84:          # check if division by two will result in less than 42
            return bears(n // 2)

    if (n % 4) == 0:          # check if multiple by 4
        new_bear = n - ((n % 10) * second_to_last(n))
        if new_bear >= 42:          # check if bears greater than 42
            return bears(new_bear)

    if (n % 3) == 0:            # check if multiple of 3
        new_bear = n - ((n % 10) * second_to_last(n))
        if new_bear >= 42:          # check if bears greater than 42
            return bears(new_bear)

    return False


def second_to_last(number):
    last_two_string = number % 100          # get last two digits

    second_to_last_num = last_two_string // 10          # get second to last digit

    return second_to_last_num
