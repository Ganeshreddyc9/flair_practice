# 1. Create a text file “intro.txt” in python and ask the user to write a single line of text by user input.


text_file = open('intro.txt','w')

text_file.write(input("write a single line of text: "))