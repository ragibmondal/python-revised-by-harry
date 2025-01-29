# Write a program to input eight numbers from the user and display all the unique 
# numbers (once).
set1=set()
for i in range(8):
    a=int(input("Enter the Number:"))
    set1.add(a)
    
print(set1)

