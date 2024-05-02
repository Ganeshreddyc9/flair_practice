# Write a Python program that accepts a hyphen separated sequence of
# words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
# Sample Items : green-red-yellow-black-white
# Expected Result : black-green-red-white-yellow

Sample_Item = "green-red-yellow-black-white"

colors_list = Sample_Item.split("-")


# print(type(colors_list))

# colors_list.sort(reverse=True)
# print(colors_list)
# print(sorted(colors_list))

print("-".join(sorted(Sample_Item.split("-"))))

res = "-".join(sorted(colors_list))
print(res)
