s = "bangalore hyderabad chennai pune"
# Count how many times letters are repeated in each word .

# result = {}
# for chars in s.split():
    
#     if chars in result:
#         result[chars] +=1
#     else:
#         result[chars] =1
# print(result)

# or
# multiple lines 
# result = {}
# for chars in s.split():
#     result_1 = {}
#     for letters in chars:
#         if letters in result_1: # multiple lines
#             result_1[letters] += 1
#         else:
#             result_1[letters]=1
        
#     print(result_1)

# or
    
result = {}
for chars in s.split():
    result_1 = {}
    for letters in chars:
        result_1[letters] = result_1.get(letters,0) +1 # sinlge line
    result[chars] = result_1
    # print(result_1)
print(result)


