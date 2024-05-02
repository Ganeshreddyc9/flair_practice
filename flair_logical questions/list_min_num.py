# find the minimum no in array without in-built function:
# lsit_1=[2 8 9 -74 0 54]
list_1 = [2, 8, 9, -74, 0, 54]

print(min(list_1))


min_num = list_1[0]

for i in range(1,len(list_1)):
    if min_num > list_1[i]:
        min_num = list_1[i]
print(min_num)
