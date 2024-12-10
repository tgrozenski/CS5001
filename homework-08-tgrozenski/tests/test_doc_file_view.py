import unittest
import sys
import re
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


import doc_file_view    # type: ignore


clean_spaces = lambda string: re.sub(r"\s+", "", string)


class TestDocFileView(unittest.TestCase):

    def test_stats_to_json(self) -> None:
        """Tests stats_to_json with various doc_stats tuples."""
        self.assertEqual(
            clean_spaces(doc_file_view.stats_to_json((1, 2, 3, 4, 5))),
            clean_spaces(
                '{"lines": 1, "words": 2, "vowels": 3, "palindromes": 4, "sentence_palindromes": 5}'
            ),
        )
        self.assertEqual(
            clean_spaces(doc_file_view.stats_to_json((23, 8, 22, 3, 0))),
            clean_spaces(
                '{"lines": 23, "words": 8, "vowels": 22, "palindromes": 3, "sentence_palindromes": 0}'
            ),
        )
        # Found this which solved how to test for an error being raised
        # https://stackoverflow.com/questions/6103825/how-to-properly-use-unit-testings-assertraises-with-nonetype-objects
        self.assertRaises(ValueError, lambda: doc_file_view.stats_to_json((1, 2, 3)))
        self.assertRaises(TypeError, lambda: doc_file_view.stats_to_json([1, 2, 3, 4, 5]))
        self.assertRaises(ValueError, lambda: doc_file_view.stats_to_json(('cats', 'dogs', 'people', 'houses', 'things')))

 
    def test_write_json_to_file(self) -> None:
        """Tests write_json_file with various doc_stats tuples."""
        doc_stats = (1, 2, 3, 4, 5)
        doc_file_view.write_json_file(doc_stats, "test.json")
        with open("test.json", "r") as file:
            self.assertEqual(
                clean_spaces(file.read()),
                clean_spaces('{"lines": 1, "words": 2, "vowels": 3, "palindromes": 4, "sentence_palindromes": 5}'),
            )
        doc_stats = (0, 0, 0, 0, 0)
        doc_file_view.write_json_file(doc_stats, "test.json")
        with open("test.json", "r") as file:
            self.assertEqual(
                clean_spaces(file.read()),
                clean_spaces('{"lines": 0, "words": 0, "vowels": 0, "palindromes": 0, "sentence_palindromes": 0}'),
            )

        if os.path.exists("test.json"):
            os.remove("test.json")

    def test_read_file(self) -> None:
        """Reading a typical file, with multiple lines. No blank lines or extra whitespace."""
        self.assertEqual(
            doc_file_view.read_file("./data/auto_generated.txt"),
            ("Racecar drivers enjoy their fast cars, zooming past radar traps,", 
            "their racecar's red color reflecting in their", 
            "rearview mirrors. Madam, said the racecar driver,",
            "A Santa at NASA", 
            "made a radar trap a palindrome."),
        )
        self.assertEqual(
            doc_file_view.read_file("./data/dinos.txt"),
            ("this is my file about dinos,",
            "better clean this line up,",
            "Contrary to what many people think, not all dinosaurs lived during the same geological period.",
            "Stegosaurus, for example, lived during the Late Jurassic Period, about 150 million years ago.",
            "Tyrannosaurus rex lived during the Late Cretaceous Period, about 72 million years ago.")
        )
        self.assertEqual(
            doc_file_view.read_file("./data/empty.txt"),()
        )


if __name__ == "__main__":
    unittest.main()
