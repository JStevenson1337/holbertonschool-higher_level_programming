#!/usr/bin/python3
"""
    Write a script that reads stdin line
    by line and computes metrics:
"""
import sys
import statistics


def main():
    """
        Write a script that reads stdin line
        by line and computes metrics:
    """
    if len(sys.argv) == 1:
        print("Mean: {}".format(statistics.mean(sys.stdin.readlines())))
    else:
        print("Mean: {}".format(statistics.mean(sys.argv[1:])))


