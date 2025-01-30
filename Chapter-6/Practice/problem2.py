# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.
a= int (input("Enter the marks of first subject:"))
b= int (input("Enter the marks of second subject:"))
c= int (input("Enter the marks of forth subject:"))
# cheak for total percentage
t=(100*(a+b+c))/300
if(t>=40  and a>=33 and b>=33 and c>=33):
    print("You are Passed the exam")
else:
    print("You are failed")