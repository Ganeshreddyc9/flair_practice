# enclosed

#
def outer():
    enclosed_val = 10

    def inner():
        # enclosed_val = 1
        print(enclosed_val)

    return inner()

out = outer()



