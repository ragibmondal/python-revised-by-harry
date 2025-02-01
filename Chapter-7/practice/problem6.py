# Write a program to calculate the factorial of a given number using for loop.
a= int(input("Enter the Number: "))
fact=1
for i in range(1,a+1):
    fact*=i
print(f"The factorial of {a} is {fact}")