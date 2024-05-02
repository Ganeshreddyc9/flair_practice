def sum_number(a,b):

    if a > b:
        a , b = b , a

    return sum(range(a, b+1))


print(sum_number(0,4))