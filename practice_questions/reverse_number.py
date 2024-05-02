n = int(input("enter the number:"))
print("n value before reversing: %d" %n)

reverse = 0

while n !=0:

    print(reverse*10)
    reverse =reverse*10+ n%10

    
    n= n //10

print(reverse)