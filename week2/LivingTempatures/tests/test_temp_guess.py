import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from typing import List

import temp_guess # type: ignore

class TestTempGuess(unittest.TestCase):
    def __check_cities(self, actual : str, expected : List[str]) -> None:
        """Helper method to make it easier on the order/give more freedom on the ordering

        Args:
            actual (str): string returned
            expected (List[str]): te expected output list
        """
        if actual:
            actual = sorted(actual.splitlines())
            expected = sorted(expected)   

        self.assertEqual(expected, actual, "Does not contain the expected cities, or has extra (note order does not matter, case does matter)")


    def test_check_lower_first(self) -> None:
        """Tests check_lower(10, 33) returns True"""
        self.assertTrue(temp_guess.check_lower(10,33))

    def test_check_lower_second(self) -> None:
        """Tests check_lower(33, 10) returns False"""
        self.assertFalse(temp_guess.check_lower(33,10))


    def test_check_lower_equal(self) -> None:
        """Tests check_lower(33, 33) returns True"""
        self.assertTrue(temp_guess.check_lower(33, 33))

    

    def test_simple_conditions(self) -> None:
        """Tests get_cities(-8, 33) expects all cities returned"""
        actual= temp_guess.get_cities(-8, 33)
        expected = ['Beijing', 'Boston', 'Honolulu',
                           'San Francisco', 'Vancouver']
        self.__check_cities(actual, expected)


    def test_simple_conditions_two(self) -> None:
        """Tests get_cities(12, 35)"""
        actual = temp_guess.get_cities(12, 35)
        expected = ['Honolulu']
        self.__check_cities(actual, expected)


    def test_conditions_unknown(self) -> None:
        """Tests get_cities(24,32)"""
        actual = temp_guess.get_cities(24, 32)
        expected = ['Unknown']
        self.__check_cities(actual, expected)




if __name__ == '__main__':
    unittest.main()
