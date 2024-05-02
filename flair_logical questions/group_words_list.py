# Write a program to group words from a list.
data = ['ashok', 'hari', 'bhanu', 'anil', 'bharath', 'anvesh', 'uday','raja']
# result = {'a': ['ashok', 'anil', 'anvesh'],
# 'b': ['bhanu', 'bharath'],
# 'h': ['hari'],
# 'u': ['uday'],
# 'r': ['raja']
# }

data = ['ashok', 'hari', 'bhanu', 'anil', 'bharath', 'anvesh', 'uday','raja']

result = {}

for name in data:
    if name[0] in result:
        result[name[0]].append(name)
    else:
        result[name[0]]= [name]

print(result)


# inko_method

res = {}

for name in data:
    res[name[0]] = res.get(name[0],[])+[name]

print(res)