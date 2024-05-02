

"""refer------------------kode ho...............mail for more detail"""







#  s = "i am in bangalore"
 # Count how many times letters are repeated in above string
 # O/P -- i = 2,a = 2,m=1,n=2,b=1,g=1,l=1,o=1,r=1,e=1

s = "i am in bangalore"
# result = {}
# for i in s:

#     result[i]= s.count(i)
# print(result)

# or 

# result = {}

# for i in s:

#     if i in result:
#         result[i] +=1
#     else:
#         result[i] = 1
# print(result)

# or

# result = {}

# for i in s:

#     result[i] = result.get(i,0)+1
# print(result)

# set default 

result = {}

for i in s:
    result [i]=result.setdefault(i,0)+1
print(result)

