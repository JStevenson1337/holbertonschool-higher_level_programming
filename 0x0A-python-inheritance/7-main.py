#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

bg = BaseGeometry()

integer_validator("my_int", 12)
integer_validator("width", 89)
#
#
integer_validator("name", "John")
#
#
integer_validator("age", 0)



integer_validator("distance", -4)

