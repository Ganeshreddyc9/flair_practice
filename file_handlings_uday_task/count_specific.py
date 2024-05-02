# 6. Find the total occurrences of a specific word from a text file.



file_path = 'MergedFile.txt'
word = input("enter the word: ")
with open(file_path,'r') as file:
    content = file.read()

word_list = content
# print(type(word_list))
word_list = content.split()
# print(word_list)

count = word_list.count(word)


print(f"total occurrences of a specific word {word} is repeated {count} occurrences")