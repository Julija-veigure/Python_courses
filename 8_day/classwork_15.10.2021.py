# # 1. What's the frequency?
# # Write a function: get_char_count(text) that receives a string and returns a dictionary with the number of single
# letter applications.
# # get_char_count ("hubba bubba") -> {'h': 1, 'u': 2, 'b': 5, 'a': 2, '': 1}
# # # dictionary sequence doesn't matter and the whole alphabet doesn't have to be included
# #  There may also be a solution with Counter from standard Python library but this is definitely not necessary,
# although it is very elegant smile
# ____________________________________________________________

def get_char_count(text):
    letters = {}
    for i in text:
        if i in letters:
            letters[i] +=1
        else:
            letters[i] = 1
            print(letters)
    return letters


get_char_count("Ehubba bubba")
get_char_count("TTT ab")

# 2. Dictionary editor
# Write replace_dict_value (d, bad_val, good_val), which returns a dictionary with changed values
# The parameters of the function are the dictionary d to be processed and the values bad_val to be changed to good_val
# clean_dict_value ({'a': 5, 'b': 6, 'c': 5}, 5, 10) -> {'a': 10, 'b': 6, 'c': 10}, because 5 was the value to be replaced.
# ____________________________________________________________

def replace_dict_value(d, bad_val, good_val):
    print("\nGiven:", d)
    for key, value in d.items():
        if value == bad_val:
            d[key] = good_val
            print("Result after changes", d)
    return d


replace_dict_value({"a": 1, "b": 2, "c": 5, "d": 4}, 5, 3)


# 3. Dictionary cleaner
# 3a. Write clean_dict_value (d, bad_val), which returns a cleaned dictionary
# The parameters of the function are the dictionary d to be processed and the value bad_val to be disposed of together with its key.
# Example:
# clean_dict_value ({'a': 5, 'b': 6, 'c': 5}, 5) -> {'b': 6}, because 5 was a value for both a and c keys to get rid of.
# ____________________________________________________________

def clean_dict_value(d, bad_val):
    print("\nGiven:", d)
    for key, value in d.items():
        if value == bad_val:
            del d[key]
            print("Result after delete:", d)
            break
    return d


clean_dict_value({'a': 10, 'b': 2, 'c': 10, 'd': 4}, 10)
clean_dict_value({'a': 1, 'b': 2, 'c': 3, 'd': 4}, 2)
