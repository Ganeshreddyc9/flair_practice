#Write a program to remove duplicates from the given list.
#[2,3,5,6,6,7,23,45,10,10,45,2]

list_1 = [2, 3, 5, 6, 6, 7, 23, 45, 10, 10, 45, 2]

list_2 = []

for i in list_1:
    # print(i)

    if i  not in list_2:
        list_2.append(i)
print(list_2)