# 1.	Write a Python program to sum all the items in a list.


n=int(input("enter how many values u want plase in list:"))
list = list()

if n<=0:
    print("this is an empty list")
else:
    for i in range(1,n+1):
        val = int(input("enter {} value:".format(i)))
        list.append(val)
        sum = 0
        for i in list:
            sum +=i
            print(list)
            print("sum of all items in a list is {}".format(sum))