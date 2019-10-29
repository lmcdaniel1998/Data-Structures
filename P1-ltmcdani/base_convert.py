def convert(num, b):
    """Recursive function that returns a string representing num in the base b"""
    reverse_list = reverse_convert_list(num, b)

    forward_list = reverse_list[::-1]           # turns backward list forward

    base_gt_ten_list = base_gt_ten(forward_list)

    return ''.join(base_gt_ten_list)            # return converted value as a string


def reverse_convert_list(num, b):           # generates a backward non-hex list of base conversion
    quotient = num // b
    remainder = num % b
    if quotient == 0:           # recursive loop through num
        return [remainder]
    return [remainder] + reverse_convert_list(quotient, b)


def base_gt_ten(num_list):          # function that converts 10 - 15 to A - F
    new_list = []
    for i in num_list:
        if 0 <= i <= 9:
            new_list.append(str(i))
        if i == 10:
            new_list.append('A')
        elif i == 11:
            new_list.append('B')
        elif i == 12:
            new_list.append('C')
        elif i == 13:
            new_list.append('D')
        elif i == 14:
            new_list.append('E')
        elif i == 15:
            new_list.append('F')
        pass
    return new_list
