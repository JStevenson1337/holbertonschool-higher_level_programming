#!/usr/bin/python3
"""Gather OS information and display it in a formatted way."""
import os
import platform



print(os.getcwd())
for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    print("Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)
    print()
