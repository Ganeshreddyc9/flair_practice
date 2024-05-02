num = int(input("enter the number:"))


if num <= 1:
    print("enter the number greater than 1")
elif num > 1:
    flag = False
    for i in range(2,num):
        if num % i == 0:
            flag = True
            break
    if flag :
        print(num, "is not a prime number")
        
    else:
        print(num, "is  a prime number")
