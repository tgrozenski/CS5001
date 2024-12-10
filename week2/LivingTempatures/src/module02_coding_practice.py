"""Coding practice problems for Module 02 for CS 5001.

Semester: Fall 2024 
Name: Tyler Grozenski 
"""


# While it seems tedious to add all the 
# docstrings when it is on the website
# They help you think through the logic as you type them out.
# plus it will help as your functions get more complicated. 



# problem found at: https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
def hacker_rank_if_else(n) -> str:
    """
    Prints 'Weird' if an number is Odd or an even between 6 and 20.
    Prints 'Not Weird' if even between 1-5, or an even number greater than 20   
    """
    if(n >= 6 and n <= 20) and (n % 2 == 0):
            return 'Weird'
    elif(n % 2 != 0):
        return 'Weird'
    if(n >= 1 and n <= 5) and (n % 2 == 0):
            return 'Not Weird'
    elif(n > 20 and n % 2 == 0):
        return 'Not Weird'

# problem found at https://codingbat.com/prob/p195669
def cigar_party(cigars : int, is_weekend: bool) -> bool:
    """Summary from codingbat
        
    When squirrels get together for a party, they like to have cigars. 
    A squirrel party is successful when the number of cigars is 
    between 40 and 60, inclusive. Unless it is the weekend, in which case 
    there is no upper bound on the number of cigars. 
    Return True if the party with the given values is successful, or False otherwise.


    Examples:
        >>> cigar_party(30, False)
        False
        >>> cigar_party(50, False)
        True
        >>> cigar_party(70, True)
        True

    Args:
        cigars (int): number of cigars
        is_weekend (bool): if it is the weekend or not

    Returns:
        bool: True or False indicating a good squirrel party
    """
    pass # your solution would be here

def main():
    for i in range(30):
        print(f"{hacker_rank_if_else(int(i))} {i}")

if __name__ == "__main__":
    main()