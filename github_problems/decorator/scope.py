# Scope: Scope refers to the visibility of variables within a program. In Python, variables have either global or local scope.

# Global Scope: Variables defined outside of any function have global scope and can be accessed from anywhere in the program.

# Local Scope: Variables defined within a function have local scope and can only be accessed within that function.

global_var = 'i can be accessed everywere'


def my_function():

    local_var = 'i can be accessed with in the func'

    print("global var:",global_var)
    print("local var",local_var)

result = my_function()

print(global_var)
print(local_var)

