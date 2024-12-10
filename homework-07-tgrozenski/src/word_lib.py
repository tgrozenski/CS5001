"""
Homework 07: Library of Word Functions, all written recursively
===========================
Course:   CS 5001
Student:  Tyler Grozenski

Various functions to practice recursion.
"""
import string


def is_palindrome(word: str, reversed: str = '') -> bool:
    """
    Recursively looks at a string to determine if it is a palindrome.

    Does not remove punctuation or spaces, and assumes the word is
    already in lower case.

    Examples:
        >>> is_palindrome('racecar')
        True
        >>> is_palindrome('hello')
        False
        >>> is_palindrome('    not a palindrome tyler    ')
        False
        >>> is_palindrome('22/02/2022')
        False
        >>> is_palindrome('22022022')
        True
        >>> is_palindrome('')
        False
        >>> is_palindrome('madam noon wow')
        False
        >>> is_palindrome('wow wow wow')
        True

    Args:
        word (str): the word to check

    Returns:
        bool: True if the word is a palindrome, False otherwise
    """
    if (word == ''):
        return False

    if (len(word) == len(reversed)): 
        return reversed == word
    return is_palindrome(word, reversed + word[len(word) - (len(reversed) + 1)])


def count_vowels(word: str, count: int = 0) -> int:
    """
    Recursively counts the number of vowels in a string. Case
    does not matter.

    Examples:
        >>> count_vowels('hello')
        2
        >>> count_vowels('aeiou')
        5
        >>> count_vowels('AEZOU')
        4
        >>> count_vowels('cats and dogs')
        3

    Args:
        word (str): the word to check

    Returns:
        int: the number of vowels in the word
    """
    # base case
    if (word.__len__() <= 0):
        if (is_vowel(word)):
            return count + 1
        else:
            return count
    if (len(word) > 0 and is_vowel(word[len(word) - 1])):
        count += 1
    return count_vowels(word[:-1], count)


def is_vowel(char: str) -> bool:
    """
    determines if a vowel is present in a string of size 1 regardless of case.

    Examples:
        >>> is_vowel('a')
        True
        >>> is_vowel('E')
        True
        >>> is_vowel('z')
        False
        >>> is_vowel('p')
        False

    Args:
        char (str): the character to check

    Returns:
        bool: whether the character is a vowel or not
    """
    match char.lower():
        case 'a':
            return True
        case 'e':
            return True
        case 'i':
            return True
        case 'o':
            return True
        case 'u':
            return True
    return False


def clean_word(word: str, cleaned: str = '') -> str:
    """
    Recursively removes punctuation from a word, and reduces it to lower case.

    Examples:
        >>> clean_word('Hello!')
        'hello'
        >>> clean_word('World...')
        'world'
        >>> clean_word('This IS my Sente*~``nce with punctu@ation!')
        'thisismysentencewithpunctuation'
        >>> clean_word('this is a \\n\\t harder sentence@#$%^&')
        'thisisa\\n\\thardersentence'

    See:
        https://docs.python.org/3/library/stdtypes.html#str.isalnum


    Args:
        word (str): the word to remove punctuation from

    Returns:
        str: the word without punctuation
    """
    # once the clean word is built up to the same size
    if (len(word) == len(cleaned)):
        return cleaned
    current_char: str = str(word[len(cleaned)])
    if (current_char not in string.punctuation and current_char != ' '): 
        return clean_word(word, cleaned + current_char.lower())
    else:
        # keep both the same length for the base case to work
        return clean_word(word[1:], cleaned)


# Just running this file will run the doctests
if __name__ == "__main__":  # if doctest is not installed, comment out these lines
    # import doctest
    # doctest.testmod(verbose=True)
    print(clean_word('aloha world'))
