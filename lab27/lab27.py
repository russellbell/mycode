# # #!/usr/bin/env python3
# # ######## EXPLORE READ ##########
# # ## create file object in "r"ead mode
# # configfile = open("vlanconfig.cfg", "r")
# #
# # ## display file to the screen - .read()
# # print(configfile.read())
# #
# # ## close file
# # configfile.close()
#
# ######## EXPLORE READLINES ##########
# ## re-create file object to explore new method
# configfile = open("vlanconfig.cfg", "r")
#
# # ## make a list of file lines - .readlines()
# configlist = configfile.readlines()
# # print(configlist, end="")
#
# # Iterate thrhough configlist
# for x in configlist:
#     print(x, end="")
#
# ## Always close your file
# configfile.close()

# #!/usr/bin/env python3
# ## create file object in "r"ead mode
# configfile = open("vlanconfig.cfg", "r")
#
# ## display file to the screen - .read()
# configblog = configfile.read()
#
# ## break configblog across line boundaries (strips out \n)
# configlist = configblog.splitlines()
#
# ## display list with no "\n"
# print(configlist)
#
# ## Always close your file
# configfile.close()

#!/usr/bin/env python3
## create file object in "r"ead mode
with open("vlanconfig.cfg", "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()

## file was just auto closed (no more indenting)

## display list with no "\n"
print(configlist)
