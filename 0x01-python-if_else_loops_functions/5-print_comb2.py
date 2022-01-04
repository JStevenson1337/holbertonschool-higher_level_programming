#!/usr/bin/python3
for i in range(0, 99):
    if (i < 98):
        print("{:02d}".format(i), end=', ');
    else:
        print(i, end='\n');
