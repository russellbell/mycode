#!/usr/bin/env python3
import datetime

user_name = input("Please enter your name: ")
# day = input("Please enter the day of the week: ")

# weekdays as a tuple
weekDays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
current_day = datetime.date.today().weekday()
currentDayAsString = weekDays[current_day]


print(f"Hello, {user_name}. Happy {currentDayAsString}!")

