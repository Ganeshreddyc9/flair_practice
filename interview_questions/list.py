list_1=[5,6,4,2,1,3]
length=len(list_1)

# string=""
for i in range(length):
    print("i value for ---->",i)


    for j in range(i+1,length):
        print("j value is : ",j,list_1[j])
        if list_1[i]>list_1[j]:
            list_1[i],list_1[j]=list_1[j],list_1[i]
            print(list_1)



    #         string=string+str(j)
    # print(string)-