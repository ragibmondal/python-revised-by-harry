# Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.
for i in range(3):
    marks=int(input("Enter the marks of subject:  "))
    if(marks>=33):
        print("You are passed in the subjects")
    else:
        print("You are failed in the subject")