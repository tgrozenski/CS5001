"""
Student: Tyler Grozenski
Term: Fall 2024

Compares two colors, both normal, and with various color blindness conditions applied

"""
import math

MIN_DIFFERENCE = .10


def delta(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> float:
    """Uses the following formula to compare two different colors. This
    is a simplified way to compare two colors as it doesn't take
    into account hue or saturation differences. If you are curious
    about a more standard approach, one should look up the CIEDE2000 formula. 

    euclidean = (R_1 - R_2)^2 + (G_1 - G_2)^2 + (B_1 - B2)^2
    euclidean = sqrt(euclidean)  # the two lines are known as the euclidean distance and common for a lot of things
    scaled = floor(euclidean) / 441  #scales the distance between 0 and 1


    Examples:
        >>> delta(255, 255, 255, 255, 255, 255)
        0.0
        >>> delta(255, 255, 255, 0, 0, 0)
        1.0
        >>> round(delta(255, 255, 255, 127, 127, 127), 2) # round helps with floating point errors
        0.5
        >>> delta(0, 0, 0, 0, 0, 0)
        0.0

    Args:
        red_one (int): a color range between 0 and 255 representing the red for the first color
        green_one (int): a color range between 0 and 255 representing the green for the first color
        blue_one (int):a color range between 0 and 255 representing the blue for the first color
        red_two (int): a color range between 0 and 255 representing the red for the second color
        green_two (int): a color range between 0 and 255 representing the green for the second color
        blue_two (int): a color range between 0 and 255 representing the blue for the second color


    Returns:
        float: a value between 0 and 1, representing how different colors are. Lower numbers are more similar. 
    """
    return int(math.sqrt((red_one - red_two) ** 2 + 
                         (green_one - green_two) ** 2 + 
                         (blue_one - blue_two) ** 2)) / 441


def rgb_to_hex(red: int, green: int, blue: int) -> str:
    """Converts an RBG color to a HEX string value often used for HTML color pallets. 

    The conversion format string is  f"#{red:02x}{green:02x}{blue:02x}"

    Examples:
    >>> rgb_to_hex(255, 255, 255)
    '#ffffff'
    >>> rgb_to_hex(0, 0, 0)
    '#000000'
    >>> rgb_to_hex(127, 127, 127)
    '#7f7f7f'
    >>> rgb_to_Hex(255, 0, 0)
    '#ff0000'

    Args:
        red (int): red color value
        green (int): green color value
        blue (int): blue color value

    Returns:
        str: the formatted string
    """
    return f"#{red:02x}{green:02x}{blue:02x}"


# Add your functions here 
# Remember write one at a time! (we recommend start with different_colors)
# Follow - define, document, implement, and test - with every function! 


def different_colors(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> bool:
    """Compares to RGB values to see how different they are. Does not convert only compares

    Examples:
    >>> different_color(230,13,255,123,200,255)
    True
    >>> different_color(255, 255, 255, 0, 0, 0)
    True
    >>> different_color(255, 255, 255, 255, 255, 255)
    False

    Args:
        * red_one (int): a color range between 0 and 255 representing the red for the first color
        * green_one (int): a color range between 0 and 255 representing the green for the first color
        * blue_one (int):a color range between 0 and 255 representing the blue for the first color
        * red_two (int): a color range between 0 and 255 representing the red for the second color
        * green_two (int): a color range between 0 and 255 representing the green for the second color
        * blue_two (int): a color range between 0 and 255 representing the blue for the second color
    Returns:
        str: the formatted string
    """
    difference: float = delta(red_one, green_one, blue_one, red_two, green_two, blue_two)
    return (difference > MIN_DIFFERENCE)


def check_protanopia(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> bool:
    """
    ### check_protanopia
    Compares two RBG values checking to see if when the colors are seen
    by someone with protanopia, they are to similar. 

    > Protanopia is means 0 red and greens and only blues, so when comparing, all colors become their blue value only. 

    Examples:
    >>> check_protanopia(255, 255, 255, 0, 0, 0)
    True
    >>> check_protanopia(255, 255, 255, 0, 0, 225)
    False 
    >>> check_protanopia(255, 255, 255, 127, 127, 127)
    True

    Args
    * red_one (int): a color range between 0 and 255 representing the red for the first color
    * green_one (int): a color range between 0 and 255 representing the green for the first color
    * blue_one (int):a color range between 0 and 255 representing the blue for the first color
    * red_two (int): a color range between 0 and 255 representing the red for the second color
    * green_two (int): a color range between 0 and 255 representing the green for the second color
    * blue_two (int): a color range between 0 and 255 representing the blue for the second color

    Returns
    boolean: returns False if the colors are too similar when someone has protanopia
    """
    # check difference using different colors function with only blue values
    return different_colors(0, 0, blue_one, 0, 0, blue_two)


def check_deuteranopia(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> bool:
    """
    check_deuteranopia
    Compares two RBG values checking to see if when the colors are seen
    by someone with deuteranopia, they are to similar. 

    Deuteranopia means no greens


    Examples:
    >>> check_deuteranopia(255, 255, 255, 0, 255, 0)
    True
    >>> check_deuteranopia(255, 255, 255, 255, 0, 255)
    False 
    >>> check_deuteranopia(255, 255, 255, 127, 255, 127)
    True

    #### Args
    * red_one (int): a color range between 0 and 255 representing the red for the first color
    * green_one (int): a color range between 0 and 255 representing the green for the first color
    * blue_one (int):a color range between 0 and 255 representing the blue for the first color
    * red_two (int): a color range between 0 and 255 representing the red for the second color
    * green_two (int): a color range between 0 and 255 representing the green for the second color
    * blue_two (int): a color range between 0 and 255 representing the blue for the second color

    #### Returns
    boolean: returns False if the colors are too similar when someone has deuteranopia
    """
    return different_colors(red_one, 0, blue_one, red_two, 0, blue_two)


def check_tritanopia(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> bool:
    """
    check_tritanopia
    Compares two RBG values checking to see if when the colors are seen
    by someone with tritanopia, whether they are to similar. 

    > Tritanopia is when someone sees only red and green values of an RGB color scheme.

    Examples:
    >>> check_tritanopia(255, 255, 255, 0, 0, 255)
    True
    >>> check_tritanopia(255, 255, 0, 255, 255, 255)
    False 
    >>> check_tritanopia(255, 255, 255, 127, 127, 255)
    True

    Args
    * red_one (int): a color range between 0 and 255 representing the red for the first color
    * green_one (int): a color range between 0 and 255 representing the green for the first color
    * blue_one (int):a color range between 0 and 255 representing the blue for the first color
    * red_two (int): a color range between 0 and 255 representing the red for the second color
    * green_two (int): a color range between 0 and 255 representing the green for the second color
    * blue_two (int): a color range between 0 and 255 representing the blue for the second color

    Returns
    boolean: returns False if the colors are too similar when someone has tritanopia
    """
    return different_colors(red_one, green_one, 0, red_two, green_two, 0)


def rgb_to_hex_deuteranopia(red: int, green: int, blue: int) -> str:
    """
    Converts RGB color values to hexadecimal representation for individuals with deuteranopia color blindness. 
    Deuteranopia is when there is 0 green values 

    Examples:
    >>> rgb_to_hex_deuteranopia(255, 255, 255)
    #ff00ff
    >>> rgb_to_hex_deuteranopia(0, 255, 0)
    #000000
    >>> rgb_to_hex_deuteranopia(75, 100, 100)
    #4b0064


    Args:
    * red (int): The red component of the RGB color.
    * green (int): The green component of the RGB color.
    * blue (int): The blue component of the RGB color.


    Returns:

    str: The hexadecimal representation of the RGB color, adjusted for deuteranopia color blindness.
    """
    # returning rgb to hex with zero for green
    green = 0
    return rgb_to_hex(red, green, blue)


def rgb_to_hex_protanopia(red: int, green: int, blue: int) -> str:
    """
    rgb_to_hex_protanopia
    Converts RGB color values to hexadecimal representation for individuals with protanopia color blindness.
    Protanopia is when there is 0 red and greens and only blues

    Args:
    * red (int): The red component of the RGB color.
    * green (int): The green component of the RGB color.
    * blue (int): The blue component of the RGB color.

    Examples:
    >>> rgb_to_hex_protanopia(255, 255, 255)
    #ff00ff
    >>> rgb_to_hex_protanopia(0, 255, 0)
    #000000
    >>> rgb_to_hex_protanopia(75, 100, 100)
    #4b0064

    #### Returns:

    str: The hexadecimal representation of the RGB color, adjusted for protanopia color blindness.
    """
    # returning rgb to hex with zero for red and green 
    red, green = 0, 0
    return rgb_to_hex(red, green, blue)


def rgb_to_hex_tritanopia(red: int, green: int, blue: int) -> str:
    """
    rgb_to_hex_tritanopia
    # Converts RGB color values to hexadecimal representation for individuals with tritanopia color blindness.

    Tritanopia is when there is 0 blues and normal greens and reds

    Args:
    * red (int): The red component of the RGB color.
    * green (int): The green component of the RGB color.
    * blue (int): The blue component of the RGB color.

    Examples:
    >>> rgb_to_hex_tritanopia(255, 255, 255)
    #0000ff
    >>> rgb_to_hex_tritanopia(0, 255, 0)
    #000000
    >>> rgb_to_hex_tritanopia(75, 100, 100)
    #0000c8

    Returns:

    str: The hexadecimal representation of the RGB color, adjusted for tritanopia color blindness.
    """
    # returning rgb to hex no blues
    blue = 0
    return rgb_to_hex(red, green, blue)


def get_fails(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> str:
    """
    get_fails:

    Returns a list of colorblindness if the colors fail. The tests are checked in order of Protanopia, Deuteranopia, Tritanopia

    Examples:
    >>> get_fails(255, 255, 255, 0, 0, 255)
    "Protanopia\n"
    >>> get_fails(0, 0, 255, 0, 0, 0)
    "Tritanopia"
    >>> get_fails(255, 255, 255, 255, 0, 255)
    "Protanopia\nDeuteranopia\n"

    Args:
    * red_one (int): a color range between 0 and 255 representing the red for the first color
    * green_one (int): a color range between 0 and 255 representing the green for the first color
    * blue_one (int):a color range between 0 and 255 representing the blue for the first color
    * red_two (int): a color range between 0 and 255 representing the red for the second color
    * green_two (int): a color range between 0 and 255 representing the green for the second color
    * blue_two (int): a color range between 0 and 255 representing the blue for the second color

    Returns:
    str: A string of names blindness types separated by \n, or an empty string if the color is fine
    """
    fails: str = ''
    if (not check_protanopia(red_one, green_one, blue_one, red_two, green_two, blue_two)):
        fails += "Protanopia\n"
    if (not check_deuteranopia(red_one, green_one, blue_one, red_two, green_two, blue_two)):
        fails += "Deuteranopia\n"
    if (not check_tritanopia(red_one, green_one, blue_one, red_two, green_two, blue_two)):
        fails += "Tritanopia\n"
    return fails  


def main():
    # while this main isn't the primary entry point of the program
    # you can use this mean to help test as you develop, this is common practice
    if round(delta(255, 255, 255, 127, 127, 127), 2) != .50:
        print("Fail check delta expected return .5")


if __name__ == "__main__":
    main()
