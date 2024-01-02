# # Print two tables

for x in range (1,11):
    print(x,"x 2 =",x*9)

# # print count of even numbers <Method-1>
count=[]
for x in range(1,11):
    if (x%2 ==0):
        count.append(x)
print(len(count))

# # print count of even  & even numbers <Method-2>
even_count=0
odd_count =0
for x in range(1,11):
    if (x%2==0):
        even_count+=1
    else:
        odd_count+=1
print("Even : ",even_count)
print("Odd : ",odd_count)

# # print count of numbers which are divisible by 3 &5
count_3 = 0
count_5 = 0
count_3and5 = 0

for x in range(1, 101):
    if (x % 3 == 0) and (x % 5 == 0):
        count_3and5 += 1
    elif (x % 3 == 0):
        count_3 += 1
    elif (x % 5 == 0):
        count_5 += 1

print("3 divisible : ", count_3)
print("5 divisible : ", count_5)
print("Both 3 & 5 divisible : ", count_3and5)

# # print sum of natural numbers from 1 to 5
sum=0
for x in range(1,6):
    sum+=x
print(sum)

# # ask 10 input from user then sum then give average of inputs
a=[]
sum=0
for x in range(10):
    num=int(input("Enter the value of " + str(x+1)+" : "))
    a.append(num)
for i in a:
    sum+=i
result=sum/len(a)
print(result)

# first 7 natural number

num=int(input("Enter the number : "))
print("first "+str(num)+" natural numbers : ")
for x in range(1,num+1):
   print(x)
    
# cube of an integer
num=int(input("Enter the number : "))
for x in range(1,num+1):
    print("The cube of "+str(x)+" is "+str(x**3))
