def outer_function():
    outer_variable = "I'm outer!"

    def inner_function():

        print(outer_variable)
        inner_variable = "I am inner"
        print(inner_variable)

    inner_function()


outer_function()

# inner_function()