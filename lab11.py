#!/usr/bin/env python3

switch = {"hostname": "sw1", "ip": "10.0.1.1", "version": "1.2", "vendor": "cisco"}

# display parts of the dictionary
print(switch["hostname"])
print(switch["ip"])

# request a fake key
# print(switch["lynx"])

print("first test -.get()")
print(switch.get("lynx"))

print("Second test - .get()")
print(switch.get("lynx", "The key is in another castle!"))

print("Third test - .get()")
print(switch.get("version"))

print("Fourth test - .keys()")
print(switch.keys())

print("Fifth test - .values()")
print(switch.values())

print("Sixth test - .pop()")
switch.pop("version") # removes the key (and value) pair
print(switch.keys())
print(switch.values())

print("Seventh test - add a new value")
switch["adminlogin"] = "karl08"
print(switch.keys())
print(switch.values())

print("Eighth test - add a new value")
switch["password"] = "qwerty"
print(switch.keys())
print(switch.values())

print(switch["adminlogin"])
