#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    num_of_args = len(argv)
    arg_count = 1

    if argv is not True:
        print("{} arguments.".format(num_of_args))
    else:
        print("{:d} arguments:".format(num_of_args))
    for i in argv:
        print("{:d}: {}".format(arg_count, i))
        arg_count += 1
