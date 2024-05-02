s = "This is hyb9900164930bngl 9900 flair950apr9505909369"
# O/P -- only mobile numbers in above string
# 9900164930
# 9505909369

mobiles = []
mobile = ""
for i in s:
    # print(i)
    if i.isdigit():
        
        mobile +=i
        # print(mobile,"....")
        # print(mobiles,"....ss")
    else:
        if len(mobile) == 10 and mobile[0]  in   "9876":
            mobiles.append(mobile)
        mobile = ""
        # print(mobile,"===")
        # print(mobiles)
else:
    # print(mobile)
    if len(mobile) == 10 and mobile[0] in "9876":
        mobiles.append(mobile)
        
print(mobiles)