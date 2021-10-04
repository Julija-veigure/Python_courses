#1. Health check  Ask user for their temperature.
# If the user enters below 35, then output "not too cold"
# If 35 to 37 (inclusive), output "all right"
# If the temperature  over 37, then output  "possible fever"
username = input("What is your name?")
temp = input(f"{username}, what is the outside temperature?")
not_too_cold = 37
all_right = 35
possible_fever = "Possible fever"
if temp < 35:
    print("Not too cold")
    if temp (<= 37 and >= 35):
        print("All right")
        else print()