# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]


def swappositions(list, pos1, pos2):

    get = list[pos1], list[pos2]

    list[pos2], list[pos1] = get

    return list

List = [23, 65, 19, 90]

pos1, pos2 = 1, 3

print(swappositions(List,pos1-1, pos2-1))