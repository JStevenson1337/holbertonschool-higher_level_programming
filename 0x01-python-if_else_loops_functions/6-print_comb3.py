#!/usr/bin/python3
i, j = 0, 0
while i <= 9:
    while j <= 9:
        if (i < j) & (i < 8):
            print("{}{}".format(i, j), end=', ')
        elif ((i == 8) & (j == 9)):
            print("{}{}".format(i, j), end='\n')
        j += 1
    i += 1
    j = 0
