#!/usr/bin/python3
for c in range(97, 123):
    if (chr(c) == 101) | (chr(c) == 113):
        continue
    else:
        print(chr(c), end = "");
