# s = "bangalore hyderabad chennai pune"
# Count how many times letters are repeated in each word .
# {'bangalore': {'b': 1, 'a': 2, 'n': 1, 'g': 1, 'l': 1, 'o': 1, 'r': 1, 'e': 1}, 
#  'hyderabad': {'h': 1, 'y': 1, 'd': 2, 'e': 1, 'r': 1, 'a': 2, 'b': 1}, 'chennai': {'c': 1, 'h': 1, 'e': 1, 'n': 2, 'a': 1, 'i': 1}, 'pune': {'p': 1, 'u': 1, 'n': 1, 'e': 1}}
def wcount(s):
    result ={}
    for i in s:

        result[i] = result.get(i,0)+1
    # print(result)
    return result

s = "bangalore hyderabad chennai pune"

sen_result = {}

for chars in s.split():
    sen_result[chars] = wcount(chars)
print(sen_result)