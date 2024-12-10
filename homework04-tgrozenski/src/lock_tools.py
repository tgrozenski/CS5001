""" 
This file contains information about the
locks that need breaking.
"""
from typing import Union,List

from random import randint # randint provides a random number in a range

# STUDENTS: Do NOT modify this file
# However, you will use some of the functions. 
# most notably: get_lock_type, check_solution
# you are also free to use the COMBO and PATTERN global variables 


COMBO = "COMBO"
PATTERN = "PATTERN"

__LOCK_OPTIONS = [COMBO, PATTERN]

__PATTERNS = [  # this is actually a really bad way, but the better why to come up with pattern option would provide a solution.
    "",
    "x",
    "x x\n x \nx x",
    "x   x\n x x \n  x  \n x x \nx   x",
    "x     x\n x   x \n  x x  \n   x   \n  x x  \n x   x \nx     x",
    "x       x\n x     x \n  x   x  \n   x x   \n    x    \n   x x   \n  x   x  \n x     x \nx       x",
    "x         x\n x       x \n  x     x  \n   x   x   \n    x x    \n     x     \n    x x    \n   x   x   \n  x     x  \n x       x \nx         x",
    "x           x\n x         x \n  x       x  \n   x     x   \n    x   x    \n     x x     \n      x      \n     x x     \n    x   x    \n   x     x   \n  x       x  \n x         x \nx           x",
]

MAX_PATTERN_SIZE = len(__PATTERNS)*2 - 1

# You will learn more about
# classes and objects in the future. It is a
# to combine information with actions (methods), 
# and also essentially create your own times. 
# In python, you are already using 'objects' when you use str.
class Lock():
    """
    A object that represents a lock.
    """

    def __init__(self, lock_type: str, solution: Union[str, int]) -> None:
        """
        Creates a new lock object. A lock needs a type
        and the solution. 

        Args:
            type (str): the type of lock (COMBO or PATTERN)
            solution (Union[str, int]): the solution to compare against
        """
        self.__lock_type = lock_type
        if type(solution) == str:
            self.__solution = solution.strip() # remove any extra spaces
        else:
            self.__solution = solution
        self.__open = False

    def check_solution(self, test: Union[str, int]) -> bool:
        """
        Checks a guess for the lock type to see if it is the correct solution.

        Args:
            test (Union[str, int]): the potential solution to check against

        Returns:
            bool: True if the solution matches, False otherwise
        """
        if type(test) == str:
            test = test.strip() # remove any extra spaces
        self.__open = self.__solution == test 
        return self.__open

    def get_type(self) -> str:
        f"""Gets the type of the lock. 
        
        For now, the options include {COMBO} or {PATTERN}

        Returns:
            str: one of the solution options {COMBO} or {PATTERN}
        """
        return self.__lock_type
    
    def is_open(self)-> bool:
        """Confirms if the lock is open or closed.

        Returns:
            bool: True if open, False if closed
        """
        return self.__open

    def __str__(self) -> str:
        """Builds a string representation of the lock.

        Returns:
            str: the lock type, if it is open, and the solution
        """
        return f"Lock: {self.__lock_type}\nOpen: {self.__open}\nSolution:\n{self.__solution}\n" 
    
    def __repr__(self) -> str:
        """Builds a string representation of the lock.

        Returns:
            str: the lock type, if it is open, and the solution
        """
        return self.__str__()

def __build_random_lock() -> Lock: 
    """ Build a random lock to be stored with the door.
    
    Returns:
        (Lock): a type of lock with a solution and type associated with it.
    """
    lock_type = __LOCK_OPTIONS[randint(0, 1)]
    if lock_type == PATTERN:
        solution = __PATTERNS[randint(0, len(__PATTERNS)-1)]
    else:
        solution = randint(0, 100)
    return Lock(lock_type, solution)


CURRENT_DOOR : List[Lock]= []


def get_lock_type(lock_id: int) -> str:
    f"""
    Gets the type of lock based on the lock ID.

    Often this is better done by attaching this function
    to an object, but as we haven't learned objects yet, using this
    as a basic function.

    Args:
        lock_id (int): the lock id out of all the locks on the door

    Returns:
        str: the lock type {COMBO} or {PATTERN} or '' for an invalid ID
    """
    if lock_id < len(CURRENT_DOOR):
        return CURRENT_DOOR[lock_id].get_type()
    return ''

def check_solution(lock_id: int, solution: Union[int, str]) -> bool:
    """
    Checks the lock with the lock_id based on the given
    solution.

    Args:
        lock_id (int): the lock to check against
        solution (Union[int, str]): the solution to check

    Returns:
        bool: True if passes, False if fails or error (like invalid lock id)
    """
    if lock_id < len(CURRENT_DOOR):
        return CURRENT_DOOR[lock_id].check_solution(solution)
    return False

def new_door() -> int:
    """
    Builds a new door

    Returns:
        int: the total number of locks on the door.    
    """
    global CURRENT_DOOR # setup so this is the global variable
    CURRENT_DOOR = []
    locks = randint(1, 10)
    current = 0
    while current < locks:
        CURRENT_DOOR.append(__build_random_lock())
        current += 1
    return locks

def is_open() -> bool:
    """
    Checks to make sure all the locks are unlocked on the door

    Returns:
        (bool): True if all locks are open, False otherwise
    """
    return all([x.is_open() for x in CURRENT_DOOR])


def get_single_combo() -> Lock:
    """Mainly used for unit testing, but generates a door with a single combo lock.

    Returns:
        (Lock): the lock 
    """
    global CURRENT_DOOR
    CURRENT_DOOR = [Lock(COMBO, randint(0, 100))]
    return CURRENT_DOOR[0]

def get_single_pattern() -> Lock:
    """Mainly used for unit testing, but generates a door with a single pattern lock.

    Returns:
        (Lock): the lock 
    """
    global CURRENT_DOOR
    CURRENT_DOOR = [Lock(PATTERN, __PATTERNS[randint(0, len(__PATTERNS)-1)])]
    return CURRENT_DOOR[0]