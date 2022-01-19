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

