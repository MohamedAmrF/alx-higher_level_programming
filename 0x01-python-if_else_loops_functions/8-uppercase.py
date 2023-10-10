#!/usr/bin/python3
def uppercase(str):
    for i in str:
        n = ord(i)
        if ord(i) >= 97:
            i = chr(n - 32)
        else:
            i = chr(n)
        print("{}".format(i), end="")
    print()
