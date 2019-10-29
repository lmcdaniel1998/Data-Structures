def perm_gen_lex(a):
    """Recursive function that returns all permutations of the input string in lexicographic order"""
    perm_list = []
    perm = individual_permutation(a)
    for one_perm in perm:
        perm_list.append(''.join(one_perm))
    return perm_list


def individual_permutation(string):
    my_perm = []            # list of a single permutation
    if len(string) == 0:
        return []
    if len(string) == 1:            # stops permutation when remanding string reaches 1 or starts at 0
        return [string]

    for first_char in string:            # first character for comparison
        remainder = []          # where remainder characters are stored

        for second_char in string:            # second character for comparison
            if second_char != first_char:
                remainder.append(second_char)         # if second_char isn't first_char add second_char to remainder

        for remainder_char in individual_permutation(remainder):         # recursive four loop on remainder characters
            my_perm.append([first_char] + remainder_char)

    return my_perm
