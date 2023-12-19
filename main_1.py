# Print two tables

for x in range (1,11):
    print(x,"x 2 =",x*9)

# print count of even numbers
count=[]
for x in range(1,11):
    if (x%2 ==0):
        count.append(x)
print(len(count))