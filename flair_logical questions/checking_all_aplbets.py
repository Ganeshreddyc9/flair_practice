# (A pangram is a sentence that contains all the letters of the
# English alphabet at least once, for
# example: "The quick brown fox jumps over the lazy dog".)

import string
data = "The quick brown fox umps over the lazy dog"

for i in string.ascii_lowercase:
    if i not in data:
        print(f"alphabet {i} is missing")
        break
else:
    print("All alphabets are present")
