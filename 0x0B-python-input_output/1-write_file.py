#!/usr/bin/python3
"""a file that contains a function that writes to a text file"""


def write_file(filename="", text=""):
    """Function that writes to a text file in utf-8.
    Args:
        filename (str): The file name to write.
        text (str): The text to write.
    Returns:
        The text.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
