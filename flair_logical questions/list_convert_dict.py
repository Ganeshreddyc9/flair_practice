# list1=[324,45,5,34]
# # list2=[44,23,5,23]

# make it in dict as {324:44,45:23,34:23}


list1=[324,45,5,34]
list2=[44,23,5,23]

# print(dict(zip(list1,list2)))

result = {}
for i in range(len(list1)):

    result[list1[i]] = list2[i]

print(result)