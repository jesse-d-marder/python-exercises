# Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.

from function_exercises import calculate_tip
import itertools

calculate_tip(.18,45)

# Read about and use the itertools module from the python standard library to help you solve the following problems:

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
num_combos = itertools.permutations([["a","b","c"],["1","2","3"]],2)
print(list(num_combos))
# How many different combinations are there of 2 letters from "abcd"?
num_combo_2 = itertools.combinations('abcd',2)
print(list(num_combo_2))
print(len(list(num_combo_2)))
# How many different permutations are there of 2 letters from "abcd"?
num_perm_2 = itertools.permutations('abcd',2)
print(list(num_perm_2))
print(len(list(num_perm_2)))
