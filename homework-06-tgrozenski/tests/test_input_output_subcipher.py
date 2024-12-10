import unittest
from typing import List, Tuple
import platform

from string import digits, ascii_letters
import subprocess

CHECK_FILES = True

if platform.system() == "Windows":
    PYTHON_CMD = ["python"]
else:
    PYTHON_CMD = ["python3"]


ALL_LETTERS_DIGITS_FOR_TESTS = (digits + ascii_letters)[::-1]  # reversed

# To execute these tests, run **from the terminal**
# the following assumes you are in the homework directory (one above src)
# python src/test_input_output_subcipher.py
# replace python with python3 if on max/linux

# These tests are all "input/output" tests. They only look
# at passing in some input and checking the output. They do not
# check the internal state of the program. They are also not
# "unit tests" in the sense that they do not test individual
# functions. They are more like integration tests that test
# the entire program.

# However, since we don't know the name of your functions for 
# encrypting and decrypting, we can't test them directly. Instead,
# we will run the program with some input and check the output.

# Take a look at test_subcipher.py for sample unit tests
# that you can use to test your functions directly.


def _run_program(arguments: List[str]) -> Tuple:
    """runs the program returning the process, and the standard out as a list"""
    process = subprocess.run(PYTHON_CMD + ["src/subcipher.py"] + arguments, capture_output=True, timeout=60)
    lines: list[str] = process.stdout.decode().splitlines()
    return process, lines


def _clean_lines(lines: List[str]) -> Tuple:
    return tuple([line.split("=")[1].strip() for line in lines if '=' in line])


class TestSubCipher(unittest.TestCase):
    encrypt_basic = ["ADA"]
    encrypt_hard = ["Aloha, World. To the Hawai'i Islands I go."]
    decrypt = ['-d']


    def test_simple_encrypt(self):
        """Tests encrypt with simple input of ADA, assumes random key generation"""
        proc, lines = _run_program(self.encrypt_basic)
        msg, key = _clean_lines(lines)
        self.assertIsNot(msg, '', "Failed to print an encrypted message.")
        self.assertEqual(len(msg), 3, "Message is not the correct length.")
        self.assertIsNot(key, '', "Failed to print an generated key.")

    def test_simple_encrypt_controlled(self):
        """Tests encrypt with simple input of ADA, Uses defined key."""
        proc, lines = _run_program(self.encrypt_basic + [ALL_LETTERS_DIGITS_FOR_TESTS])
        msg, key = _clean_lines(lines)
        self.assertEqual(msg, 'pmp', "Message does not match expected encryption using the provided key")
        self.assertIsNot(key, '', "Failed to print an generated key.")

    def test_simple_decrypt(self):
        """Tests decrypt a message based on results from encrypt."""
        proc, lines = _run_program(self.encrypt_basic)
        msg, key = _clean_lines(lines)
        proc, lines = _run_program(self.decrypt + [msg, key])
        indx = lines[0].find(":")+1
        line = lines[0][indx:].strip()
        if "ADA" in line:
            self.assertTrue("ADA" in line, "Message did not decrypt exactly to encryption type.")
        else:
            self.assertEqual('ADA', line, "Message did not decrypt exactly to encryption type.")

    def test_simple_decrypt_controlled(self):
        """Tests decrypt a message based on provided key and message."""
        proc, lines = _run_program(self.decrypt + ["pmp", ALL_LETTERS_DIGITS_FOR_TESTS])
        indx = lines[0].find(":")+1
        line = lines[0][indx:].strip()
        if "ADA" in line:
            self.assertTrue("ADA" in line, "Message did not decrypt exactly with provided key and message.")
        else:
            self.assertEqual('ADA', line, "Message did not decrypt exactly with provided key and message.")

    def test_hard_encrypt(self):
        """Tests encrypt with complex string, assumes random key generation"""
        proc, lines = _run_program(self.encrypt_hard)
        msg, key = _clean_lines(lines)
        self.assertIsNot(msg, '', "Failed to print an encrypted message.")
        self.assertEqual(len(msg), len(self.encrypt_hard[0]), "Message is not the correct length.")
        self.assertIsNot(key, '', "Failed to print an generated key.")

    def test_hard_encrypt_controlled(self):
        """Tests encrypt with complex string Uses defined key."""
        proc, lines = _run_program(self.encrypt_hard + [ALL_LETTERS_DIGITS_FOR_TESTS])
        msg, key = _clean_lines(lines)
        self.assertEqual(msg, "pEBIP, 3ByEM. 6B wIL iPtPH'H hxEPCMx h JB.",
                         "Message does not match expected encryption using the provided key")

    def test_hard_decrypt(self):
        """Tests decrypt a message based on results from encrypt."""
        proc, lines = _run_program(self.encrypt_hard)
        msg, key = _clean_lines(lines)
        proc, lines = _run_program(self.decrypt + [msg, key])
        indx = lines[0].find(":")+1
        line = lines[0][indx:].strip()
        if self.encrypt_hard[0] in line:
            self.assertTrue(self.encrypt_hard[0] in line, "Message did not decrypt exactly to encryption type.")
        else:
            self.assertEqual(self.encrypt_hard[0], line, "Message did not decrypt exactly to encryption type.")

    def test_hard_decrypt_controlled(self):
        """Tests decrypt a hard message based on provided key and message."""
        proc, lines = _run_program(self.decrypt + ["pEBIP, 3ByEM. 6B wIL iPtPH'H hxEPCMx h JB.",
                                                   ALL_LETTERS_DIGITS_FOR_TESTS])
        indx = lines[0].find(":")+1
        line = lines[0][indx:].strip()
        if self.encrypt_hard[0] in line:
            self.assertTrue(self.encrypt_hard[0] in line, "Message did not decrypt exactly with provided key and message.")
        else:
            self.assertEqual(self.encrypt_hard[0], line,
                         "Message did not decrypt exactly with provided key and message.")


if __name__ == '__main__':
   unittest.main()
