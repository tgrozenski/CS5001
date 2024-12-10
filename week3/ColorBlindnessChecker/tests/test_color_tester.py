import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

# import sequence to allow for local testing and testing on auto-grader due to different directory structs
import color_tester # type: ignore


class TestColorTester(unittest.TestCase):
    # uncomment each test/function as you complete the functions

    def test_different_colors(self) -> None:
        """Tests different colors with a variety of inputs (255,255,255,0,0,0), and others."""
        self.assertTrue(color_tester.different_colors(255, 255, 255, 0, 0, 0))
        self.assertFalse(color_tester.different_colors(255, 255, 255, 255, 255, 255))
        self.assertTrue(color_tester.different_colors(255, 255, 255, 127, 127, 127))


    def test_check_protanopia(self) -> None:
        """Tests the check_protanopia function with a variety of inputs."""
        self.assertTrue(color_tester.check_protanopia(255, 255, 255, 0, 0, 0))
        self.assertFalse(color_tester.check_protanopia(255, 255, 255, 0, 0, 255))
        self.assertTrue(color_tester.check_protanopia(255, 255, 255, 127, 127, 127))


    def test_check_deuteranopia(self) -> None:
        """Tests the check_deuteranopia function with a variety of inputs."""
        self.assertTrue(color_tester.check_deuteranopia(255, 255, 255, 0, 255, 0))
        self.assertFalse(color_tester.check_deuteranopia(255, 255, 255, 255, 0, 255))
        self.assertTrue(color_tester.check_deuteranopia(255, 255, 255, 127, 255, 127))


    def test_check_tritanopia(self) -> None:
        """Tests the check_tritanopia function with a variety of inputs."""
        self.assertTrue(color_tester.check_tritanopia(255, 255, 255, 0, 0, 255))
        self.assertFalse(color_tester.check_tritanopia(255, 255, 0, 255, 255, 255))
        self.assertTrue(color_tester.check_tritanopia(255, 255, 255, 127, 127, 255))


    def test_rgb_to_hex_deuteranopia(self) -> None:
        """Testing rgb_to_hex_deuteranopia(255, 255, 255) should be #ff00ff"""
        actual = color_tester.rgb_to_hex_deuteranopia(255, 255, 255)
        expected = "#ff00ff"
        self.assertEqual(actual, expected)

        actual = color_tester.rgb_to_hex_deuteranopia(0, 255, 0)
        expected = "#000000"
        self.assertEqual(actual, expected)

        actual = color_tester.rgb_to_hex_deuteranopia(75, 100, 100)
        expected = "#4b0064"
        self.assertEqual(actual, expected)


    def test_rgb_to_hex_protanopia(self) -> None:
        """Testing rgb_to_hex_protanopia(255, 255, 255) should be #00000ff"""
        actual = color_tester.rgb_to_hex_protanopia(255, 255, 255)
        expected = "#0000ff"
        self.assertEqual(actual, expected)

        actual = color_tester.rgb_to_hex_protanopia(255, 255, 0)
        expected = "#000000"
        self.assertEqual(actual, expected)

        actual = color_tester.rgb_to_hex_protanopia(120, 255, 200)
        expected = "#0000c8"
        self.assertEqual(actual, expected)

    def test_rgb_to_hex_tritanopia(self) -> None:
        """testing rgb_to_hex_tritanopia(255, 255, 255) should be #ffff00"""
        actual = color_tester.rgb_to_hex_tritanopia(255, 255, 255)
        expected = "#ffff00"
        self.assertEqual(actual, expected)

        actual = color_tester.rgb_to_hex_tritanopia(0, 0, 255)
        expected = "#000000"
        self.assertEqual(actual, expected)

        actual = color_tester.rgb_to_hex_tritanopia(120, 255, 200)
        expected = "#78ff00"
        self.assertEqual(actual, expected)


    def test_get_fails(self) -> None:
        """Tests get fails with simple inputs"""
        actual = color_tester.get_fails(255, 255, 255, 255, 255, 255).strip()
        expected = "Protanopia\nDeuteranopia\nTritanopia\n".strip()
        self.assertEqual(actual, expected, "Tested with 255, 255, 255, 255, 255, 255")
        actual = color_tester.get_fails(255, 255, 255, 0, 0, 0).strip()
        expected = ""
        self.assertEqual(actual, expected, "test with 255, 255, 255, 0, 0, 0")


    def test_get_fails_more_complex(self) -> None:
        """Tests get fails with more complex inputs"""
        actual = color_tester.get_fails(255, 255, 255, 0, 0, 255).strip()
        expected = "Protanopia\n".strip()
        self.assertEqual(actual, expected, "Tested with 255, 255, 255, 0, 0, 255")

        actual = color_tester.get_fails(0, 0, 255, 0, 0, 0).strip()
        expected = "Tritanopia".strip()
        self.assertEqual(actual, expected, "test with 0, 0, 255, 0, 0, 255")

        actual = color_tester.get_fails(255, 255, 255, 255, 0, 255).strip()
        expected = "Protanopia\nDeuteranopia\n".strip()
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
