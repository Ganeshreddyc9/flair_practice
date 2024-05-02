d = [23,54,5,4,56,34]

small_num = d[0]

for i in range(len(d)):

    # print(i) refer notes and just do the paper work if wont get the answer 
    if small_num > d[i]:
        small_num = d[i]

print(small_num)