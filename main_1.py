# Print two tables

for x in range (1,11):
    print(x,"x 2 =",x*9)

# print count of even numbers
count=[]
for x in range(1,11):
    if (x%2 ==0):
        count.append(x)
print(len(count))


# swap two variable with temp
a=77
b=12
temp=a

a=b
b=temp
print("value of a is ",a)
print("value of b is ",b)

#  swap two variable without temp using add sub
a=int(input("Enter a value for a : "))
b=int(input("Enter a value for b : "))
a=a+b
b=a-b
a=a-b

print("value of a is ",a)
print("value of b is ",b)

#  swap two variable without temp using xor operator
a=int(input("Enter a value for a : "))
b=int(input("Enter a value for b : "))
a=a^b
b=a^b
a=a^b

print("value of a is ",a)
print("value of b is ",b)



