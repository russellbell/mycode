"""
col_list= ["blue", "Columbus"]
Append the integer 1492 to col_list
Include an input asking for the user's name
using the appended list and the input, make this output:
In 1492, Columbus sailed the ocean blue. <name> fell off the boat
"""
col_list = ["blue", "Columbus"]
col_list.append(1492)
#print(col_list)
username = input("Please enter your name: ")
print(f"In {col_list[2]}, {col_list[1]} sailed the ocean {col_list[0]}. {username} fell off the boat.")

print(type(col_list[2]))
