#!/usr/bin/python3
for c in range(97, 121):
    if (chr(c) == 'e') | (chr(c) == 'q'):
        continue
    else:
        print(chr(c), end = "")
print(chr(122), end= "")
