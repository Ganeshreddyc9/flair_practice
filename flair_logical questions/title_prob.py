S = "I am in hyderabad"
# Result = "I Am In Hyderabad".
# Do this without using title ()

# print(S.title())

for word in S.split():
    
    print(word.title(),end=" ")
    


  
# print(dir(S))
    
res = ""
for word in S.split():
    
    # print(i.title(),end=" ")
    res += word[0].upper()+ word[1:]+" "
print(res)


s = "I am in bangalore"
# Count how many times letters are repeated in above string
# O/P -- I = 2,a = 2,m=1,n=2,b=1,g=1,l=1,o=1,r=1,e=1

# res={}

# for i in s:
#     res[i] = res.get(i,0)+1
# print(res,"dict...")
