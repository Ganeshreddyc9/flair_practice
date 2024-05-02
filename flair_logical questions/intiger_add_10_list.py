#  data = ["a","b","c",3,4,5]
# If it is integer add 10 and print all those values in list
# o/p -- ["a","b","c",13,14,15].

data = ["a","b","c",3,4,5]


result = []
for i in data:
    result.append(i+10 if isinstance(i,int) else i)

print(result)

