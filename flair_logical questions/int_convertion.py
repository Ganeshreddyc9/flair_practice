# str_week_temps_f="75.7,77.7,88.9,34.6,73.5" convert to integer .

str_week_temps_f="75.7,77.7,88.9,34.6,73.5"

data = str_week_temps_f.split(",")
# print(convert)
result= []
for value in data:
    # print(value)
    conv = int(float(value))
    result.append(conv)
print(result)

# res = [int(float(value)) for value in data ]
# print(res)