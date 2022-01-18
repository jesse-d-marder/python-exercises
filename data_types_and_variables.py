# Describe following scenarios with Python code

# 1st scenario - movie rental
price_per_day = 3
days_per_movie = {'Little Mermaid': 3, 'Brother Bear': 5, 'Hercules': 1}
total_payment = sum([price_per_day*days for days in days_per_movie.values()])

print(f'Total payment is: {total_payment}')

# 2nd scenario - hourly rates
rate_per_hour = {'Google':400, 'Amazon':380, 'Facebook':350}
hours_worked = {'Google':6,'Amazon':4,'Facebook':10}

total_payment = sum([rate_per_hour[x]*hours_worked[x] for x in rate_per_hour.keys()])

print(f'You will be paid {total_payment}')

# 3rd scenario - class
class_is_full = False
is_conflict = False
can_enroll = not class_is_full and not is_conflict

# 4th scenario - product offer
is_offer_expired = False
items_bought = 1
is_premium = False
apply_offer = (not is_offer_expired) and (items_bought>2 or is_premium)

# continuing on...
username = 'codeup'
password = 'notastrongpassword'

password_at_least_5 = len(password)>=5
username_no_more_20 = len(username)<=20
password_vs_username = (username != password)
starts_with_whitespace = (username[0]==' ') or (password[0]==' ')