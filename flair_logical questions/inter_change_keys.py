#  Write a python function to interchange keys and values in a dictionary.
data = {'x': 1, 'y': 2, 'z': 3}
# result = {1: 'x', 2: 'y', 3: 'z'}
print(data)

res= {value:key for key,value in data.items()}
print(res)


print({ele[1]:ele[0] for ele in data.items()})
# for ele in data.items():
#     # print(ele[0],ele[1])
#     print(ele[1],ele[0])