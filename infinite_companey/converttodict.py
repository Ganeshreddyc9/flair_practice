# make it in dicttionary as key , value output ->{324:44,45:23,5:5,34:23}
# list1=[324,45,5,34]
# list2=[44,23,5,23]

list1=[324,45,5,34]
list2=[44,23,5,23]

output_dict = {}

for key,value in zip(list1,list2):
    output_dict[key] = value

print(output_dict)
