# Create an empty dictionary. Allow 4 friends to enter their favorite language as 
# value and use key as their names. Assume that the names are unique.
# s={}
# for i in range(4):
#     a=input("Enter the name: ")
#     b=input("Enter the language: ")
#     s[a]=b
# print(s,len(s))
a={}
name=input("Enter Friends Name:")
lang=input("Enter Friends Language: ")
a.update({name:lang})    
name=input("Enter Friends Name:")
lang=input("Enter Friends Language: ")
a.update({name:lang})    
name=input("Enter Friends Name:")
lang=input("Enter Friends Language: ")
a.update({name:lang})    
name=input("Enter Friends Name:")
lang=input("Enter Friends Language: ")
a.update({name:lang})    
name=input("Enter Friends Name:")
lang=input("Enter Friends Language: ")
a.update({name:lang})
print(a)    
