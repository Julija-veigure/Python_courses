# 1. FizzBuzz
# Print a string 1,2,3,4, Fizz, 6, Buzz, 8, ..... 34, FizzBuzz, 36, .... to 97, Buzz, 99, Fizz
# So if number divided by 5 then Fizz If divided by 7 then Buzz, If divided by 5 AND 7 then FizzBuzz
        #otherwise the same number
#  Note: such a task became popular as the first task to ask to determine whether a person knows
        #about programming at all smile

for i in range (1, 101):
    if i % 5 == 0:
        print('Fizzbuzz')
    elif i % 5 == 0:
        print('Fizz')
    elif i % 7 == 0:
        print('Buzz')
    else:
        print(i)

#  2. Christmas tree
# Enter the height of the tree
# Print the tree: Ex. height == 3
# The printout would be:
#   *
#  ***
# *****
# Note: remember that several symbols can be printed at once, for example: print ("" * 10 + "*" * 6)

tree_size = int(input("Please enter tree size:\n"))
line = 1
space = tree_size - line
for i in range (tree_size):
    print((' ' * space) + ('*' * line) + (' ' * space))
    line +=2
    space -=1

# 3. Primes Check if entered positive number is a prime number.
#  A prime number is a number that divides without remainder only by itself and 1.
# Hint: what numbers do we have to check?

number = int(input("Enter positive number:\n"))
i = 2
isPrime = True
while i < number//2:
    if number % i == 0:
        isPrime = False
        break
    i += 1
if isPrime:
    print("Number is prime")
else:
    print("Number is not prime")