# print 1 to 5 using while loop
# i=1
# while(i<6):
#     print(i)
#     i+=1
#print 10,20,30,40,50,60,70,80,90,100
# i=10
# while(i<210):
#     print(i,end=",")
#     i+=10
# 
i=10
# while(i>0):
#     print(i,end=",")
#     i-=1


# Example of a stack in Python using a list last in first out
# my_stack = []
# my_stack.append(1)
# my_stack.append(2)
# print(my_stack)
# popped_element = my_stack.pop()
# print(popped_element)
# print(my_stack)

# Example of a queue in Python using collections.deque
from collections import deque

my_queue = deque()
my_queue.append(1)
my_queue.append(2)
print(my_queue)
popped_element = my_queue.popleft()
print(popped_element)
print(my_queue)
