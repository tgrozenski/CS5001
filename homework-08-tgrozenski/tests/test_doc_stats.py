import unittest
import sys
import re
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


import doc_stats # type: ignore


clean_spaces = lambda string: re.sub(r"\s+", "", string)


class TestDocStats(unittest.TestCase):

    def test_get_input_file(self) -> None:
        """Tests the -f filename option for get_input_file"""
        filename = "tests/test_files/test_file.txt"
        result = doc_stats.get_input_file(["-f", filename])
        self.assertEqual(result, filename)
        result = doc_stats.get_input_file(["hello", "-o", "-f", filename])
        self.assertEqual(result, filename)
        self.assertRaises(ValueError, lambda: doc_stats.get_input_file(('cats', 'dogs', 'people', 'houses', 'things')))
        self.assertRaises(ValueError, lambda: doc_stats.get_input_file(('cats', 'dogs', '-f', '', 'things')))
        self.assertRaises(ValueError, lambda: doc_stats.get_input_file(('cats', 'dogs', '-f', None, 'things')))
        self.assertRaises(ValueError, lambda: doc_stats.get_input_file(('somearg', '-f')))
        result = doc_stats.get_input_file(["hello", "-o", "-f", filename, 'args after', 'more args'])
        self.assertEqual(result, filename)
        self.assertRaises(ValueError, lambda: doc_stats.get_input_file(('somearg', '-f', '-')))
        self.assertRaises(ValueError, lambda: doc_stats.get_input_file(('somearg', '-f', '--')))

    def test_get_output_file(self) -> None:
        """Tests the -o filename option for get_output_file"""
        filename = "test_file.txt"
        result = doc_stats.get_output_file(["-o", filename])
        self.assertEqual(result, filename)
        result = doc_stats.get_output_file(["hello", "-f", "look.txt", "-o", filename])
        self.assertEqual(result, filename)
        result = doc_stats.get_output_file(["hello", "-f", "look.txt", "-o", ''])
        self.assertEqual(result, 'out.txt')
        result = doc_stats.get_output_file(["hello", "-f", "look.txt", "-o", None])
        self.assertEqual(result, 'out.txt')
        result = doc_stats.get_output_file(["hello", "-f", "look.txt", "-o"])
        self.assertEqual(result, 'out.txt')
        result = doc_stats.get_output_file(["hello", "-f", "look.txt", "-o", 'this is an invalid file name'])
        self.assertEqual(result, 'out.txt')
        result = doc_stats.get_output_file(["hello", "-f", "look.txt", "o", 'no - o present'])
        self.assertEqual(result, '')

    def test_get_input_file_exception(self)-> None:
        """Test to make sure -f nothing -f - properly raises ValueError"""
        with self.assertRaises(ValueError):
            doc_stats.get_input_file(["-f"])
            doc_stats.get_input_file(["-f", "-"])

    def test_output_file_not_provided(self) -> None:
        """Tests that the -o nothing default is out.txt"""
        result = doc_stats.get_output_file(["-o"])
        self.assertEqual(result, "out.txt")
        result = doc_stats.get_output_file(["-o", "-f", "hello.txt"])
        self.assertEqual(result, "out.txt")



if __name__ == "__main__":
    unittest.main()
