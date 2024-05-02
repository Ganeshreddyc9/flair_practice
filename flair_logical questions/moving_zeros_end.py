# moving zeros to the end od the list

# list = [1,0,2,3,0,5]


# here i am updatting the original list that not a good practice 
list_1 = [1,0,2,3,0,5]


for i in list_1:

    if i == 0:
        list_1.remove(i)
        list_1.append(i)
   
print(list_1)


non_zero_elements = [x for x in list_1 if x!=0]

zeros_count = len(list_1) - len(non_zero_elements)

res = non_zero_elements+ [0]*zeros_count
print(res)