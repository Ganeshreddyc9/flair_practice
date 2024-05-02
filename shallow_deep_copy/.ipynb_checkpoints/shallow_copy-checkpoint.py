# shallow copy 

import copy

a = [[1,2],[3,4]]
b = copy.copy(a)

print(id(a),print(id(b)))



print("address of the internal elements",id(a[0]),id(b[0]))

a.append("hi")
print(a)

print(b)


a[0].append("hey i am updated")

print(a)
print(b)