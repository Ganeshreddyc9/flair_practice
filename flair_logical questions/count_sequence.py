# s = "i am in bangalore"
# Count how many times letters are repeated in above string
# O/P -- i = 2,a = 2,m=1,n=2,b=1,g=1,l=1,o=1,r=1,e=1


# na method evry time i do this method 
s = "i am in bangalore"

resut = {}
for i in s:

    if i not in resut:
        resut[i] =1
    else:
        resut[i] += 1
print(resut)


# sir method

result = {}

for i in s:
    result[i] = result.get(i,0) +1

print(result)
# print(result.get(i,0))

# inko method
res = {}

for i in s:
    res[i]= res.setdefault(i,0)+1

print(res)
