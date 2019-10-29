
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    # check for NoneType
    if int_list is None:
        raise ValueError("Do not enter NoneType value")
    # check if int_list is empty
    elif len(int_list) == 0:
        return None
    # check if list is only one integer
    elif len(int_list) == 1:
        return int_list[0]
    else:
        max_value = 0
        return recursive_list(int_list, max_value)
        '''# establish initial max_val
        max_val = int_list[0]
        # for loop through int_list to find max value
        for i in range(0, len(int_list)):
            if int_list[i] > max_val:
                max_val = int_list[i]
        return max_val'''


def recursive_list(int_list, max_value):
    if int_list[max_value] > int_list[max_value + 1]:
        return int_list[max_value]
    return recursive_list(int_list, max_value + 1)


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    # check for NoneType
    if int_list is None:
        raise ValueError("Do not enter NoneType value")
    reverse_list = []
    current = len(int_list) - 1
    # check if list is empty
    if len(int_list) == 0:
        return None
    # check if lis is only one integer
    elif len(int_list) == 1:
        return [int_list[0]]
    # recursive loop through int_list reversing values into reverse_list
    if current >= 0:
        return [int_list[current]] + reverse_rec(int_list[0:current])
    return reverse_list


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    # check for NoneType
    if int_list is None:
        raise ValueError("Do not enter NoneType value")
    # check if list is empty
    elif len(int_list) == 0:
        return None
    # return None if target is not found in int_list
    elif low == high and target != int_list[low]:
        return None

    # middle value equation
    middle = (low + high)//2

    # middle value less than target
    if int_list[middle] < target:
        low = middle + 1
        return bin_search(target, low, high, int_list)
    # middle value greater than target
    elif int_list[middle] > target:
        high = middle - 1
        return bin_search(target, low, high, int_list)
    return middle
