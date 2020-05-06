#!/usr/bin/env python3
char_name = ""
char_stat = ""
char_dict = {"flash": {"speed": "fastest", "intelligence": "lowest", "strength": "lowest"},
             "batman": {"speed": "slowest", "intelligence": "highest", "strength": "money"},
             "superman": {"speed": "fast", "intelligence": "average", "strength": "strongest"}}

while char_name != "flash" and char_name != "batman" and char_name != "superman" and char_stat != "speed" and char_stat != "intelligence" and char_stat != "strength":
    char_name = input("Which character do you want to know about? (Flash, Batman, Superman)").lower()
    char_stat = input("What statistic do you want to know about? (Strength, speed, or intelligence)").lower()

print(f"{char_name.capitalize()}'s {char_stat} is {char_dict[char_name][char_stat]}")
