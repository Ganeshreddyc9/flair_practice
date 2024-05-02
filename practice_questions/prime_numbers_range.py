a = int(input("enter the start  number: "))
b = int(input("enter the  end number: "))


if a <= 1:
    print(a, "is not a prime number")
elif a > 1:

    for i in range(a,b//2):
        if a % i == 0:
            # print()
            break
    else:
        print(a, 'is a prime number')