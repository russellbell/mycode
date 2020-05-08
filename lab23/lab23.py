#!/usr/bin/env python3

# iplist = ["10.1.1.1", "10.2.2.2", "10.3.3.3"]
#
# for ip in iplist:
#     print(ip)

# dnsfile = open("dnsservers.txt", "r")
# dnslist = dnsfile.readlines()
# for srv in dnslist:
#     print(srv, end="")
# dnsfile.close()

# with open("dnsservers.txt", "r") as dnsfile:
#     dnslist = dnsfile.readlines()
#     for srv in dnslist:
#         print(srv, end="")

import uuid

howmany = int(input("How man UUIDs should be generated? "))

print("Generating UUIDs......")

for rando in range(howmany):
    print(uuid.uuid5(uuid.NAMESPACE_DNS, "bell.com"))

# with open("dnsservers.txt", "r") as dnsfile:
#     for svr in dnsfile:
#         svr = svr.rstrip("\n")
#
#         if svr.endswith("org"):
#             with open("org-domain.txt", "a") as svrfile:
#                 svrfile.write(svr + "\n")
#         elif svr.endswith("com"):
#             with open("com-domin.txt", "a") as svrfile:
#                 svrfile.write(svr + "\n")
