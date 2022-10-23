from stack import Stack

def check_palindrome(strings):
    my_stack = Stack()
    reverse_str = ""
    for letters in strings:
        my_stack.push(letters)
    while not my_stack.is_empty():
        reverse_str += my_stack.pop()
    if strings == reverse_str:
        print("palindrome string")
    else:
        print("Not a palindrome")



check_palindrome("aba")