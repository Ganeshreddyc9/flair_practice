# data = [1,1,2,3,4,5,1,12,1,2,1,1,2]
# remove duplicates without using set? Try with and without a temporary list?

# data = [1,1,2,3,4,5,1,12,1,2,1,1,2]

# res = []
# for i in data:
#
#     if i not in res:
#         res.append(i)
#     # else:
#
#
# print(res)

data = [1,1,2,3,4,5,1,12,1,2,1,1,2]


# index = 0
# while index <len(data):
#     current_index = data[index]
#     if data.count(current_index)>1:
#         data.pop(index)
#     else:
#         index +=1
# print(data)





data = [1,1,2,3,4,5,1,12,1,2,1,1,2]
i = 0

while i <len(data):
    c_v = i

    j = c_v +1

    while j <len(data):
        if data[c_v] == data[j]:
            data.pop(j)
        else:
            j +=1
    i += 1
print(data)


