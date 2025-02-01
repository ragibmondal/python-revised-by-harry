# Write a program to print the following star pattern.
#  *
# ***
# ***** for n = 3
a=int(input("Enter the number: "))
for i in range(1,a+1):
    print(" "*(a-i),end="")
    print("*" * (2*i-1),end="")
    print("\n")