# loginfail = 0
# keystone_file = open("keystone.common.wsgi", "r")
# keystone_file_lines = keystone_file.readlines()
# for line in keystone_file_lines:
#     if "- - - - -] Authorization failed" in line:
#         loginfail += 1
# print(f"The number of failed log in attempts is, {loginfail}")
# keystone_file.close()

# loginfail = 0
# keystone_file = open("keystone.common.wsgi", "r")
#
# for line in keystone_file:
#     if "- - - - -] Authorization failed" in line:
#         loginfail += 1
# print(f"The number of failed login attempts is {loginfail}")

# loginfail = 0
# with open("keystone.common.wsgi", "r") as keystone_file:
#
#     if "- - - - -] Authorization failed" in keystone_file:
#         loginfail += 1
# print(f"The number of failed login attempts is {loginfail}")

loginfail = 0

with open("keystone.common.wsgi", 'r') as kfile:
    for line in kfile:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
print(f"The number of failed log in attempts is {loginfail}")
