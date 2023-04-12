#!/usr/bin/python3
"""a file that contains a function to append  to a text file"""


def write_file(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8).
    Args:
        filename (str): The file name to append.
        text (str): The text to write.
    Returns:
        The text.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
