t = (1,2,1,2,3,5,4,6,6,5)

result = ()

for i in t:
    if i not in result:
        result += (i,)
print(result)