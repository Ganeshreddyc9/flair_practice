str_week_temps_f="75.7,77.7,88.9,34.6,73.5"

str_1 = str_week_temps_f.split(",")
print(str_1)

count = 0
for i in str_1:
    # print(i)
    count = count+float(i)

print(count)

