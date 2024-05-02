# Write a python program to create a dictionary.
# data = ["sachin cricket", "Federer tennis", "Nadal tennis", "virat cricket", "Messi football"]
# o/p: {"cricket": ["sachin", "virat"], "tennis": ["federer", 'nadal'], "football": ['Messi']}

data = ["sachin cricket", "Federer tennis", "Nadal tennis", "virat cricket", "Messi football"]


result = {}

for info in data:
    player,sport = info.split()

    result[sport] = result.get(sport,[]) +[player]

    # if sport in result:
    #     result[sport].append(player)
    # else:
    #     result[sport] = [player]
print(result)
















# result = {}
# for value in data:
#     player,sport= value.split()

#     result[sport] = result.get(sport,[])+[player]
# print(result)
    

