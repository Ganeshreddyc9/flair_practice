# 2 Update total marks with sum of marks

_dict = {"city": ["Hyderabad", 500072], 
        'student': [{"name": "rahul", "roll_no": 123, "marks": {'maths': 90, "science": 87, "social": 75}, "total_marks": 0}]}

print("before updATING The total sum:",_dict['student'][0]['total_marks'])
# for key , value in _dict.items():
    # print(key,value)
    # data = ['marks']
count = 0
for value in (_dict['student'][0]['marks'].values()):
    count += value
    # print(count)
# print(count)

# print(_dict.values())

# print(dir(_dict))
_dict['student'][0]['total_marks']=count

print(f"after updating the total sum ",_dict['student'][0]['total_marks'])

print(_dict)