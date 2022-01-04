#!/usr/bin/python3
for c in range(97, 123):
    if (chr(c) == 'e') | (chr(c) == 'q'):
        continue
    else:
        print(chr(c), end = "")
