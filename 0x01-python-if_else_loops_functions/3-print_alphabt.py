#!/usr/bin/python3
for c in range(ord('a'), ord('z')):
    if ((c == 101) | (c == 113)):
        continue
    else:
        print(chr(c), end = "")
