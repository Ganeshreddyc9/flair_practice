data = ["a","b","c",3,4,5]
 # If it is an integer then add 10 to integer and print
 # O/p -- a,b,c,13,14,15
 # data = ["a","b","c",3,4,5]
 # If it is integer add 10 and print all those values in list
 # o/p -- ["a","b","c",13,14,15].

for i in data:
    if isinstance(i,int):
        print(i+10,end = ",")
    else:
        print(i,end=",")
    
# or
        

result = []

for i in data:
    result.append(i+10 if isinstance(i,int) else i)
print(result)