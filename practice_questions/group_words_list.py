# Write a program to group words from a list.
# data = ['ashok', 'hari', 'bhanu', 'anil', 'bharath', 'anvesh', 'uday','raja']
# result = {'a': ['ashok', 'anil', 'anvesh'],
# 'b': ['bhanu', 'bharath'],
# 'h': ['hari'],
# 'u': ['uday'],
# 'r': ['raja']
# }


data = ['ashok', 'hari', 'bhanu', 'anil', 'bharath', 'anvesh', 'uday','raja','ganesh']

result = {}
for i in data:
    # print(i[0])
    if i[0] in result:
        result[i[0]].append(i)
    else:
        result[i[0]] = [i]
print(result)
