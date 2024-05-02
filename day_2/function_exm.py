
def add(a,b,*args):

    return a+b
a = add(1,2)
print(a)


def outer_function(x):
    def inner_function(y):
        result = x + y
        return result  # This is where the return statement is used

    return inner_function  # The outer function returns the inner function

# Example usage:
add_five = outer_function(5)
result_value = outer_function(3)
print(result_value)  # Output: 8