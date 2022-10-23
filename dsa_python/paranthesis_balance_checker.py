from faulthandler import is_enabled
from stack import Stack

def paranthesis_checker(paranthesis):
    stack = Stack()
    balanced = True
    index = 0
    symbols = {
        '(':')',
        '{':'}',
        '[':']'
    }

    while index < len(paranthesis) and balanced:
        symbol = paranthesis[index]
        if symbol in symbols.keys():
            stack.push(symbol)
        else:
            if stack.is_empty():
                balanced = False
            else:
                stack.pop()
        index += 1

    if balanced and stack.is_empty():
        return True
    return False

print(paranthesis_checker('({()}'))
