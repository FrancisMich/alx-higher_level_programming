#!/usr/bin/python3
""" A file that executes a function that appends a line """


def append_after(filename="", search_string="", new_string=""):
    """ Function that appends a text when a string is found
    Args:
        filename: the filename
        search_string: string to search for the file
        new_string: string to append file
    """

    res_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            res_line += [line]
            if line.find(search_string) != -1:
                res_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(res_line))
