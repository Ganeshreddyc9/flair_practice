# s = "i am in bangalore"
# # Count only vowels (a,e,i,o,u)how many times repeated.

s = "i am in bangalore"
result = {}

for i in s:
    if i in "aeiou":
        result[i] = result.get(i,0)+1
print(result)


# inko method 

result = dict.fromkeys('aeiou',0)


for i in s:
    if i in result:
        result[i] +=1

print(result)