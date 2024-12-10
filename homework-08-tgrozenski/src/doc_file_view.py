""" 
Homework 08: File "View" For the Application
===========================
Course:   CS 5001
Student:  Tyler Grozenski

This file contains functions to help with manipulating files and JSON.
"""
import os
import sys


def read_file(file_path: str) -> tuple:
    """
    Reads in a file and returns a tuple with each line as a string.
    Each line will have leading and trailing whitespace removed.
    Empty lines are removed

    Args:
        file_path (str): The path of the file to be read.

    Returns:
        tuple: A tuple with each line of the file as a string.
    """
    lines: list = []
    file = open(file_path)

    for line in file:
        current_line = line.strip()
        if (current_line != ''):
            lines.append(current_line)

    file.close()
    return (tuple(lines))


def write_json_file(doc_stats: tuple, file_path: str) -> None:
    """
    Writes the document statistics as a JSON string to a file.


    See:
        stats_to_json

    Args:
        doc_stats (tuple | list): the document statistics
        file_path (str): The path of the file to be written.
    """

    try:
        json_str = stats_to_json(doc_stats)
    except ValueError:
        return ValueError("Value Error, Tuple length should be exactly five")
    except TypeError:
        return TypeError("Type Error, not a tuple")

    try:
        file = open(file_path, 'w')
        file.write(json_str)
        file.close()
    except FileNotFoundError:
        sys.stderr("the file", file_path, "was not found")


def stats_to_json(doc_stats: tuple) -> str:
    """
    Writes the document statistics as a JSON string, format would be:
    {"lines": 1, "words": 2, "vowels": 3, "palindromes": 4, "sentence_palindromes": 5}
    with the numbers replaced with the actual values.

    Examples:
        >>> stats_to_json((1, 2, 3, 4, 5))
        '{"lines": 1, "words": 2, "vowels": 3, "palindromes": 4, "sentence_palindromes": 5}'
        >>> stats_to_json((0, 0, 0, 0, 0))
        '{"lines": 0, "words": 0, "vowels": 0, "palindromes": 0, "sentence_palindromes": 0}'
        >>> stats_to_json((12, 102, 33, 42, 0))
        '{"lines": 12, "words": 102, "vowels": 33, "palindromes": 42, "sentence_palindromes": 0}'

    Args:
        doc_stats (tuple | list): the document statistics

    Returns:
        str: the JSON formatted string
    """

    # validate input
    if (type(doc_stats) is not tuple):
        raise TypeError('Must pass a tuple')
    if (len(doc_stats) != 5 or [x for x in doc_stats if type(x) is not int]):
        raise ValueError('Tuple must be size 5 of integers')

    format = f'"lines": {doc_stats[0]}, "words": {doc_stats[1]}, "vowels": {doc_stats[2]}, "palindromes": {doc_stats[3]}, "sentence_palindromes": {doc_stats[4]}'
    return '{' + format + '}'


if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)
