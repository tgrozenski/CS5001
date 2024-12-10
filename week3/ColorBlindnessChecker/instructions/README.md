# Homework 3 - Functions

**Divide-Conquer-Glue** whenever we talk about programming, those three terms are at the heart of what we do. Take a problem,
break it into smaller, more abstract parts, conquer those parts, and glue them back together to solve the original problem. That is the heart of programming, and the mindset you need with functions! 

As you work on this assignment, remember the order:

* define
* document
* implement
* test

For every function, you define it, you document it, you implement it, and then you test it - **Before** moving onto the next function!


## Color Blindness Tester
Roughly 8% of Northern European Descent are colorblind. However, application developers often fail to develop applications that can been seen by individuals with colorblindness, or even worse, they use colors to convey information that is not available in any other way. A recent example had a bus route applications that put 
blue on green to indicate a bus was on time. This was not accessible to individuals with colorblindness.

In this assignment, you will write a program that will test if a color is visible to individuals with colorblindness. 

### Understanding Color Blindness

There are many different types of color blindness. The most common is red-green color blindness. This is where the individual has trouble distinguishing between red and green. For this assignment, we will be filtering
colors based on three types of color blindness: Protanopia, Deuteranopia, and Tritanopia.

* Protanopia - Red and Green is reduced in intensity.
* Deuteranopia - Green is reduced in intensity.
* Tritanopia - Blue is reduced in intensity.

While this assignment over simplifies the testing of these colors (spoiler: this could be a fun final project to improve upon), it will give you a sense of how to use functions to break down a problem into smaller parts.

### Understanding RGB Values

RGB stands for Red, Green, Blue. It is a way of representing colors in a computer. Each color is represented by a number between 0 and 255. For example, the color white is represented by (255, 255, 255) and the color black is represented by (0, 0, 0). For this assignment we will be using RGB values. While true color is often a much wider range, and can include alpha (transparency) values, we will be using the simplified version.

While the code is provided, you will also print out the HTML values for the colors. HTML colors are represented by a # followed by 6 hexadecimal digits. For example, white is #FFFFFF and black is #000000. A hexadecimal digit is a number between 0 and 9, or a letter between A and F. The letters A through F represent the numbers 10 through 15. For example, the number 10 in hexadecimal is A, and the number 15 in hexadecimal is F. As you are covering binary in CS 5002 which is a "base 2" notation of numbers, hexadecimal is a "base 16" notation of numbers compared to our standard "base 10" notation. The reason HTML uses hexadecimal is because it is a more compact way of representing colors, representing 3 bytes (0-255) of information in 6 digits.


### Implementation and Testing
You will find [ColorTesterDesign](ColorTesterDesign.md) in this folder. It is a design document that will help you break down the problem into smaller parts. You will want to read through this document, and then slowly practice

* defining
* documenting
* implementing
* testing

for every function you are required to implement! Make sure to take it into small parts, and run and test your code regularly.  The over arching concept behind the project is your manager has given you this design document to work on and your job as a junior developer is to implement their design. In practice you are given more freedom as a developer, but this is a good way to practice breaking down a problem into smaller parts. 

As you work on the project, take a look at some of the resources below. Sometimes seeing the actual colors it is generating is helpful to understanding the problem.

👉🏽 **Task**  - Implement [color_tester.py](../src/color_tester.py) using the information provided by [ColorTesterDesign](ColorTesterDesign.md). Make sure to test by uncommenting the tests in [test_color_tester.py](../tests/test_color_tester.py)

> [!NOTE]
> This assignment you are focusing on the workings of a larger program. Once you have completed 
> color_tester.py, you can run color_blindness_driver.py, and see a full working program! 

### different_colors walkthrough
This assignment is focusing on a repeating methodology in order to enforce a process to approach
writing functions. To help you focus on methodology, let's walk through different_colors together.

#### STEP 1 Define:

* Ask yourself what are you meant to do (see [ColorTesterDesign](ColorTesterDesign.md)).
  * In the document we give the function definition, and a **start** of the documentation.

```python
def different_colors(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> bool:
    pass
```

While coding wise, that is all we have to do at the define stage, we are really doing is asking three questions.

* What do I need to do?
* What do I have to work with/need it to work?
* What am I returning. 
  
#### STEP 2 Document:

> [!CAUTION]
> You will write more documentation than you will code. In fact, most functions are only one or two lines often repeating similar but different tasks. However, your documentation will be extensive. This feels tedious now, but will save you in the future. Use this as a time to get into the habit. 

In this step, you will write your docstring. The docstring is an opportunity to think through what you are doing, including expected input and output for the function. 

We can once again start with the design document

```python
def different_colors(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> bool:
    """
    Compares two color RBG values to see how different they are.  Does
    not convert, only compares.

    Args:
        red_one (int): a color range between 0 and 255 representing the red for the first color
        green_one (int): a color range between 0 and 255 representing the green for the first color
        blue_one (int):a color range between 0 and 255 representing the blue for the first color
        red_two (int): a color range between 0 and 255 representing the red for the second color
        green_two (int): a color range between 0 and 255 representing the green for the second color
        blue_two (int): a color range between 0 and 255 representing the blue for the second color

    Returns:
        bool: True if the difference defined by delta is greater than MIN_DIFFERENCE
    """
    pass
```

> [!NOTE]
> MIN_DIFFERENCE is a variable at the top of the file. You can use it directly in your function.

The problem with the documentation above is that it isn't complete. One **MAJOR** missing requirement
is the examples section. The examples section helps us think through input/output of the 
function *before* we write it.

