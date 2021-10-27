import statistics
# 1. Min, Avg, Max
# Write a function get_min_avg_max (sequence) that returns a tuple with three values, the smallest, the arithmetic mean, and the largest value in the string, respectively.
# Example:
# get_min_avg_max ([0,10,1,9]) -> (0,5,10)
# the incoming sequence can be a tuple or a list with numeric values.
#
def get_min_avg_max(a):
    print("\nGiven:", a)
    print("MIN number is:", min(a), "\nMAX number is:", max(a),
          "\nMedian number is:", statistics.median(a))
    return min(a), max(a), statistics.median(a)


get_min_avg_max([1, 100, 5, 9, 15, 6])
print(type(get_min_avg_max([1, 2, 3, 4, 5, 6, 7, 8, 9])))
print(type(get_min_avg_max("Baaaaac")))

# 2. Common Elements
# Write a function that returns a tuple with common elements in three sequences. Inputs can be list, tuple, string.
# get_common_elements (seq1, seq2, seq3)
# Example:
# get_common_elements ("abc", ['a', 'b'], ('b', 'c')) -> ('b',) # we return a tuple with a single element
# # remember that we can convert strings to set with set(mystring), and set to tuple with tuple(myset)
#
def get_common_elements (seq1, seq2, seq3):
    return (set(seq1) & set(seq2) & set(seq3))

print("\n", get_common_elements ("abc", ['a', 'b'], ('b', 'c')))

# 3. Is there a pangram?
# Write a function is_pangram(text, alphabet='abcdefghijklmnopqrstuvwxyz')
# that returns True when the text parameter contains all the letters passed in an alphabet.
# We return False otherwise
# pangram - sentence, word string containing all letters of the alphabet - https://en.wikipedia.org/wiki/Pangram
# We ignore spaces and believe that uppercase is as valid as lowercase, i. here A and a -> a
# print(is_pangram("The five boxing wizards jump quickly")) -> True
# print(is_pangram("Not a pangram")) -> False
# Bonus: test it also on Latvian alphabet:
# a_lv = 'aābcčdeēfgģhiījkķlļmnņoprsštuūvzž'
# print(is_pangram('Tfū, čeh, džungļos blīkšķ, zvaņģim jācērp!', alphabet=a_lv)) -> True

def is_pangram(text, alphabet):
    return set(text.lower()) >= set(alphabet.lower())


print("\n", is_pangram("The five boxing wizards jump quickly", "abcdefghijklmnopqrstuvwxyz")) #-> True
print("\n", is_pangram("Nav pangram", "abcdefghijklmnopqrstuvwxyz")) #-> False
