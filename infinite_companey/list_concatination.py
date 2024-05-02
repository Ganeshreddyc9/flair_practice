input1=[1,2,3]
input2=[4,5,6,7]
# out=[14,15,16,17,24,25,26,27,34,35,36,37]
# str_1 = ""
list_1 = []
for i in input1:
    # print(i)
    for j in input2:
        list_1.append(int(str(i)+str(j)))

print(list_1)

# print("".join(list(str_1)))

