# data = ["a","b","c",3,4,5]
# If it is an integer then add 10 to integer and print
# O/p -- a,b,c,13,14,15




# steps to do :

# read  cheyali --
# if that is a string --> ignore
# if that is int add 10 to it

# tried my self
# data = ["a","b","c",3,4,5]
# list_1 = []

# for num in data:
#     # print(num)
#
#
#     if type(num) is str:
#         list_1.append(num)
#     else:
#         # print(int,'value')
#         data = num+10
#         (list_1.append(data))
# print(list_1)

# chatgpt
# data =["a", "b", "c", 3, 4, 5]
# list_1 = []
#
# for item in data:
#     if isinstance(item, int):
#         list_1.append(item + 10)
#     else:
#         list_1.append(item)
#
# print(list_1)

# data =["a", "b", "c", 3, 4, 5]
# modified_data = []

# for item in data:

#     if not isinstance(item,int):
#         modified_data.append(str(item))
#     else:
#         modified_data.append(item+10)
# print(modified_data)
# result = ",".join(map(str, modified_data))
# print(result)


# expected o/p:# O/p -- a,b,c,13,14,15

data =["a", "b", "c", 3, 4, 5]


for i in data:
    if isinstance(i,int):
        print(i+10 , end = ",")
    else:
        print(i, end = ",")

print("\n")


# one more type

for i in data:

    print(i+10 if isinstance(i,int) else i, end =",")