#1. Write a program to find the greatest of four numbers entered by the user.
a= int(input("Enter the first number:"))
b= int(input("Enter the second number:"))
c= int(input("Enter the third number:"))
d= int(input("Enter the forth number:"))
if(a>b and a>c and a>d):
    print(a,"is the greatest number")
elif(b>a and b>c and b>d):
    print(b,"is the greatest number")
elif(c>a and c>b and c>d):
    print(c, "is the greatest number")
elif(d>a and d>b and d>c):
    print(d, "is the greatest number")