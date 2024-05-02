
# 13. Write a python program to all the occurances of number from a given list.
# l = [1,4,2,5,1,6,7,1,4,3,5,3,5,3,2,5,3,1,5,3] remove 3 output :[1,4,2,5,1,6,7,1,4,5,5,2,5,1,5]

l = [1,4,2,5,1,6,7,1,4,3,5,3,5,3,2,5,3,1,5,3]

result = []

for i in l:
    if i == 3:
        continue
    else:
        result.append(i)
print(result)

# list_comprehention

res = [i for i in l if i != 3 ]
print(res)
