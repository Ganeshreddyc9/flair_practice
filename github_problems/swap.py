# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]


def swap_positions(list_1, pos_1, pos_2):




    list_1[pos_1], list_1[pos_2] = list_1[pos_2], list_1[pos_1]
    return list_1

list_1 = [23, 65, 19, 90]
# pos_1, pos_2= 1, 3
pos_1, pos_2= 0, 2
print(swap_positions(list_1,pos_1, pos_2))
