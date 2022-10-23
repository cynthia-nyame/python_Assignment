#1. With a for  print even numbers from 1 - 30.
start,end = 1, 30
for num in range(start,end +1):
    if num % 2==0:
        print(num, end = " ")
print("")
#With while loop, print even numbers from 1 - 30.
max=30
num=1
while num<=max:
    if(num %2==0):
        print(num,end = " ")
    num=num+1
print("")
# 2.With a for  print odd numbers from 1 - 30.
start,end = 1, 30
for num in range(start,end +1):
    if num % 2==1:
        print(num, end = " ")
print("")       
#With while loop, print odd numbers from 1 - 30.
max=30
num=1
while num<=max:
    if(num %2==1):
        print(num,end = " ")
    num=num+1
print("")