```python
def different_colors(red_one: int, green_one: int, blue_one: int, red_two: int, green_two: int, blue_two: int) -> bool:
    """
    Compares two color RBG values to see how different they are.  Does
    not convert, only compares.


    Examples:
        >>> different_colors(255, 255, 255, 255, 255, 255)
        False
        >>> different_colors(255, 255, 255, 0, 0, 0)
        True
        >>> different_colors(255, 255, 255, 127, 127, 127)
        True
        >>> different_colors(0, 0, 0, 0, 0, 0)
        False

    Args:
        red_one (int): a color range between 0 and 255 representing the red for the first color
        green_one (int): a color range between 0 and 255 representing the green for the first color
        blue_one (int):a color range between 0 and 255 representing the blue for the first color
        red_two (int): a color range between 0 and 255 representing the red for the second color
        green_two (int): a color range between 0 and 255 representing the green for the second color
        blue_two (int): a color range between 0 and 255 representing the blue for the second color

    Returns:
        bool: True if the difference defined by delta is greater than MIN_DIFFERENCE
    """
    pass
```

Can you think of other examples? You may want to run `delta` with a few color combinations and figure out what the result would be if different_colors had the same values. 

> [!WARNING]
> Don't skip the examples section. It is required for the meets grade in your rubric!

#### STEP 3 Implement:
This step we leave for you to work on, but we recommend keeping it **SIMPLE**. The solution code was only one line for this function. Actually, most of them they are one line, though really doing it in a few lines may be easier to read! You should not feel constrained, but try to keep it simple. The focus on this assignment is the process, not the code. 


#### STEP 4 Test:
You actually defined your tests in STEP 2 with the examples, but now is your time to run tests. To make this step easier, we have provided [test_color_tester.py](../tests/test_color_tester.py). You should run it now!

> [!IMPORTANT]
> Always test after **EVERY** function. It is very common to try to write multiple functions and then test, and while that feels faster it ends up being much, much slower in the long run. Test as you develop, and you will thank yourself in the future. 
> 

One last reminder, this is about the process! It may seem really repetitive, but our goal is for you to really build your understanding of how to write a function from scratch. 

## Report.md and README.md

👉🏽 **Task**: Answer the questions in the [Report.md](../Report.md) and [README.md](../README.md) files. 


As always you are free to ask about the questions in MS Teams, including clarifications on the code. 

### Inclusive Design Resources
The following resources will be helpful in answering the Deeper Thinking in your report. Make sure to
cite them if you use them!

* [Microsoft Inclusive Design](https://inclusive.microsoft.design/)
* [What is Inclusive Design](http://www.inclusivedesigntoolkit.com/whatis/whatis.html)
* [W3Schools Design Tips](https://www.w3.org/WAI/tips/designing/)
* [10 Essential Guidelines for Colorblind Friendly Design](https://www.colorblindguide.com/post/colorblind-friendly-design-3)
* [Color Blindness Simulator](https://www.color-blindness.com/coblis-color-blindness-simulator/)


## Coding Practice
Looking at the coding [practice problems](https://github.com/CS5001-khoury/Resources/blob/main/PracticeProblems.md) in the class resources, you should ideally do a few
others on your own to get more practice coding.  However, you need to submit at least ONE (1) 
completed practice as its own python file (which means even if the coding practice had an online
form to fill out like codingbat, you need to copy your solution to a python file). 




## 📝 Grading Rubric

You need to submit the following files:

* [color_tester.py](../src/color_tester.py)
* Your Coding Practice file
* [Report.md](../Report.md)
* [README.md](../README.md) (the one with your name in it)


### Rubric


1. Learning (AG)
   * check_x functions are completed properly
2. Approaching  (AG)
   * rgb_to_hex_x functions completed properly
   * get_fails completed properly
   * passes PEP8 style check
3. Meets  (MG)
   * every function in color_tester.py has an examples section in docstring
   * Properly formatted docstrings exist for each function
   * Coding practice file provided
4. Exceeds  (MG)
   * Report questions answered properly
   * Report deeper thinking answered with some thought


AG - Auto-graded  
MG - Manually graded



### Submission Reminder 🚨
For manually graded elements, we only guarantee time to submit for a regrade IF you submit by the DUE DATE. Submitting late may mean it isn't possible for the MG to be graded before the AVAILABLE BY DATE, removing any windows for your to resubmit in time. While it will be graded, it is always best to submit by the due date, so you have full opportunity to improve your grade.

## 📚 Additional Resources

For our functions, we have been using type hints. If you are interested in learning more, feel free to follow the additional resources, but these are mostly beyond the scope of the class. Type hints were introduced in Python 3.0, but they weren't really given a purpose until Python 3.5 (PEP 484). It has become common in industry to include them even though python is a dynamically typed language. Dynamically typed means specifying the types are not required as the language will determine the memory needed at runtime. Some languages, like Java which you will learn in CS5004, are strongly typed which means the types are required and strictly enforced at time of programming (compile time). 

Adding the type hints in python is two fold. First, it makes it easier to see what is expected both as the arguments of a function and as the return value of the function. This helps you debug and helps other programmers. Second, there are tools that someone can run against your code to make sure the types are being followed, such as mypy below! This matters for large scale application development.

While not required for this course, you can learn about types hints
* [mypy](https://mypy.readthedocs.io/en/latest/)
* [typing library](https://docs.python.org/3/library/typing.html)

Above all, keep it simple! There are far more features in python than we will need. 

