# Exercises from https://ds.codeup.com/python/functions/

# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(x):
    # Checks if the passed argument (type converted to int) is equal to 2
    return int(x) == 2
# Checks that 2 in string form returns True
is_two('2')
is_two(2)
is_two('3')
is_two(3)

# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(x):
    # Checks whether the passed argument is in the list of vowels and returns True if it is
    return x in ['a','e','i','o','u']
is_vowel('a')
is_vowel('b')
is_vowel(5)
# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(x):
    # Uses the previously defined is_vowel function to return True if the passed argument to is_vowel is not True
    return not is_vowel(x)
is_consonant('x')
is_consonant('a')
# Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_consonant(x):
    if is_consonant(x[0]): 
        return x.capitalize()
capitalize_consonant('aardvark')
capitalize_consonant('rare')
# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(tip_p, bill_total):
    return tip_p * bill_total
calculate_tip(0.18, 68.32)
calculate_tip(0.2, 45)
# Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(original, discount_percentage):
    return original - original*discount_percentage/100
apply_discount(100,20)
apply_discount(65,5)
# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(x):
    return float(x.replace(",",""))
handle_commas('1,000,009')
handle_commas('3,987.44')

# Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(user_grade):
    if 88 <= user_grade <= 100:
        return("A")
    elif 80 <= user_grade <= 87:
        return("B")
    elif 67 <= user_grade <= 79:
        return("C")
    elif 60 <= user_grade <= 66:
        return("D")
    elif 0 <= user_grade <= 59:
        return("F")
get_letter_grade(76)
get_letter_grade(45)
get_letter_grade(98)
# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(x):
    for letter in x:
        if is_vowel(letter):
            x = x.replace(letter, "")
    return x
remove_vowels('aardvark')
remove_vowels('captain')
remove_vowels('echo')
# Define a function named normalize_name. It should accept a string and return a valid python identifier

# A little clunky but it works and is robust
def normalize_name(x):
    x = x.strip()
    x_list = list(x)
    swapped_space = False

    for char in x_list:
        if not char.isidentifier() and not char == " ":
            x_list.remove(char)

    x = "".join(x_list)
    x = x.strip()
    x_list = list(x)

    for i, char in enumerate(x_list):   
        if char == " " and not swapped_space:
            x_list[i] = '_'
            swapped_space = True
        elif char == " " and swapped_space:
            x_list[i] = ""
            swapped_space = False

    x = "".join(x_list)
    x = x.lower().strip()
    return x

normalize_name('First Name')
normalize_name('% Completed')

# Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumulative_sum([1, 1, 1]) returns [1, 2, 3]
# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(x):
    new = [x[0]] # Initialize new list with first value to store cumulative sums
    for i in range(1,len(x)):
        new.append(x[i]+new[i-1])

    return new
cumulative_sum([1,2,3,4])
# Additional Exercise


# Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.
# Bonus

# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.
# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27