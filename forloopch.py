# for i in range(1,10 + 2):
#     for j in range(1, i + 1):
#         print("*", end="")
#     print()

# for x in range(0,5):
#     for j in range(0, x+1):
#         print("*")
# print()

counter = 0
for x in range(5):
    counter += 1
    print("* " * counter)

for x in range(5):
    counter -= 1
    print("* " * counter)
