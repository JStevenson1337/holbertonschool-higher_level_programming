#!/usr/bin/python3


for c in range(ord('a'), ord('z') + 1):
    if ((c == 101) | (c == 113)):
        continue
    else:
        print("{}".format(chr(c)), end="")
