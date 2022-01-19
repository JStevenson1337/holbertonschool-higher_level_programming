#!/usr/bin/python3


class Piza:
    def __init__(self, tops=[], sauce="",  diameter=0):
        self.tops = tops
        self.sauce = sauce
        self.diameter = diameter
        self.num_pizza += 1

    def __str__(self):
        return "Pizza with " + str(self.tops) + " and " + self.sauce + " sauce"