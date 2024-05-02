# write a python program to create a dictionary, list element as key and frequency of element as value?

# l = [4, 7, 6, 7, 6, 7, 'a', 4, 'a', 'a', 5, 9, 2, 5, 9]

l = [4, 7, 6, 7, 6, 7, 'a', 4, 'a', 'a', 5, 9, 2, 5, 9]

result = {}
for i in l:

    result[i] = result.get(i,0)+1
print(result)