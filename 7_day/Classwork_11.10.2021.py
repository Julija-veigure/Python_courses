#---------------------------------------------------------------------------
# 1. The Big Result
# Write an add_mult function that requires three parameters / arguments
# Returns the result that is the sum of the 2 smallest arguments multiplied by the largest
# #argument value.
# PS Assume that numeric parameters will always be passed to the function,
# #no need to check types
# Various solutions are possible (you are allowed to use other data structures inside function such as list).
# Example add_mult (2,5,4) -> will return (2 + 4) * 5 = 30

def add_mult(a, b, c):
    num = [a, b, c]
    num.sort()
    min = num[0]
    max = num[-1]
    between = num[1]
    sum = (min + between) * max
    print(f"{num}\nŖesult = {sum}")
    return sum

add_mult(1, 2, 3)
add_mult(-7, 9, 3)
add_mult(-4, 3, 3)

#---------------------------------------------------------------------------

# Write the function is_palindrome (text)
# which returns a bool True or False depending on whether the word or sentence is read equally from both sides.
# PS You can start with a one-word solution from the beginning, but the full solution will ignore whitespace and
# uppercase and lowercase letters.
#
# is_palindrome ("Alus ari i ra    sula") -> True
# is_palindrome("ABa") -> True
# is_palindrome("nava") -> False

def is_palindrome(text):
    print("ORIGINAL TEXT: " + text)
    text = text.replace(" ", "").lower()
    print(f"Changed text: {text}\n"
          f"Reversed text: {text[::-1]}")
    if text == text[::-1]:
        print(f"Text match: True\n")
        return True
    else:
        print("Text doesn't match: False\n")
        return False


is_palindrome("Alot of words are in this text")
is_palindrome("A ba bA ba ba ba Ba")
is_palindrome("IMIMI")


#---------------------------------------------------------------------------
#
# 3. City Population
# The city has a known population p0
# A percentage of population perc is added each year
# Every year a certain number of delta also arrive (or leave)
# We need to know when (if at all) the city will reach a population of p
# Write a function get_city_year (p0, perc, delta, p) that returns the years (full) when p is reached.
# If p cannot be reached, then we return -1


# def get_city_year(p0, perc, delta, p):
#
#
# I DONT UNDERSTAND HOW TO WRITE CODE FOR THIS TASK
#
# get_city_year(10521, 2, 125, 19999)
