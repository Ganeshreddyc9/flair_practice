
# enclosed_val

def outer():
    enclsoed_val = 10
    print("outer is executed")
    print(enclsoed_val,"inside outer")
    def inner():
        print(enclsoed_val)

        return outer()
outer()
