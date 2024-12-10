"""
--------------------------
Homework 06: Substitution Cipher
--------------------------
STUDENT: Tyler Grozenski
SEMESTER: Fall 2024 
"""
import sys
from string import digits, ascii_letters
from random import sample

ALL_LETTERS_DIGITS = digits + ascii_letters
# use this random key if none is provided, try printing it out to see what it is
RANDOM_KEY = "".join(sample(list(ALL_LETTERS_DIGITS), len(ALL_LETTERS_DIGITS)))

ACTION_ENCRYPT = 'encrypt'
ACTION_DECRYPT = 'decrypt'

# add your functions here. you should think about how you break up your program.
def encrypt(key: str, msg: str) -> str:
    """
    Encrypts a string based on the key

    Args: 
        key (str): the key to encypt with
        msg (str): the string to be encrypted
    
    Examples:
        >>> encrypt('BEKYPfzGR8JD3jv0d5Hk9wecInOsLrAubX7WQalyUqptCM41NhmiSTZFVg62xo', 'hello, world 123')
        ToDDZ xZBDe 81J
        >>> encrypt('', 'my name is, Tyler')
        my name is, Tyler
        >>> encrypt('BEKYPfzGR8JD3jv0d5Hk9wecInOsLrAubX7WQalyUqptCM41NhmiSTZFVg62xok', 'this is an ex@mple w(th sp3ci@l ch#arac%->_')
        r5HL HL Jc vX@enwv b(r5 LnY3H@w 35#JsJ3%->_

    Returns:
        str: the encrypted string
    """
    if(key == ''):
        return msg
    encrypted_str: str = ''
    for char in msg:
        if(char in ALL_LETTERS_DIGITS):
            encrypted_str += key[ALL_LETTERS_DIGITS.find(char)]
        else:
            encrypted_str += char

    return encrypted_str


def decrypt(key: str, msg: str) -> str:
    """
    decrypts string based on the key

    Args: 
        key (str): the key to encypt with
        msg (str): the string to be decrypted
    
    Examples:
        >>> decrypt('', 'hello, world 123')
        'hello, world 123'
    Returns:
        str: the decrypted string
    """
    if(key == ''):
        return msg
    decrypted_str: str = ''
    for char in msg:
        if(char in ALL_LETTERS_DIGITS):
            decrypted_str += ALL_LETTERS_DIGITS[key.find(char)]
        else:
            decrypted_str += char
    return decrypted_str


def main(action: str, msg: str, key: str) -> None:
    f"""Main driver of the program based on
    the passed in arguments. Will encrypt or decrypt
    based on the action, message, and key provided.



    Args:
        action (str): Options are {ACTION_ENCRYPT} and {ACTION_DECRYPT}
        msg (str): the message to encrypt or decrypt
        key (str): the key to use for encryption or decryption, if the empty
        string is passed in, a random key will be generated using
        RANDOM_KEY.
    """
    testing_key = 'BEKYPfzGR8JD3jv0d5Hk9wecInOsLrAubX7WQalyUqptCM41NhmiSTZFVg62xo'

    print(RANDOM_KEY)
    print(ALL_LETTERS_DIGITS)
    message = encrypt(RANDOM_KEY, 'Hello world 123')
    print(message)
    print(decrypt(RANDOM_KEY, message))
    print(encrypt('BEKYPfzGR8JD3jv0d5Hk9wecInOsLrAubX7WQalyUqptCM41NhmiSTZFVg62xok', 'this is an ex@mple w(th sp3ci@l ch#arac%->_'))

# If you wish to run the program from the command line
# You could do the following
# python3 subcipher.py "Aloha, World"
# that will encrypt this is my message and return both message and key
# you can decrypt by adding -d or --decrypt as the first argument, and then a key after the message
# python3 subcipher.py -d "9HUqv, VUEHQ" "0XkDwIrGzYv17QfNiqgbZHJ5UhKEljCTRnxA9uaySWopM6emc2dP4sL83BVtFO"
# reminder, windows replaces python3 with python

# The following allows us to run various features from the command line
# do not modify!
if __name__ == "__main__":
    # sets default values for args
    _action = ACTION_ENCRYPT
    _msg = ''
    _key = ''
    if len(sys.argv) > 1:
        if sys.argv[1] == '-d' or sys.argv[1] == '--decrypt':
            _action = ACTION_DECRYPT
            remainder = sys.argv[2:]
        else:
            remainder = sys.argv[1:]
        if len(remainder) > 0:
            _msg = remainder[0]
            if len(remainder) > 1:
                _key = remainder[1]

    # calls your main function
    main(_action, _msg, _key)
