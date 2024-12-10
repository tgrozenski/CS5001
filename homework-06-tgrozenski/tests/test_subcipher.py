import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from string import digits, ascii_letters

ALL_LETTERS_DIGITS_FOR_TESTS = (digits + ascii_letters)[::-1]  # reversed

import subcipher # type: ignore


class TestSubCipher(unittest.TestCase):
   # this just exists to prevent errors with a mostly empty file
   # you can remove this if you add tests to it
   def test_nothing(self):
      return True  

# uncomment the following lines - it assumes
# you have a function called encrypt in subcipher.py

#    def test_simple_encrypt(self):
#        """Tests encrypt with simple input of ADA, assumes random key generation"""
#        expected = "pmp"
#        actual = subcipher.encrypt("encrypt", "ADA", ALL_LETTERS_DIGITS_FOR_TESTS)
#        self.assertEqual(actual, expected, "Failed to encrypt simple message.")

# if you want to test additional functions, follow
# the pattern above ideally one test per function
# notice that def is indented from class that is intentional. You can look at the
# examples in the previous homework for guidance


    
if __name__ == '__main__':
   unittest.main()
