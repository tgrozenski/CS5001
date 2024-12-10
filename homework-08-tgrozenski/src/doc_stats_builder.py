"""
Homework 07: Document Statistics Builder
===========================
Course:   CS 5001
Student:  Tyler Grozenski

Functions for reading document stats. They all assume a 'document' is
a tuple or list of strings, where each string is a line of the document.

For example:
    ('Hello', 'World') is the document
    Hello
    World


    ('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho')
    An old silent pond...
    A frog jumps into the pond—
    Splash! Silence again.
    - Matsuo Basho

"""

from word_lib import clean_word, count_vowels, is_palindrome


def get_number_lines(lines: tuple) -> int:
    """
    Gets the number of lines in the document.

    Examples:
        >>> get_number_lines(('Hello', 'World'))
        2
        >>> get_number_lines(('line one with writing this is how so many words', 'this is line two in the tuple ect. ect.', 'this is line three in the tuple'))
        3
        >>> get_number_lines(('', '', '', '', '', '', '', '', '', '', ''))
        11

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of lines in the document
    """
    return lines.__len__()


def get_number_words(lines: tuple) -> int:
    """
    Gets the number of words in the document.
    Note, make sure to clean the words before counting them,
    and an 'empty' word should not be counted.

    Examples:
        >>> get_number_words(('Hello', 'World'))
        2
        >>> get_number_words(('Aloha!', '-', 'World'))
        2
        >>> get_number_words(('this!', '-', 'world'))
        2
        >>> get_number_words(('this sentence should have six words &@^%$$ ()""$', '-', 'this sentence thr$$'))
        9
        >>> get_number_words(('&*(*(&(*&* *()*(&@ ^&^#&@ #### #####))))', '-', '&&&&& ----- $$$$$'))
        0

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of words in the document
    """
    count = 0
    for words in lines:
        for word in words.split():
            if (clean_word(word) != ''):
                count += 1
    return count


def get_vowel_count(lines: tuple) -> int:
    """
    Gets the number of vowels in the document.

    Examples:
        >>> get_vowel_count(('Hello', 'World'))
        3
        >>> get_vowel_count(('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho'))
        24
        >>> get_vowel_count(('Lorem ipsum dolor sit amet', 'consectetur adipiscing elit.', 'Aenean nec tortor eu est' 'volutpat condimentum'))
        36

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of vowels in the document
    """
    count = 0
    for words in lines:
        for word in words.split():
            count += count_vowels(clean_word(word))
    return count


def get_word_palindromes(lines: tuple) -> int:
    """
    Gets the number of palindromes in the document. Ignores punctuation.

    Examples:
        >>> get_word_palindromes(('Hello', 'World'))
        0
        >>> get_word_palindromes(('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho'))
        1
        >>> get_word_palindromes(('raceCar', 'kayak!', 'sator arepo tenet opera rotas!'))
        3
        >>> get_word_palindromes(('m/a/d/a/m', 'cake!', 'Lepers Repel...', 'non lemons snomel non'))
        3

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of palindromes in the document
    """
    count = 0
    for words in lines:
        for word in words.split():
            if (is_palindrome(clean_word(word))): 
                count += 1
    return count


def get_sentence_palindromes(lines: tuple) -> int:
    """
    Gets the number of palindromes in the document. Ignores punctuation.

    Examples:
        >>> get_sentence_palindromes(('Hello', 'World'))
        0
        >>> get_sentence_palindromes(('An old silent pond...', 'A frog jumps into the pond—', 'Splash! Silence again.', '- Matsuo Basho'))
        0
        >>> get_sentence_palindromes(('A raceCar', 'A kayak!', 'sator arepo tenet opera rotas!'))
        1
        >>> get_sentence_palindromes(('m/a/d/a/m', 'cake!', 'Leper Repel...', 'non lemons snomel non'))
        3

    Args:
        lines (tuple): the lines of the document

    Returns:
        int: the number of palindromes in the document
    """
    count = 0
    for line in lines:
        if (is_palindrome(clean_word(line))):
            count+=1
    return count


# just running the file will automatically run doctest 
if __name__ == "__main__":  # if doctest is not installed, comment out these lines
    import doctest

    doctest.testmod(verbose=True)
