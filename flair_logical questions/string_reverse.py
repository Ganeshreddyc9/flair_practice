
# 1 Write a program which give below inputs
# list2 ["who", "are", "you"]
#  o/p: "uoy era ohw

list2 =  ["who", "are", "you"]

data = list2[::-1]
print(data)
result = []
for i in data:
    result.append(i[::-1])
print(" ".join(result))