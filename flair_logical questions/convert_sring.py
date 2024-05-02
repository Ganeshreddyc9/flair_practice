# convert string to this 
#  e_op = "ivar si a doog yob"

s = "ravi is a good boy"

word = s.split(" ")
# print(word)

res = ""
for char in word:
    res += char[::-1] +" "
print("".join(res))
print(res.strip())


# print(" ".join(res))