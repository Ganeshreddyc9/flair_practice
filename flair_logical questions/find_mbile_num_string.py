# find mobile numbers from a given string

# s = "This is hyb9900164930 bngl 9900 apr9505909369 flair950"
# O/P -- only mobile numbers in above string
# 9900164930
# 9505909369


s = "This is hyb9900164930 bngl 9900 apr9505909369 flair950"

mobiles= []
mobile = ""

for i in s:
    if i.isdigit():
        mobile += i
# print(mobile)
    else:
        if len(mobile) == 10 and mobile[0] in "9876":
            mobiles.append(mobile)
        mobile = ""

else:
    if len(mobile) == 10 and mobile[0] in "9876":
        mobiles.append(mobile)
# print(mobile)
print(mobiles)


    


