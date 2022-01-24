# Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.

from function_exercises import calculate_tip
import itertools
import json

calculate_tip(.18,45)

# Read about and use the itertools module from the python standard library to help you solve the following problems:

# How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?
num_combos = itertools.product(("a","b","c"),("1","2","3"))
print(len(list(num_combos)))
# How many different combinations are there of 2 letters from "abcd"?
num_combo_2 = itertools.combinations('abcd',2)
print(len(list(num_combo_2)))
# How many different permutations are there of 2 letters from "abcd"?
num_perm_2 = itertools.permutations('abcd',2)
print(len(list(num_perm_2)))

# 3 json load

profiles = json.load(open('profiles.json'))
# Total number of users
print(f"Total number of users: {len(profiles)}")
# Number of active users
active_users = [user['name'] for user in profiles if user['isActive']]
print(f"Total number of active users: {len(active_users)}")
# Number of inactive users
inactive_users = [user['name'] for user in profiles if not user['isActive']]
print(f"Total number of inactive users: {len(inactive_users)}")
# Grand total of balances for all users
balances = [float(user['balance'].replace(',','').replace('$','')) for user in profiles]
print(f"Grand total of balances for all users: ${sum(balances)}")
# Average balance per user
print(f"Average balance per user: ${round(sum(balances)/len(balances),2)}")
# User with the lowest balance
lowest_balance = min(profiles, key = lambda x:x['balance'])['name']
print(f"The user with the lowest balance is {lowest_balance}")
# User with the highest balance
highest_balance = max(profiles, key = lambda x:x['balance'])['name']
print(f"The user with the highest balance is {highest_balance}")
# Most common favorite fruit

fruit_count = {}
for prof in profiles:
    if prof['favoriteFruit'] in fruit_count.keys():
        fruit_count [prof['favoriteFruit']] += 1
    else:
        fruit_count [prof['favoriteFruit']] = 1

print(f"Most common favorite fruit: {max(fruit_count)}")

# Least most common favorite fruit
print(f"Least common favorite fruit: {min(fruit_count)}")
# Total number of unread messages for all users
unread_messages = 0
for prof in profiles:
    # To obtain the unread messages per user need to get the number from the greeting string through some splits
    unread_messages += int(prof['greeting'].split('have ')[1].split(' unread')[0])

print(f"There are a total of {unread_messages} unread messages for all users")
