def multi_bracket_validation(string):
    """
    This function will check to see if the brackets are matching. It creates
    an empty list, which is our stack and we will iterate through each
    character. 

    Any opening brackets will be appended to our stack. 
    
    When it encounters a closing bracket, it will check if the stack is empty and 
    will return false if it is. 
    
    If the stack is not empty, it will pop the last element and it will 
    compare to the closing bracket.
    It will return false it doesn't match right away. Once we are done
    iterating, it checks the length again and return the appropriate Boolean
    """
    stack = []

    for char in string:
        print(char)
        if char == '{' or char == '(' or char == '[':
            stack.append(char)
        elif char == '}' or char == ')' or char == ']':

            if len(stack) == 0:
                return False

            top_of_stack = stack.pop()

            if not compare(top_of_stack, char):
                return False

    if len(stack) != 0:
        print('stack not empty...')
        return False

    print(stack)
    return True

def compare(opening, closing):
    """
    This function supplements our multi bracket validation.
    If the statement returns False, the function returns False.
    """
    if opening == '{' and closing == '}':
        return True
    if opening == '(' and closing == ')':
        return True
    if opening == '[' and closing == ']':
        return True
    return False

print(multi_bracket_validation('{(})'))