"""
Homework 2: Where to live

Course:   CS 5001
Semester: Fall 2024 
Student: Tyler Grozenski 

An application that provides recommendations on where to live based on temp ranges. 

"""

# Remember, keep it simple. You are really working on three different problems to solve
# One for each function you are completing/working on.


def get_number(prompt: str) -> int:
    """
    Gets a whole number based on the prompt given. 

    Warning: does no error checking (so assumes client enters the correct input).

    Examples:
        Assume 0 is entered by the client
        >> get_number("Enter a number between 0 and 5: ")      # doctest: +NORMALIZE_WHITESPACE
        Enter a number between 0 and 5: 
        0

        Assume -100 is entered by the client
        >> get_number("Enter a temp: ")                        # doctest: +NORMALIZE_WHITESPACE
        Enter a temp:
        -100

    Args:
        prompt (str): The prompt you want displayed

    Returns:
        int: a whole number
    """

    number_string: str

    while (True):
        number_string = input(prompt)
        try:
            # Filtering out extreme inhospitable temps and non number temps
            temperature: int = int(number_string)
            if (temperature < 60 and temperature > -60):
                return temperature
            else:
                print("Please enter a temperature between 60 and -60 C")
        except ValueError:
            print("Please enter a number")


# Note: the Examples in the docstrings are simple tests. We will learn
# how to build them ourselves and test against them in the future. 
# For now, use the examples to help you think through your logic and ask yourself did 
# we cover every "case"/situation


def check_lower(first: int, second: int) -> bool:
    """
    Checks to see if first is lower or equal to y. 

    Examples: 
        >>> check_lower(10, 12)
        True
        >>> check_lower(12, 11)
        False
        >>> check_lower(10, 10)
        True

    Args:
        first (int): the first value
        second (int): the second value

    Returns:
        bool: True if first is lower than second
    """
    return True if first <= second else False


# if you find yourself trying to use stuff we haven't taught you
# you are probably making it too complicated. 
def get_cities(low: int, high: int) -> str:
    r"""Builds a string of cities separated by a new line character (\n)
    that fall within a given temperature.  


    | City | High | Low |
    | Beijing | 33 | -8 |
    | Boston | 28 | -7 |
    | Honolulu | 32 | 13 |
    | San Francisco | 27 | 6 |
    | Vancouver | 24  | 2 |

    Examples:
        >>> get_cities(-10, 28)
        'Boston\nSan Francisco\nVancouver\n'
        >>> get_cities(0, 20)
        'Unknown'
        >>> get_cities(12, 34)
        'Honolulu\n'
        >>> get_cities(5, 34)
        'Honolulu\nSan Francisco\n'

    Args:
        low (int): the lower temperature 
        high (int): the higher temperature

    Returns:
        str: a string of cities separated by \n or unknown
    """

    list: str = ''

    if (low <= -7 and high >= 28):
        list += "Boston\n"
    if (low <= 13 and high >= 32):
        list += "Honolulu\n"
    if (low <= 6 and high >= 27):
        list += "San Francisco\n"
    if (low <= 2 and high >= 24):
        list += "Vancouver\n"
    if (low <= -8 and high >= 33):
        list += "Beijing\n"
    if (len(list) == 0):
        list += "Unknown"

    return list


def main():
    """
    Asks the client for two temperatures. Based on the values, it provides cities
    that meets the conditions. Temperatures are whole numbers only.

    | City | High | Low |
    | Beijing | 33 | -8 |
    | Boston | 28 | -7 |
    | Honolulu | 32 | 13 |
    | San Francisco | 27 | 6 |
    | Vancouver | 24  | 2 |

    Values can be in any order.

    Examples:
        >> main()                                       # doctest: +NORMALIZE_WHITESPACE
        Enter a temperature: 28
        Enter a second temperature: -10
        Boston
        San Francisco
        Vancouver
        >> main()                                       # doctest: +NORMALIZE_WHITESPACE
        Enter a temperature: 0
        Enter a second temperature: 20
        Unknown    
    """
    temp1 = get_number("Enter a temperature: ")
    temp2 = get_number("Enter a second temperature: ")

    if check_lower(temp1, temp2):
        low = temp1 
        high = temp2
    else:
        high = temp1
        low = temp2

    cities = get_cities(low, high)

    print(cities.strip())  # .strip() removes leading and trailing whitespace

    again = input("Run again (y or n)? ")
    if again.strip().lower() == 'y':
        main()  # discussion item: what does this do?
    else: 
        print("Good luck on the move!")


if __name__ == "__main__":
    main()

    # flowchart TD
    # A[Start, Init string to build] -->
    # C[Low <= -7 and High >= 33] 
    # C-- false --> E[Boston not added] --> F
    # C-- true --> D[Boston added] --> F
    # F[Low <= 15 and High >= 32] 
    # F-- false --> H[Honolulu not added] --> J
    # F-- true --> I[Honolulu added] --> J
    # J[Low <= 6 and High >= 27]
    # J -- true--> K[San Francisco added] -->M
    # J --false-->L[San Francisco not added] --> M
    # M[Low <= 2 and High >= 24]
    # M--true-->N[Vancouver Added] -->P
    # M--false-->O[Vancouver not Added]-->P
    # P[Low <= -8 and High >= 33]
    # P--true-->Q[Beijing added] -->S
    # P--false-->R[Beijing not added]-->S
    # S[String length is 0?] 
    # S--true-->X[add unknown to string]-->U 
    # S--false-->Y[dont add unknown] -->U
    # U[End, return string]
