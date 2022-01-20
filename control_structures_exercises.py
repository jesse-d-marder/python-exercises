# 1. Conditional basics

day_of_week = input("What is the day of the week?")
if str(day_of_week).lower() == 'monday':
    print("It is Monday")
else:
    print("It is not Monday")

day_of_week = input("What is the day of the week?")
if str(day_of_week).lower() in ['monday','tueday','wednesday','thursday','friday']:
    print(f"{day_of_week.capitalize()} is a weekday")
else:
    print(f"{day_of_week.capitalize()} is on the weekend")

hours_worked_in_week = 45
hourly_rate = 25

if hours_worked_in_week <= 40:
    weekly_paycheck = hours_worked_in_week*hourly_rate
else:
    weekly_paycheck = (hours_worked_in_week-40)*hourly_rate*1.5+(40*hourly_rate)

## 2 Loop Basics

i = 5

while i <= 15:
    print(i)
    i += 1

i =0

while i <= 100:
    print(f"{i} \n")
    i += 2

i = 100

while i >= -10:
    print(f"{i} \n")
    i -= 5

i = 2

while i < 1000000:
    print(i)
    i = i*i

i = 100

while i >= 5:
    print(i)
    i -= 5
# b. For loops
# i.
number = int(input("Give me a number"))

for i in range(1,11):
    product = i * number
    print(f"{number} x {i} = {product}")

# ii. 
m = '1'
for i in range(1,10):
    print(i*int(m))
    m += '1'

# c. break and continue

while True:
    user_num = input ("Give me an odd number between 1-50")
    if not user_num.isdigit():
        print("Numbers only please, try again")
    elif not 1 <= int(user_num) <= 50:
        print("outside of range, try again")
    elif int(user_num) % 2 == 0:
        print("That was even, try again")
    else:
        break

print(f"Number to skip is {user_num} \n")

for i in range(1,50,2):
    if i != int(user_num):
        print(f"Here is an odd number: {i}")
    else:
        print(f"Yikes! Skipping number: {user_num}")
        continue

# d. input function

while True:
    user_num = input("Give me a positive number please")
    if not user_num.isdigit():
        print("Numbers only please, try again")
    elif int(user_num) <= 0:
        print("outside of range, try again")
    else:
        break

for i in range(int(user_num)+1):
    print(i)

# e. prompt for positive integer, then output input down to 1

while True:
    user_num = input("Give me a positive number please")
    if not user_num.isdigit():
        print("Numbers only please, try again")
    elif int(user_num) <= 0:
        print("outside of range, try again")
    else:
        break

for i in range(int(user_num), 0, -1):
    print(i)

# 3. FizzBuzz

for i in range(1,101):
    print(i)

for i in range(1,101):
    
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print(i)

# 4. Table of powers - could use some alignment

while True:
    
    user_num = int(input("Please enter an integer for your power table to go up to!"))

    print("Here is your table!")

    print("number | squared | cubed ")
    print("------ | ------- | ----- ")
    for i in range(1,user_num+1):
        print(f"{i}      |{i**2}         |{i**3}  ")
    
    continue_input = input("Want to continue? y/n")

    if continue_input == 'y':
        continue
    else:
        break

# 5. Grade conversion

while True:

    user_grade = int(input("Please give me a grade between 0 - 100"))
    print(f"{user_grade} converts to a: ")
    if 88 <= user_grade <= 100:
        print("A")
    elif 80 <= user_grade <= 87:
        print("B")
    elif 67 <= user_grade <= 79:
        print("C")
    elif 60 <= user_grade <= 66:
        print("D")
    elif 0 <= user_grade <= 59:
        print("F")
    else:
        print("Invalid grade")

    continue_input = input("Want to continue? y/n")

    if continue_input == 'y':
        continue
    else:
        break

# 6. List of book dictionaries

books = [{'title':'Moby Dick', 'author': 'Herman Melville', 'genre': 'fiction'},{'title':'Harry Potter', 'author': 'JK Rowling', 'genre': 'children\'s fiction'},
{'title':'Pride and Prejudice', 'author' :'Jane Austen', 'genre': 'romance'},{'title':'Lone Survivor', 'author': 'Mark K', 'genre': 'non-fiction'},
{'title':'Gone Girl', 'author' :'Jane something', 'genre': 'fiction'},{'title':'Python Cookbook', 'author': 'Oreilly', 'genre': 'non-fiction'}]

for book in books:
    print(f'This book is called {book["title"]} and is by {book["author"]} and is the genre {book["genre"]}')

user_genre = input("Please enter a genre")

i = 0
for book in books:
    if book["genre"] == user_genre and i == 0:
        print(f"In {book['genre']} we have {book['title']}")
        i += 1
    elif book["genre"] == user_genre and i != 0:
        print(f"we also have {book['title']}")