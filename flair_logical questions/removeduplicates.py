# remove duplicates from the given dict output->{'b':1,'d':2}
# dict_1 = {"a":0,"b":1,"c":0,"d":2,'e':0}

dict_1 = {"a":0,"b":1,"c":0,"d":2,'e':0}

result = {}
for key,value in dict_1.items():
    
    if list(dict_1.values()).count(value)==1:
        result[key] = value
        
print(result)
 
