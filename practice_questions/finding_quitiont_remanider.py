# find quituiont and remainder with out using % anf //


def remainder(dividend,divisor): #15 , 3 

    # quitiont = 0
    while dividend >=divisor:

        dividend -= divisor

    return dividend


result = remainder(15,3)

print(result)

result = remainder(15,4)

print(result)