#!/usr/bin/python3
""" A file that defines the class Student
"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """initialize new student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ returns directory description of student"""
        return self.__dict__.copy()
