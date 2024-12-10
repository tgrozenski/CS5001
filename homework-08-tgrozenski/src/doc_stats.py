"""
Homework 08: Document Statistics Program
===========================
Course:   CS 5001
Student:  Tyler Grozenski

Update this file by adding required functions.

Small program that builds document statistics from a command line input.
"""
import os 
import sys

from doc_stats_builder import (
    get_number_lines,
    get_number_words,
    get_sentence_palindromes,
    get_vowel_count,
    get_word_palindromes,
)
from doc_view import get_input, print_stats
from doc_file_view import read_file, write_json_file


def get_stats_block(doc: tuple) -> tuple:
    """
    Builds a tuple of statistics from a tuple of strings.

    Args:
        doc (tuple): A tuple of strings.

    Returns:
        tuple: A tuple of statistics in the order of lines, words, vowels,
        palindromes and sentence palindromes.
    """
    return (
        get_number_lines(doc),
        get_number_words(doc),
        get_vowel_count(doc),
        get_word_palindromes(doc),
        get_sentence_palindromes(doc),
    )


def check_args_for_help(args: list) -> bool:
    """
    Checks to see if -h is in the args, if so, prints the help message and returns True.

    Args:
        args (list): A list of command line arguments.

    Returns:
        bool: True if -h is in the args, False otherwise.
    """
    if "-h" in args or "--help" in args:
        print_help()
        return True
    return False


def print_help() -> None:
    """
    Prints the help message for the program.
    """
    print("Usage: python doc_stats.py [-h|--help] [-f filename]  [-o filename]")
    print("Options:")
    print("  -f filename: The name of the file to analyze.")
    print("  -h or --help: Print this help message and exit")
    print("  -o filename: The name of the file to write the output to.",  
          "If filename is not provided, but -o is used then the default file", 
          "name is out.txt.")

# end provided functions
# edit the following functions


def get_input_file(args: list) -> str:
    """
    Checks to see if -f file_name is in the args, if so, returns the file name,
    or returns an empty string if it is not there.

    On a bad format, such as -f (nothing) or -f followed by a -- or - (another flag),
    raises a ValueError.

    Args:
        args (list): A list of command line arguments.

    Returns:
        str: The file name if it exists in the args and is valid, otherwise an empty string.

    Examples:
        >>> filename = "tests/test_files/test_file.txt"
        >>> doc_stats.get_input_file(["-f", filename])
        'tests/test_files/test_file.txt'

        >>> doc_stats.get_input_file(["hello", "-o", "-f", filename])
        'tests/test_files/test_file.txt'

        >>> doc_stats.get_input_file(('cats', 'dogs', 'people', 'houses', 'things'))
        ValueError

        >>> doc_stats.get_input_file(('cats', 'dogs', '-f', '', 'things'))
        ValueError

        >>> doc_stats.get_input_file(('cats', 'dogs', '-f', None, 'things'))
        ValueError

        >>> doc_stats.get_input_file(('somearg', '-f'))
        ValueError

        >>> doc_stats.get_input_file(["hello", "-o", "-f", filename, 'args after', 'more args'])
        'tests/test_files/test_file.txt'

        >>> doc_stats.get_input_file(('somearg', '-f', '-'))
        ValueError

        >>> doc_stats.get_input_file(('somearg', '-f', '--'))
        ValueError
    """
    file_name = ''
    try:
        for i in range(args.__len__()):
            if (args[i].strip() == '-f'):
                file_name = args[i + 1].strip()
    except AttributeError:
        raise ValueError('An object of Type None encountered')
    except IndexError:
        raise ValueError('File name expected after -f')

    if (file_name == '' or file_name == '-' or file_name == '--'):
        raise ValueError('File name expected after -f')

    if (not os.path.exists(file_name)):
        raise FileNotFoundError(f"The file: {file_name} was not found")

    return file_name


def get_output_file(args: list) -> str:
    """
    Checks to see if a -o file_name is in the args, if so returns the file name or
    the empty string if it is not there.

    If -o is provided without a following file name, it uses the default 'out.txt'.

    Args:
        args (list): A list of command line arguments.

    Returns:
        str: A file name if -o is in the args, otherwise an empty string.

    Examples:
        >>> filename = "test_file.txt"
        >>> doc_stats.get_output_file(["-o", filename])
        'test_file.txt'

        >>> doc_stats.get_output_file(["hello", "-f", "look.txt", "-o", filename])
        'test_file.txt'

        >>> doc_stats.get_output_file(["hello", "-f", "look.txt", "-o", ''])
        'out.txt'

        >>> doc_stats.get_output_file(["hello", "-f", "look.txt", "-o", None])
        'out.txt'

        >>> doc_stats.get_output_file(["hello", "-f", "look.txt", "-o"])
        'out.txt'

        >>> doc_stats.get_output_file(["hello", "-f", "look.txt", "-o", 'this is an invalid file name'])
        'out.txt'

        >>> doc_stats.get_output_file(["hello", "-f", "look.txt", "o", 'no -o present'])
        ''
    """

    file_name = ''
    o_arg = False
    try:
        for i in range(args.__len__()):
            if (args[i].strip() == '-o'):
                o_arg = True
                file_name = args[i + 1].strip()
    except AttributeError:
        return "out.txt"
    except IndexError:
        return "out.txt"

    if (o_arg and '.txt' not in file_name): 
        return "out.txt"

    return file_name 


def get_user_text() -> str:
    """
    Gets user text

    Returns: string of formatted stats block
    """
    input_data = get_input()
    stats_block = (
        get_number_lines(input_data),
        get_number_words(input_data),
        get_vowel_count(input_data),
        get_word_palindromes(input_data),
        get_sentence_palindromes(input_data),
    )
    return stats_block


def main(args) -> None:
    """
    python3 doc_stats.py
    Will do the typical run you saw in Homework 07 asking for client input, and printing out to the terminal. 

    python3 doc_stats.py -f haiku.txt
    Will run your program, but instead of reading from the command line, it will read from the file haiku.txt. 

    python3 doc_stats.py -f haiku.txt -o haiku_stats.txt
    Will run your program, but instead of reading from the command line, it will read from the file haiku.txt, and 
    write the output to haiku_stats.txt. 

    python3 doc_stats.py -h
    Will print out a help message (and is already completed for you).

    Your job is to handle the `-f filename` and `-o filename` arguments, along with updating
    the main to change how the program flows based on list of strings passed into main. 
    MAKE SURE to look at the weekly team activity provided code!
    """

    if (len(args) == 1):
        print_stats(get_user_text())
    else:  # we have more than one command line arg
        output_file: str = get_output_file(args)
        stats_block: str = get_stats_block(read_file(get_input_file(args)))
        if (output_file == ''):  # print stats to terminal from input file
            print_stats(stats_block)
        else:  # print stats to output file from input file
            write_json_file(stats_block, './data/actual/' + output_file)


if __name__ == "__main__":
    main(sys.argv)
