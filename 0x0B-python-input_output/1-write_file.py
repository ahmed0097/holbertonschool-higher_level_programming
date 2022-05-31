#!/usr/bin/python3
""" function that writes a string to a text file """


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8)
    and returns the number of characters written"""
    with open('my_first_file.txt', 'w+', encoding='utf-8') as f:
        f.write(text)
        return (len(text))
