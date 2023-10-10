#!/usr/bin/python3

for i in range(99):
    print("{}{}, ".format(int(i / 10) % 10, i % 10), end="")
print("99")
