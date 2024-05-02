


# count vowels

# result = {}

# for i in ["o", "m", "o", "m", "l", "p", "o"]:

#     result[i] = result.get(i,0)+1
# print(result)

# or

s = "i am in bangalore"

# result = {}
# for i in s:
#     if i in "aeiou":
#         result[i] = result.get(i,0)+1
# print(result)


# or

result = dict.fromkeys("aeiou",0)
print(result)
for i in s:
   
    if i in result:
        result[i] += 1
print(result)
