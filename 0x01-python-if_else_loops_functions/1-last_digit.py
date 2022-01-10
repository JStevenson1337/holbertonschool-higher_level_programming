#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
if (number == 0):
    print("Last digit of {} is {} and is {}".format(number, number, number))
elif (number > 5):
    print("Last digit of {} is {} and \
is greater than 5".format(number, number % 10))
else:
    if(number > 0):
        print("Last digit of {} is {} and \
is less than 6 and not 0".format(number, number % 10))
    else:
        print("Last digit of {} is {} and is less \
than 6 and not 0".format(number, number % -10))
