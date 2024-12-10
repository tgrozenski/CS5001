import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import jailbreak # type: ignore
import lock_tools # type: ignore

PATTERNS =  [
    "",
    "x",
    "x x\n x \nx x",
    "x   x\n x x \n  x  \n x x \nx   x",
    "x     x\n x   x \n  x x  \n   x   \n  x x  \n x   x \nx     x",
    "x       x\n x     x \n  x   x  \n   x x   \n    x    \n   x x   \n  x   x  \n x     x \nx       x",
    "x         x\n x       x \n  x     x  \n   x   x   \n    x x    \n     x     \n    x x    \n   x   x   \n  x     x  \n x       x \nx         x",
    "x           x\n x         x \n  x       x  \n   x     x   \n    x   x    \n     x x     \n      x      \n     x x     \n    x   x    \n   x     x   \n  x       x  \n x         x \nx           x",
]
class TestJailBreak(unittest.TestCase):

    def setUp(self) -> None:
        """Forces the door to have a specific set of locks for each test."""
        # note part of testing often involves removing the randomness, so you can test
        # specific cases.
        lock_tools.CURRENT_DOOR = []
        lock_tools.CURRENT_DOOR.append(lock_tools.Lock(lock_tools.COMBO, 0))
        lock_tools.CURRENT_DOOR.append(lock_tools.Lock(lock_tools.COMBO, 10))
        lock_tools.CURRENT_DOOR.append(lock_tools.Lock(lock_tools.COMBO, 100))
        lock_tools.CURRENT_DOOR.append(lock_tools.Lock(lock_tools.PATTERN, PATTERNS[2]))
        lock_tools.CURRENT_DOOR.append(lock_tools.Lock(lock_tools.PATTERN, PATTERNS[0]))
        lock_tools.CURRENT_DOOR.append(lock_tools.Lock(lock_tools.PATTERN, PATTERNS[7]))


    def test_unlock_combo_lock(self) -> None:
        """Tests the unlock_combo_lock function with a variety of inputs."""
        self.assertEqual(jailbreak.unlock_combo_lock(0), 0)
        self.assertEqual(jailbreak.unlock_combo_lock(1), 10)
        self.assertEqual(jailbreak.unlock_combo_lock(2), 100)

    def test_unlock_pattern_lock(self) -> None:
        """Tests the unlock_pattern_lock function with a variety of inputs."""
        self.assertEqual(jailbreak.unlock_pattern_lock(3).strip(), PATTERNS[2].strip())
        self.assertEqual(jailbreak.unlock_pattern_lock(4).strip(), PATTERNS[0].strip())
        self.assertEqual(jailbreak.unlock_pattern_lock(5).strip(), PATTERNS[7].strip())
    
    def test_open_door(self) -> None:
        """Tests the open_door function with a variety of inputs."""
        self.assertTrue(jailbreak.open_door(len(lock_tools.CURRENT_DOOR)))



if __name__ == '__main__':
    unittest.main()