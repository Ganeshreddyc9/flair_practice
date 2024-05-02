# find division with out using //


def division(dividend,divisor):

    quitiont = 0

    while dividend >=divisor:

        dividend -=divisor
        quitiont +=1
    return quitiont

result = division(15,3)
print(result)

result = division(15,4)
print(result)

result = division(15,2)
print(result)
