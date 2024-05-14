#Purpose: Creating a programs that lets you know how the weather is at your location
#Programmer name: Terrance Sutton 
# #Date:5/13/2024

name = input("What is your name: ")
city = input("What city do you live in: ")
temperature = float(input("What is the temperature: "))

if temperature > 60:
    print("Hello", name, "it is nice where you live")
else:
    print("Hello", name, "it is too cold where you live")