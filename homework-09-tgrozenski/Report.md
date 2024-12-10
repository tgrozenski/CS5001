# Homework 09 Report

1. Which Airlines have the most flights in 2015? How many flights did they have?

Southwest had the most at 221,586 flights
   
2. Which Airlines have the least flights in 2015? How many flights did they have?

Virgin America had the least at 10,403 flights
   
3. Data is an important aspect of our society, and it is important to understand how to work with it. What are some ways you can see data being used in your future career?

Data is important because it is used to make data driven decisions. Every aspect of life can be positively affected by making decisions based on the data, a business for example might want to know which months they struggle to make sales in. In my career I am sure that I will spend a lot of time manipulating data files and visualizing data. Understanding data is extremely important because it can make you very useful to those you work with who can benefit from data. I may end up using data to track contributions to a project, or to display analytics in a way more user friendly way. 

4. You should start thinking about larger applications, list some applications /  projects you would like to work on? Narrow it down to projects that you can accomplish within a couple weeks?

fuzzySearch - takes in a command line argument of word or phrase and a document to search for, fuzzySearch outputs a formatted list of the lines where the phrase appears, the line itself with the phrase highlighted somehow with a percentage match of the phrase. Similar to a simple implementation of the grep command. Maybe also an option to search -r through all the files in a directory for the phrase as well. 

wageCalculator - calculates your hourly wage while factoring in commute, and gas to return your actual hourly wage. prompts user several times for all pieces of data needed. 

use Pygame library to build a simple game 


5. Provide output of you running `doctest` with the `-v` flag enabled (i.e. the output generated on your screen)

    ```
    python3 -m doctest -v src/flight_counter.py
    Trying:
        add_commas(1234567)
    Expecting:
        '1,234,567'
    ok
    Trying:
        add_commas(123)
    Expecting:
        '123'
    ok
    Trying:
        add_commas(1234)
    Expecting:
        '1,234'
    ok
    Trying:
        add_commas(1234567891)
    Expecting:
        '1,234,567,891'
    ok
    Trying:
        build_counters("./data/flights10.dat", {"AA": "American Airlines",
    "DL": "Delta Airlines", "UA": "United Airlines"})
    Expecting:
        {'UA': 2, 'DL': 2}
    ok
    Trying:
        load_airlines("./data/airlines.dat")                    # doctest: +NORMALIZE_WHITESPACE
    Expecting:
        {'UA': 'United Air Lines Inc.',
        'AA': 'American Airlines Inc.',
        'US': 'US Airways Inc.',
        'F9': 'Frontier Airlines Inc.',
        'B6': 'JetBlue Airways',
        'OO': 'Skywest Airlines Inc.',
        'AS': 'Alaska Airlines Inc.',
        'NK': 'Spirit Air Lines',
        'WN': 'Southwest Airlines Co.',
        'DL': 'Delta Air Lines Inc.',
        'EV': 'Atlantic Southeast Airlines',
        'HA': 'Hawaiian Airlines Inc.',
        'MQ': 'American Eagle Airlines Inc.',
        'VX': 'Virgin America'}
    ok
    Trying:
        counters = {"AA": 10, "DL": 5, "UA": 3}
    Expecting nothing
    ok
    Trying:
        airlines = {"AA": "American Airlines", "DL": "Delta Airlines", "UA": "United Airlines"}
    Expecting nothing
    ok
    Trying:
        print_counters(counters, airlines)                   # doctest: +NORMALIZE_WHITESPACE
    Expecting:
        American Airlines: 10
        Delta Airlines:     5
        United Airlines:    3
    ok
    2 items had no tests:
        flight_counter
        flight_counter.main
    4 items passed all tests:
    4 tests in flight_counter.add_commas
    1 tests in flight_counter.build_counters
    1 tests in flight_counter.load_airlines
    3 tests in flight_counter.print_counters
    9 tests in 6 items.
    9 passed and 0 failed.
    Test passed.
    ```

    In my own words this is everything that is happening when we run the doctest tool behind the scenes. We provided the verbose flag, so the tool printed out everything it does behind the scenes which testing the individual funtions and comparing the results of the functions to the expected results provided in the doctest. At the end we get the total tally of tests, in this case all the tests returned positive results indicating that all the functions work correctly provided the doctests are written correctly.  

6. Output of running `python3 flight_counter.py -h`, and what it means in your own words. (Note: windows is python, and file location may vary based on where you are running it. The above assume linux and running from the homework src directory)

    ```
    replace with your output here
    usage: flight_counter.py [-h] [-f FLIGHTS] [-a AIRLINES]

    Flight Counter

    options:
    -h, --help            show this help message and exit
    -f FLIGHTS, --flights FLIGHTS
                            The file containing the flight data.
    -a AIRLINES, --airlines AIRLINES
                            The file containing the airline data.
        
    ```
    This is a formatted help message which is standard to include with command line programs, sometimes it is --help. This makes a lot of sense because we want people to be able to easily figure out how to use our program from the command line. Since we have already written our documentation it makes sense to be user friendly and include a quick abbreviated way to use the program. Little things like this aren't too much work for the programmer but can go a long way for the user. 


## Deeper Thinking

When dealing with large datasets, or data in general, there needs to be a careful consideration of biases, collection, and use of that data. For example, it is very possible for real world data to be biased towards collection biases or sampling biases, and there are very real ethical issues in how that data is being used especially if a bias is not being taken into account. Take a moment to research some issues with data collection and use, and list some examples you can find. You may even find some examples that are related to data you supply on a data basis (i.e. what you give to social media)

I read this blogpost from [GAO](https://www.gao.gov/products/gao-22-106096), the government accountability office which talked about a lot of the privacy concerns when it comes to data collection. Businesses now collect, sell, and track user information. Maybe this would be okay if they always handled this data appropriately, but we know that this cannot be the case at the scale this is occurring. Furthermore, it is clear that this data can easily fall into the wrong hands when businesses are selling it. On an individual level this wouldn't seem to affect individuals, but it already is. According to GAO there are concerns about big data in marketing, health care administration, higher education, and criminal justice. To zoom in on one of these, when it comes to healthcare insurance companies can use data to discriminate against certain populations when charging for health insurance. The company is acting in it's best interest, but the result of this raises a serious ethical issue. As of 2022 when the blog post was written there has been no comprehensive privacy law that would reign in companies collection, use, and sale of user data. I think this is a problem and hope to see more people advocating for more comprehensive legislation that understands the nuances of this issue.