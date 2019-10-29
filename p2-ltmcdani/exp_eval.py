from stack_array import Stack


# You do not need to change this class
class PostfixFormatException(Exception):
    pass


def postfix_eval(input_str):
    """Evaluates a postfix expression"""

    """Input argument:  a string containing a postfix expression where tokens 
    are space separated.  Tokens are either operators + - * / ^ or numbers
    Returns the result of the expression evaluation. 
    Raises an PostfixFormatException if the input is not well-formed"""
    my_stack = Stack(30)
    input_list = input_str.split()

    for token in input_list:         # loop through postfix string
        if is_valid_token(token) is True:
            if my_is_digit(token) is True:
                my_stack.push(float(token))

            elif token == "+":          # addition
                if my_stack.num_items >= 2:
                    second_val = my_stack.pop()
                    first_val = my_stack.pop()
                    result_val = first_val + second_val
                    my_stack.push(result_val)
                else:
                    raise PostfixFormatException("Insufficient operands")
            elif token == "-":          # subtraction
                if my_stack.num_items >= 2:
                    second_val = my_stack.pop()
                    first_val = my_stack.pop()
                    result_val = first_val - second_val
                    my_stack.push(result_val)
                else:
                    raise PostfixFormatException("Insufficient operands")
            elif token == "*":          # multiplication
                if my_stack.num_items >= 2:
                    second_val = my_stack.pop()
                    first_val = my_stack.pop()
                    result_val = first_val * second_val
                    my_stack.push(result_val)
                else:
                    raise PostfixFormatException("Insufficient operands")
            elif token == "/":          # division
                if my_stack.num_items >= 2:
                    second_val = my_stack.pop()
                    if second_val == 0:
                        raise ValueError("Cannot divide by 0")
                    first_val = my_stack.pop()
                    result_val = first_val / second_val
                    my_stack.push(result_val)
                else:
                    raise PostfixFormatException("Insufficient operands")
            elif token == "^":          # exponent
                if my_stack.num_items >= 2:
                    second_val = my_stack.pop()
                    first_val = my_stack.pop()
                    result_val = first_val ** second_val
                    my_stack.push(result_val)
                else:
                    raise PostfixFormatException("Insufficient operands")
        else:
            raise PostfixFormatException("Invalid token")
    if my_stack.num_items == 1:         # there should only be one element in stack when all operations are done
                return my_stack.pop()
    else:
        raise PostfixFormatException("Too many operands")


def my_is_digit(n):         # checks of token is a operator or digit
    try:
        float(n)
        return True
    except ValueError:
        return False


def my_is_operator(my_token):           # checks if token is operator
    allowed_operators = set('^*/+- ')
    if my_token in allowed_operators:
        return True
    else:
        return False


def is_valid_token(my_token):           # checks if token is anything else besides operator or operand
    if my_is_digit(my_token) or my_is_operator(my_token) is True:
        return True


def infix_to_postfix(input_str):
    """Converts an infix expression to an equivalent postfix expression"""

    """Input argument:  a string containing an infix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression """
    my_stack = Stack(30)            # initialize stack
    input_list = input_str.split()
    rpn_expression = ""
    if len(input_list) == 1:            # if length is 1 just return token
            rpn_expression = input_str
            return rpn_expression
    for token in input_list:
        if my_is_digit(token) is True:          # if token is a operand append to rpn expression
            rpn_expression += token + " "
        else:
            if token == "(":            # if token is ( push to stack
                my_stack.push("(")

            elif token == ")":          # if token is ) remove items from stack until (
                next_operator = my_stack.peek()
                while next_operator != "(":
                    rpn_expression += my_stack.pop() + " "
                    next_operator = my_stack.peek()
                my_stack.pop()

            else:
                if my_is_operator(token) is True:
                    # order of operations while statement
                    while (my_stack.is_empty() is False) and (my_is_operator(my_stack.peek()) is True) and (order_of_operations(my_stack, token) is True):
                        rpn_expression += my_stack.pop() + " "
                    my_stack.push(token)

    for operators in range(0, my_stack.num_items):          # move rest of operators from stack to rpn expression
        if my_is_operator(my_stack.peek()) is True:
            rpn_expression += my_stack.pop()
    return rpn_expression


def operator_hierarchy(operator):
    # first number represents precedence second number represents associativity
    if operator == "^":
        hierarchy = [2, 1]
    elif operator == "*":
        hierarchy = [1, 0]
    elif operator == "/":
        hierarchy = [1, 0]
    elif operator == "+":
        hierarchy = [0, 0]
    else:
        hierarchy = [0, 0]
    return hierarchy


def order_of_operations(stack, o1):
    o1_hierarchy = operator_hierarchy(o1)
    o2_hierarchy = operator_hierarchy(stack.peek())
    if (o1_hierarchy[1] == 0) and (o1_hierarchy[0] <= o2_hierarchy[0]):
        return True
    elif (o1_hierarchy[1] == 1) and (o1_hierarchy[0] < o2_hierarchy[0]):
        return True
    else:
        return False


def prefix_to_postfix(input_str):
    """Converts a prefix expression to an equivalent postfix expression"""
    """Input argument: a string containing a prefix expression where tokens are 
    space separated.  Tokens are either operators + - * / ^ parentheses ( ) or numbers
    Returns a String containing a postfix expression(tokens are space separated)"""
    my_stack = Stack(30)            # initialize stack
    input_list = input_str.split()
    reversed_list = input_list[::-1]            # reverses expression

    for token in reversed_list:
        if my_is_digit(token) is True:          # add operands to stack
            my_stack.push(token)

        elif my_is_operator(token) is True:         # removes tokens from stack and adds them if operator is encountered
            op1 = my_stack.pop()
            op2 = my_stack.pop()
            new_str = op1 + ' ' + op2 + ' ' + token         # adds tokens and operator to stack
            my_stack.push(new_str)

    return my_stack.pop()
