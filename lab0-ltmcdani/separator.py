import sys


def multi_line_input():
    input_list = []
    while True:
        try:
            input_line = input()
        except EOFError:
            break
        if input_line:
            input_list.append(input_line)
        else:
            break
    input_string = ' '.join(input_list)
    return input_string


def my_float(item):
    try:
        float(item)
        return True
    except ValueError:
        return False


def my_integer(item):
    try:
        int(item)
        return True
    except ValueError:
        return False


def only_numbers(the_input):
    num_list = []
    for i in range(0, len(the_input)):
        append_digit = my_float(the_input[i])
        if append_digit is False:
            return num_list
        num_list.append(the_input[i])
    return num_list


def integer_count(number_list, the_max):
    integer_list = []
    for number in number_list:
        if my_integer(number) is True:
            integer_list.append(number)
    return integer_list[0:the_max]


def float_count(number_list, the_max):
    float_list = []
    for number in number_list:
        if my_integer(number) is False:
            float_list.append(number)
    return float_list[0:the_max]


def main():
    max_nums = int(sys.argv[1])

    try:
        initial_string = multi_line_input()
        initial_list = initial_string.split(" ")

        try:
            nums_list = only_numbers(initial_list)

            try:

                print("Integers: " + ' '.join(integer_count(nums_list, max_nums)) + " \nFloats: " + ' '.join(float_count(nums_list, max_nums)))

            except ValueError:
                print("Values not an integers or floats")

        except TypeError:
            print("Value cannot be converted to float")

    except ValueError:
        print("Wrong value please only enter numbers")


if __name__ == '__main__':
    main()
