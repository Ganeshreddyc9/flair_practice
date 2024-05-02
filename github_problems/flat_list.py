# Problem 2
# l = [0, [1,2,3], [4,5,[6,7,8,[9,10,11]], [12, 13]], 15, 16]
# result should be flatten
# [0, 1, 2, 3, 4, 5, 6, ----------- 16]

l = [0, [1,2,3], [4,5,[6,7,8,[9,10,11]], [12, 13]], 15, 16]

def flat(l):

    result = []
    for ele in l:
        if isinstance(ele,list):
            result.extend(flat(ele))
        # print(result,end=" ")
        else:
            result.append(ele)
    return result

l = [0, [1,2,3], [4,5,[6,7,8,[9,10,11]], [12, 13]], 15, 16]
print(flat(l))

