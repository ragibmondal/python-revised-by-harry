# # Write a python program to display a user entered name followed by Good 
# # Afternoon using input () function.
ex=input("Enter Your Name:")
import pyttsx3
kumar=pyttsx3.init()
kumar.say(f"Good Afternoon {ex} sir Are u serious to learn python with me")
kumar.runAndWait()
