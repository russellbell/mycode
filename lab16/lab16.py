# create the string hostname
# hostname = "MGT"
hostname = input("What value should we set for hostname? ")
# test logic with "if" statment
# what to do if the statement is found to be true
# if hostname == "MGT":
#     print("The hostname was found to be MTG")
if hostname.lower() == "mgt":
    print("The hostname was found to be mtg")
    print("hostname matches expected config")

print("Exiting the script.")
