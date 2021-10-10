# print("Exercise 1")
# name = input(f"What is your name?\n")
# surname = name[::-1].title()
# print(f"Hi {name}! I know your surname, it's {surname}")

print("Exercise 2")
text = input(f"Player Nr 1, please write text:\n")
text_mask = ""
for c in text:
    if c == " ":
        text_mask += " "
    else:
        text_mask += "*"
print(text_mask)

letter = input("Player Nr 2, please write letter\n")
letter_check = ""
for c in text:
    if c == " ":
        letter_check += " "
        #print(f"Congratulations, here is the letter {letter}")
    elif c == letter:
        letter_check += c
    else:
        letter_check += "*"
print(letter_check)

# 3. Text conversion
# Write a program for text conversion
# Save user input
# Print the entered text without changes
# Exception: if the words in the input are not .... bad, then the output is not ...  bad section must be changed to is good
#
# Examples:
# The weather is not bad -> The weather is good
# The car is not new -> The car is not new
# This cottage cheese is not so bad -> This cottage cheese is good
# Hints:
# Find (or index, or even rfind) will probably come in handy, as may an operator. Also slice syntax will be useful.
# Extra: How would you do this task in Latvian language (nav slikts/a -> ir labs/a)?