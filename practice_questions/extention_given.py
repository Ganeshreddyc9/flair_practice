#  Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

filename = input("enter the filename:")

extention = filename.split(".")
print(extention)
print(extention[-1])