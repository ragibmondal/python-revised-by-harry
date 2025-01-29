# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!
bangla={
    "ami": "I",
    "tumi": "you",
    "amara":"we",
    "tara":"they",
}
print("Options are: ",bangla.keys())
a=input("Enter the Word:")
print("The meaning of the words is: ",bangla.get(a))