
# (A pangram is a sentence that contains all the letters of the English alphabet at least once, for
# example: "The quick brown fox jumps over the lazy dog".)

import string
data = "The quick brown fox jumps over the lazy dog"

print(string.ascii_lowercase)


for i in string.ascii_lowercase:
    if i not in data.lower():
        print(f"{i} alphabet is missing")
        break
else:
    print("All alphabets are preset")

