import time

l = [1,2,3,4,6,8,7,9]

left_side = 0

# start_time = time.time()
# print(start_time)
for i in range(len(l)):
    

    if left_side  == sum(l[i::]):
        print("my method",l[i])
    else:
        left_side  +=l[i]

end_time = time.time()

# time_taken = end_time-start_time

# print(f"timer taken to come the code run time {time_taken}")

start_time = time.time()
for i in range(len(l)):
    if sum(l[:i]) == sum(l[i:]):
        print(l[i],"other method....")
    end_time = time.time()

time_taken = end_time-start_time

print(f"second timer taken to come the code run time {time_taken}")