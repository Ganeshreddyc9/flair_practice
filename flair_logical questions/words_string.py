
# problem 5
# Need words from a given string
# s = "how are you"
# result = ["how", "are", "you"], but don't use split'


s = "how are you"
# print(s.split())

words = []
word = ""
for i in s:
    if i == " ":
        words.append(word)
        word = ""
        # print(word,"if")
    else:
        word += i
    # print(words)
    # print(word)
else:
    if word:
        words.append(word)
print(words)