# input1=[1,2,3]
# input2=[4,5,6,7]
# out=[14,15,16,17,24,25,26,27,34,35,36,37]

input1=[1,2,3]
input2=[4,5,6,7]

# print(list(zip(input1,input2)))
result = []

for i in range(len(input1)):
    for j in range(len(input2)):

        result.append(str(input1[i])+str(input2[j]))
print(result)



out = [a + b for a in input1 for b in input2]
print(out)