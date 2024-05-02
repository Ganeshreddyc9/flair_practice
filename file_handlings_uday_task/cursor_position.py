# 9. Write a program to know the cursor position and print the text according to below-given specifications:
# a. Print the initial position
# b. Move the cursor to 4th position
# c. Display next 5 characters


with open('MergedFile.txt','r') as file:

    initial_position = file.tell()

    file.seek(4)
    cursor_position_after_move = file.tell()

    display_5_chars = file.read(5)
print(f"initial position is {initial_position}")
print(f"cursor moved to the 4 th position {cursor_position_after_move}")
print(f"dispalying next five characters {display_5_chars}")