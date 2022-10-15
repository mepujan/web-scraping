def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_upper = func.upper()
        return make_upper
    return wrapper

@uppercase_decorator
def greeting():
    return "Hello Good morning"

print(greeting())
# decorate = uppercase_decorator(greeting)
# print(decorate())
