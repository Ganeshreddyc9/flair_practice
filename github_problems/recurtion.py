# 
# def int_sum(num):
    
#     if num <= 9:
#         return num
#     else:
        
    
#         return num % 10 + int_sum(num // 10)
    
# print(int_sum(12345))

def int_sum_l9(num):
    result = 0
    while num > 0:
        result += num % 10 # result = result + num % 10
        num //= 10 # num = num // 10
    if result > 9:
        return int_sum_l9(result)
    return result

int_sum_l9(12345)