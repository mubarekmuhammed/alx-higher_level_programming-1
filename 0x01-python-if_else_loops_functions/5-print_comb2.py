#!/usr/bin/python3
for num in range(0, 99):
    if num < 10:
        print("0{:d}".format(num), end=", ")
    elif num >= 10 and num < 98:
        print("{:d}".format(num), end=", ")
    else:
        print("{:d}".format(num))
