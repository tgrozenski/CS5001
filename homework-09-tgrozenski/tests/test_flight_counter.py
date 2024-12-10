import unittest
import subprocess
import re
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import flight_counter # type: ignore

# lambda function to make feedback messages easier to read
common_msg = lambda msg, expected, actual: f"{msg}\nExpected: {expected}\nActual: {actual}"

clean_spaces = lambda string: re.sub(r"\s+", "", string)

def lines_to_set(string: str) -> set:
    """Converts a string with newlines to a set of lines"""
    return set([clean_spaces(line) for line in string.splitlines()])

# Double check class name, remember unit tests likes it to start with Test
class TestFlightCounter(unittest.TestCase):
    def test_build_airlines(self) -> None:  # notice method starts with the word test, and starts indented! 
        """Test build airlines with a smaller airlines file"""          # docstring
        airlines = flight_counter.load_airlines("./data/airlines_small.dat") # calls the function to test
        self.assertEqual(   # assertsEquals is saying, compare these two values as equals 
            airlines,       # actual value from the function
            {               # expected / correct answer
                "UA": "United Air Lines Inc.",
                "AA": "American Airlines Inc.",
                "US": "US Airways Inc.",
            },
        )

    def test_build_airlines_2(self) -> None:
        """Test build airlines with a larger airlines file"""
        airlines = flight_counter.load_airlines("data/airlines.dat")
        self.assertEqual(
            airlines,
            {
                "OO": "Skywest Airlines Inc.",
                "UA": "United Air Lines Inc.",
                "AA": "American Airlines Inc.",
                "US": "US Airways Inc.",
                "F9": "Frontier Airlines Inc.",
                "B6": "JetBlue Airways",
                "AS": "Alaska Airlines Inc.",
                "NK": "Spirit Air Lines",
                "WN": "Southwest Airlines Co.",
                "DL": "Delta Air Lines Inc.",
                "EV": "Atlantic Southeast Airlines",
                "HA": "Hawaiian Airlines Inc.",
                "MQ": "American Eagle Airlines Inc.",
                "VX": "Virgin America",
            },
        )

    def test_build_counters(self) -> None:
        """Test build counters with a smaller airlines file"""
        airlines = flight_counter.load_airlines("data/airlines.dat")
        counters = flight_counter.build_counters("tests/flights_4.dat", airlines)
        self.assertEqual(counters, {"MQ": 1, "US": 1, "DL": 1, "WN": 1})
        airlines = flight_counter.load_airlines("data/airlines.dat")
        counters = flight_counter.build_counters("data/flights10.dat", airlines)
        self.assertEqual(counters, {"EV": 2, "MQ": 2, "UA": 2, "DL": 2, "WN": 2,})


    def test_program_run_large(self) -> None:
        """Test program run, large flights file, commas included
        
        This one may not work depending on how you are executing the program.
        You  may need to modify the paths below.
        """
        process = subprocess.run(
            [
                "python3",
                "./src/flight_counter.py",
                "-f" "data/flights.dat",
                "-a",
                "data/airlines.dat",
            ],
            capture_output=True,
        )
        expected = """Alaska Airlines Inc.:           29,614
American Airlines Inc.:         97,549
US Airways Inc.:                73,942
Delta Air Lines Inc.:          147,486
Spirit Air Lines:               19,612
United Air Lines Inc.:          87,606
Hawaiian Airlines Inc.:         14,133
JetBlue Airways:                48,157
Skywest Airlines Inc.:         107,099
Atlantic Southeast Airlines:   111,206
American Eagle Airlines Inc.:   65,512
Frontier Airlines Inc.:         14,669
Southwest Airlines Co.:        221,586
Virgin America:                 10,403"""
        actual = process.stdout.decode().strip()
        self.assertEqual(
            lines_to_set(actual),
            lines_to_set(expected),
            msg=common_msg(
                "\nOutput not correct (commas counted)",
                "\n" + expected,
                "\n" + actual,
            ),
        )


if __name__ == "__main__":
    unittest.main()
