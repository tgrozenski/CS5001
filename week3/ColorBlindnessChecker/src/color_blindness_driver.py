""" 
This application is an interactive application
that can check if color codes would be difficult for 
different types of color blindness to see. 

STUDENTS: you do not have to modify this file. 

Instead run the file *after* you have passed all your tests in color_tester.py.

"""

from color_tester import *


def validate_html_hex(hex_str: str) -> bool:
    """Validates if the input is a valid HTML hex value starting with #

    Examples:
        >>> validate_html_hex("#FF0000")
        True
        >>> validate_html_hex("#00FF00")
        True
        >>> validate_html_hex("#0000FF")
        True
        >>> validate_html_hex("#123abc")
        True
        >>> validate_html_hex("#GHIJKL")
        False
        >>> validate_html_hex("FF0000")
        False
        >>> validate_html_hex("#FF000")
        False
        >>> validate_html_hex("#FF00000")
        False


    Args:
        hex_str (str): the input string to validate

    Returns:
        bool: True if the input is a valid HTML hex value, False otherwise
    """
    hex_str = hex_str.lower()
    if hex_str.startswith("#") and len(hex_str) == 7:
        return all(c in "0123456789ABCDEFabcdef" for c in hex_str[1:])
    return False


def html_hex_to_rgb(hex_str: str) -> tuple:
    """Converts an HTML hex string to a tuple  of RGB

    Examples:
        >>> html_hex_to_rgb("#FF0000")
        (255, 0, 0)
        >>> html_hex_to_rgb("#00FF00")
        (0, 255, 0)
        >>> html_hex_to_rgb("#0000FF")
        (0, 0, 255)
        >>> html_hex_to_rgb("#123abc")
        (18, 58, 188)
    

    Args:
        hex_str (str): an html hex string (starts with #)

    Returns:
        tuple: whole number values of RGB
    """
    hex_str = hex_str.lstrip('#')
    red = int(hex_str[0:2], 16)
    green = int(hex_str[2:4], 16)
    blue = int(hex_str[4:6], 16)
    return red, green, blue


def print_html_values(red: int, green: int, blue: int) -> None:
    """Prints the HTML values for the color as
    the standard value, the Protanopia value, the Deuteranopia value,
    and the Tritanopia value. 

    Examples:
        >>> print_html_values(255, 0, 0)       # doctest: NORMALIZE_WHITESPACE
        Standard:    #ff0000
        Protanopia:  #000000
        Deuteranopia:    #ff0000
        Tritanopia:  #ff0000

        >>> print_html_values(0, 255, 0)        # doctest: NORMALIZE_WHITESPACE
        Standard:    #00ff00
        Protanopia:  #000000
        Deuteranopia:    #000000
        Tritanopia:  #00ff00

        >>> print_html_values(0, 0, 255)        # doctest: NORMALIZE_WHITESPACE
        Standard:    #0000ff
        Protanopia:  #0000ff
        Deuteranopia:    #0000ff
        Tritanopia:  #000000

        >>> print_html_values(18, 58, 188)       # doctest: NORMALIZE_WHITESPACE
        Standard:    #123abc
        Protanopia:  #0000bc
        Deuteranopia:    #0000bc
        Tritanopia:  #123a00

    Args:
        red (int): red color value
        green (int): green color value
        blue (int): blue color value
    """
    print("\tStandard:\t", rgb_to_hex(red, green, blue))
    print("\tProtanopia:\t", rgb_to_hex_protanopia(red, green, blue))
    print("\tDeuteranopia:\t", rgb_to_hex_deuteranopia(red, green, blue))
    print("\tTritanopia:\t", rgb_to_hex_tritanopia(red, green, blue))


def get_html_hex() -> str:
    """Gets an HTML Hex string from the client, and validates to make sure it is a valid hex.
    
    Returns:
        str: a valid html hex string
    """
    hex_str = input("HTML color value (ex: #ffffff): ")
    if not validate_html_hex(hex_str):
        print("Invalid color value, try again")
        return get_html_hex()
    return hex_str


def main():
    """Main entry point of the program."""
    print("Welcome to color tester, please enter two HTML formatted colors (ex: #ffffff)")
    color1 = get_html_hex()
    color2 = get_html_hex()

    red1, green1, blue1 = html_hex_to_rgb(color1)
    red2, green2, blue2 = html_hex_to_rgb(color2)

    print()
    print("Color 1 data:")
    print_html_values(red1, green1, blue1)

    print("Color 2 data:")
    print_html_values(red2, green2, blue2)

    print()

    fails = get_fails(red1, green1, blue1, red2, green2, blue2)

    if fails:
        print(f"The colors are too similar, as they fail tests for:\n{fails.strip()}")
    else:
        print("Your colors are good!")




if __name__ == "__main__":
    main()
