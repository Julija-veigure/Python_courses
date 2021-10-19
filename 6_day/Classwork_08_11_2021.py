# 1a. Average value
# Write a program that prompts the user to enter numbers (float).
# The program shows the average value of all entered numbers after each entry.
# PS. 1a can do without a list
# 1b. The program shows both the average value of the numbers and ALL the numbers entered
# PS Exit the program  by entering "q"
# 1c The program does not show all the numbers entered but only TOP3 and BOTTOM3 and of course still average.

number_list = []
while True:
    entered_number = input(f"Please, enter numbers to calculate the average number, or enter 'q' to quit\n")
    if entered_number == "q":
        print("Thank you!")
        break
    else:
        number_list.append(float(entered_number))
        average_number = float((sum(number_list) / len(number_list)))
        print(f"{number_list}The average number is {average_number}!\n")

# ------------------------------------------------------------------------------------


# 3. Reversed words
# The user enters a sentence.
# We output all the words of the sentence in reverse form. - not the whole text reversed!!
# Example
# Alus kauss mans -> Sula ssuak snam
# PS Split and join operations could be useful here.

sentence = input("Please enter sentence:\n")
words = sentence.split()
reversed_words = [i[::-1] for i in words]
print(reversed_words)

# ------------------------------------------------------------------------------------


# 4. Prime numbers -
# Find and output the first 20 (even better option to choose how many first primes we want)
# prime numbers in the form of a list i.e. [2,3,5,7,11, ...]

list_of_numbers = []
max_number = int(input("Please write max number of prime, which you want to be listed: "))
current_number = 1
while len(list_of_numbers) < max_number:
    current_number += 1
    for i in range(2, int(current_number // 2) + 1):
        if (current_number % i) == 0:
            print(f"{current_number} divides by {i} - not a prime: ")
            break
    else:
        list_of_numbers.append(current_number)
print(f"Primes {list_of_numbers}")

