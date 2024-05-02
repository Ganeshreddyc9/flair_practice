s = "I am in hyderabad"
# If we give centre = 50
# Result = " I am in hyderabad "
# Do this without using center ( )
centre = 50

total_length = 50
padding_length = total_length - len(s) 
left_padding = padding_length//2

right_padding = padding_length-left_padding 
# print(s.center(50))

result = " "*left_padding+ s + " "*right_padding

print(result)
print(s.center(50))







# res = centre //2