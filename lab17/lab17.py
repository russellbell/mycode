import socket

while True:
    ipchk = input("Apply IP address ")

    # a string test as true
    if ipchk == "192.168.70.1":
        print("Looks like the IP address of the Gateway was set: : " + ipchk + "This is not recommended.")

    elif ipchk:
        try:
            socket.inet_aton(ipchk)
            print("Looks like the IP address was set: " + ipchk)
            break
        except:
            print("That's not an IP.")

    else:
        print("You didn't provide input.")

print("I'm free of the loop")
