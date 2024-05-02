s = "I am in bangalore"
# Count only vowels (a,e,i,o,u)how many times repeated .

res = {}

for i in s:
    if i in "aeiou":
        # count +=1
        res[i] = res.get(i,0)+1
print(res)



result = dict.fromkeys("aeiou",0)
print(result)

for i in s:
    if i in result:
        result[i] +=1
print(result)