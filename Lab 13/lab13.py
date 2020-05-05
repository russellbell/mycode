#!/usr/bin/env python3

def main():
    # create a small string
    lilstring = "Alta3 Research offers classed on Python coding"
    newlist = lilstring.split(" ")  # this returns a list
    print(newlist)

    myiplist = ["192", "168", "0", "12"]
    singleiplist = ".".join(myiplist)
    print(singleiplist)


main()
