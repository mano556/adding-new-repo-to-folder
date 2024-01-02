# for x in range(1,3):
#     print("Week :",x)
#     for y in range(1,4):
#         print("Day :",y)


# # # pattern
# for x in range(1,6):
#     for y in range(1,x+1):
#         print(y,end=" ")
#     print()
# ##################################################################################################
# #NUMBER PATTERNS
# #program-1

# # 1  
# # 2 2  
# # 3 3 3  
# # 4 4 4 4  
# # 5 5 5 5 5   

# for x in range(0,6):
#     for y in range(0,x):
#         print(x,end=" ")
#     print()

# #program-2

# # 1 
# # 1 2 
# # 1 2 3 
# # 1 2 3 4 
# # 1 2 3 4 5 

# row =int(input("Enter the number of row : "))
# for x in range(0,row+1):
#     for y in range(1,x+1):
#         print(y,end=" ")
#     print()

# # program-3

# # 1 1 1 1 1 
# # 2 2 2 2 
# # 3 3 3 
# # 4 4 
# # 5
# row =int(input("Enter the number of row : "))
# for x in range(1,row+1):
#     for y in range(0,row+1-x):
#         print(x,end=" ")
#     print()

# # program-4
# # 5 5 5 5 5 
# # 5 5 5 5 
# # 5 5 5 
# # 5 5 
# # 5

# row=int(input("Enter the number of rows : "))
# for x in range(1,row+1):
#     for y in range(0,row+1-x):
#         print(row,end=" ")
#     print()

# # program -5
# # 0 1 2 3 4 5 
# # 0 1 2 3 4 
# # 0 1 2 3 
# # 0 1 2 
# # 0 1 
# # 0 
# row= int(input("enter the number of row : "))
# for x in range(0,row+1):
#     for y in range(0,row+1-x):
#         print(y,end=" ")
#     print()

# # program-6
# # 5 5 5 5 5 
# # 4 4 4 4 
# # 3 3 3 
# # 2 2 
# # 1
# row =int(input("Enter the number of row : "))

# num=1
# for x in range(row,0,-1):  
#     for y in range(0,row+1-num):
#         print(x,end=" ")
#     num+=1

#     print()

# # program-6
# # 1 
# # 2 1 
# # 3 2 1 
# # 4 3 2 1 
# # 5 4 3 2 1
# row=int(input("Enter the numbner of row : "))
# for x in range(0,row+1):
#     for y in range(x,0,-1):
#         print(y,end=" ")
#     print()

# # program-7
# # 5 4 3 2 1 
# # 4 3 2 1 
# # 3 2 1 
# # 2 1 
# # 1
# row=int(input("enter the number of rows : "))
# for x in range(0,row+1):
#     for y in range(row-x,0,-1):
#         print(y,end=" ")
#     print()
    
# # program-8
# # 1
# # 3 2
# # 6 5 4
# # 10 9 8 7

# row=int(input("enter the number : "))

# num=1
# num_2=0
# a=2
# b=1
# for x in range(0,row):
#     for y in range(num,num_2,-1):
#         print(y,end=" ")
#     num+=a
#     num_2+=b
#     a+=1
#     b+=1
#     print()

# # program-9
# #           1 
# #         1 2 
# #       1 2 3 
# #     1 2 3 4 
# #   1 2 3 4 5 
    
# for x in range(5+1):
#     for y in range(0,5-x):
#         print(" ",end=" ")
#     for z in range(1,x+1):
#         print(z,end=" ")
#     print()

# program-10
# P
# Py
# Pyt
# Pyth
# Pytho
# Python

# name="python"  
# result=""
# for y in name:
#     result+=y
#     print(result)
# print()

# program-11





