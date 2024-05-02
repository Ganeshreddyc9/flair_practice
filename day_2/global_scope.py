# global

# if object is global which is out side a function and autside a class then it is a global

# ex:1
global_val = 100

def fun():
    print(global_val)
# fun()



global_val1 = 100

def fun1():
    global global_val1
    global_val1 = 200
    print(global_val1)

fun1()
print(global_val1)

print((dir('builtins')))
