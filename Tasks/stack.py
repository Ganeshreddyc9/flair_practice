

# Stack This module queue also provides LIFO Queue which technically works as a Stack.


stack = []

# pushing elements into stack

stack.append(1)
stack.append(2)
stack.append(3)

# poping element from the stack
popped_item = stack.pop()
print(popped_item)

# for element in stack:
#     print(element,"loop element")
#     popped_item = stack.pop()
#     print("in loop:",popped_item)
# # print("out of the loop:",popped_item)