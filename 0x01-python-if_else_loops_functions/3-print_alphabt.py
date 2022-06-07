#!/usr/bin/python3
for char in range(97, 123):
    if char != 'e' and char != 'q':
        print("{:c}".format(char), end="")
