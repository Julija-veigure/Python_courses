import datetime
# 1. Exercise - Age 100
#
# Write a program that asks for and saves a username
# Ask a question about the user's age, using the username in the question.
# Shows in how many years the user will be 100 years old smile
# BONUS: Let the program also show the year when the user will be 100 years old.
# It could use a variable with the current year.
# It would be even better to get the current year automatically
# then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). year
username = input("What is your name?")
print(f"{username}, you have a nice name!")
age = int(input(f"{username}, how old are you?"))
target_age = 100
birthday = (target_age - age)
print(f"{age} years old! Nice! After {birthday} years you will be 100 years old :)")
currentYear = datetime.datetime.now(). year
year = currentYear + birthday
print(f"You will be {target_age} in {year} year")

# 2. Exercise - Room volume
#
# Ask user to input 3 numbers - width, length, height
# Find the volume of the room
# PS Think about units and what is the most appropriate data type for this

w = float(input(f"{username}, input 3 numbers please: \n1. Your bathroom width:"))
l = float(input(f"2. Bathoom lenght:"))
h = float(input(f"3. Bathoom height:"))
print("Thank you!")
volume = round((w * l * h), 2)
print(f"Your bathroom volume is {volume}")

# 3. Exercise - Temperature Conversion
# Write a program that asks user for temperature in Celsius and prints out this same temperature in Farenheit
# formula is: farenheit = 32+celsius*(9/5)
# PS Remember about data type conversion, also consider precision

temp = input(f"Last question, what is the temperature in Celsius?")
temp = float(temp)
temp_faren = 32+temp*(9/5)
print(f"Temperature in celsius is {temp} and in Farenheits is {temp_faren}")