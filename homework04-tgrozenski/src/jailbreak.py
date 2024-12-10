"""
Homework 04 - JailBreak

Student: Tyler Grozenski
Semester: Fall 2024

This assignment focuses on learning while loops. It
is inspired by

Think Like a Coder ep1 Lesson by Alex Rosenthal, directed by Kozmonot Animation Studio.

https://www.youtube.com/watch?v=KFVdHDMcepw&list=PLJicmE8fK0EgogMqDYMgcADT1j5b911or&index=2
"""
from random import randint
from lock_tools import COMBO, PATTERN, MAX_PATTERN_SIZE, check_solution, is_open, \
    get_lock_type, new_door, get_single_combo, get_single_pattern
# by importing these functions and variables, you can use them directly in your code
# for example:
#  if get_lock_type(val) == COMBO:
#      do something
# get_single_combo(), and get_single_pattern() will help with interactive testing (see readme)


def unlock_combo_lock(lock_id: int) -> int:
    """
    Checks possible combinations for a combo lock, until
    the correct solution is found.

    Args:
        lock_id (int): the lock to check

    Returns:
        (int): the solution to the lock, or minus 1 if not found
    """

    attempt: int = 0
    while True:
        if (check_solution(lock_id, attempt)):
            return attempt
        attempt += 1


def draw_x(dimensions: int) -> str:
    """
    Takes in the dimensions of the x and returns a string with the x made

    Args:
        dimensions (int): the X by Y dimensions of the X

    Returns:
        A string based on the argument dimensions  
    """
    x = ''
    border_whitespace: int = 0
    center_whitespace: int = dimensions - 2
    top_half: bool = True
    space: str = ' '

    for _ in range(dimensions):
        # we have reached the center of the x
        if (center_whitespace <= 0):
            x += (border_whitespace * space) + "x" + (border_whitespace * space)
            top_half = False
            center_whitespace = 1
            border_whitespace -= 1
        # we are on the top or bottom of the x
        else:
            x += (" " * border_whitespace + "x" + (center_whitespace * space) 
                  + "x" + border_whitespace * space)
            if (top_half):
                center_whitespace -= 2
                border_whitespace += 1
            else:
                center_whitespace += 2
                border_whitespace -= 1
        x += "\n"
    return x


def unlock_pattern_lock(lock_id: int) -> str:
    """
    Checks possible patterns for a pattern lock, until
    the correct solution is found.

    Args:
        lock_id (int): the lock to check

    Returns:
        str: The pattern solution to the lock
    """

    attempt: int = 1
    while True and attempt < MAX_PATTERN_SIZE:
        if (check_solution(lock_id, draw_x(attempt))):
            return draw_x(attempt)
        attempt += 2
    empty: str = ''
    check_solution(lock_id, '')
    return ''


def open_door(num_locks: int) -> bool:
    """
    Opens a door with a number of locks. The door is opened by
    guessing the correct solution to each lock.

    Args:
        num_locks (int): the number of locks on the door

    Returns:
        bool: True if the door is opened, False otherwise
    """
    for lock_id in range(num_locks):
        lock_type = get_lock_type(lock_id)
        print(f"Lock #{lock_id}, LockType {lock_type}")
        solution = None
        if (lock_type == COMBO):
            solution = unlock_combo_lock(lock_id)
            print(__FEEDBACK_MESSAGE.format(lock_type=lock_type, lock_id=lock_id, solution=solution))
        elif (lock_type == PATTERN):
            solution = unlock_pattern_lock(lock_id)
            print(__FEEDBACK_MESSAGE.format(lock_type=lock_type, lock_id=lock_id, solution=solution))
    return is_open()


def main():
    """ Starting point for the program. """
    print(__WELCOME_MESSAGE)
    total_doors = randint(1, 6)  # generate a random number of doors
    counter = 0
    while counter < total_doors:
        locks: int = new_door()
        if not open_door(locks):
            print(__TRAPPED_MESSAGE)
            print("there are : ", total_doors, "doors, counter = ", counter)
            return
        counter += 1
    print("there are : ", total_doors, "doors, counter = ", counter)
    print(__GOODBYE_MESSAGE)


__WELCOME_MESSAGE = """Hello explorer! You have been captured and placed in a jail cell.
The only way to escape is to open the door. Make use of your infobot to help you escape."""
__GOODBYE_MESSAGE = "Congratulations! You have escaped the jail cell. You are now free."
__OPENING_DOOR_MESSAGE = "Opening door number: {counter} with {locks} locks."
__TRAPPED_MESSAGE = "You have been trapped. Better luck next time. (check for errors in your code)"
__FEEDBACK_MESSAGE = "Opened lock {lock_type} {lock_id} with solution\n{solution}"


if __name__ == "__main__":
    main()
