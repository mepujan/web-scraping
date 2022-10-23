from stack import Stack
def decimal_to_binary(decimal):
    stack = Stack()
    while decimal > 0:
        remainder = decimal % 2
        stack.push(remainder)
        decimal //= 2
    binary_string = ""
    while not stack.is_empty():
        binary_string += str(stack.pop())
    return binary_string

print(decimal_to_binary(100))


