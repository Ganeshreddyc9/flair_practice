# Replace all spaces from text with – (dash).


with open('MergedFile.txt','r') as file:

    content = file.read()

    # for char in file:

    new_content = content.replace(" ","-")
    print(new_content)