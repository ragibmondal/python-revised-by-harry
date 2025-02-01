# Write a program to find whether a given number is prime  or not
a= int(input("Enter the Number:"))
if a>2:
    print("Not a Prime Number")
else:
 for i in range(2,a):
    if(a%i==0):
        print("Not a Prime Number")
        break
 else: 
  print("Prime Number")