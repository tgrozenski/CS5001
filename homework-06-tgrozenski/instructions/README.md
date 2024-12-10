# Homework 06 - Substitution Cipher

For this assignment, you are going to explore both a [substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher), and how to build an entire program from (mostly) scratch. We are opting for the mid semester
program, as it gives us time to return the program and allow you to make design changes.

## Substitution Cipher


A substitution cipher is actually one of the oldest ciphers with documents dating back to early roman times. The
idea behind it, is that you take every letter in the alphabet and map it to a different letter.


For example,

If the text is

```
ADA
```

and we are using the following alphabet and ciphertext (also called key):

| default alphabet      | `ABCDEFGHIJKLMNOPQRSTUVWXYZ` |
| --------------------- |:----------------------------:|
| **ciphertext or key** | `ZEBRASCDFGHIJKLMNOPQTUVWXY` |

We would see, A is in the [0] spot of the original alphabet and the [0] spot in the ciphertext is 'Z'. This would
turn 'A's to 'Z's. We would find the index of 'D' in the original alphabet which is [3], and that maps to 'R' in the
ciphertext, that would make my encrypted message to be

```
ZRZ
```

If a character does not show up in the original alphabet *or* the ciphertext, it's still included in the translated message but it does not get modified. So if my text is

```
ADA 5!!!
```

It would map to

```
ZRZ 5!!!
```

## Your Task

:fire: Write the subcipher.py program, breaking it up into functions as you see fit following good design practices.

## Provided Code

In [subcipher.py](../src/subcipher.py) we provide a block of code. The most notable aspects are as follows:

```python
ALL_LETTERS_DIGITS = digits + ascii_letters
# use this random key if none is provided, try printing it out to see what it is
RANDOM_KEY = "".join(sample(list(ALL_LETTERS_DIGITS), len(ALL_LETTERS_DIGITS)))
```

* `ALL_LETTERS_DIGITS` provides the default 'alphabet' that includes numbers, lowercase letters and uppercase letters (using the above example, it would be the ABC...XYZ, but in this case it is 0123...abc...ABC...XYZ)
* `RANDOM_KEY` randomly generates a new mapping / ciphertext *if* you need it (see below)

> [!TIP]
> If you want to find a location of a letter in the string, you can use .find(). For example
>
> ```python
> index_of_a = ALL_LETTERS_DIGITS.find('A')
> print(index_of_a)
> ```
>
> Would print `36` because `A` shows up in the 36th location in the `ALL_LETTERS_DIGITS` string.
> You can try printing out `ALL_LETTERS_DIGITS` to see the full string using your interactive
> python window (don't forget to include the imports in your selection).



### Running the program

There is a section of code at the bottom you should not modify.  This code allows us to the program
from the command line passing in various arguments. It is not only how we grade
but a very common approach for a command line program. You can also run the code from the command line. Here are some examples of running the program:

```text
> python3 src/subcipher.py "Aloha, World"
Encrypted=T6mfP, 0mw6b
Key=X8aq4vpsR1PuBbGSyfQZ36HJminw5j7xKEWAT9edklNzLDUhIgFctMo2YV0OCr
```
It would generate something similar to standard out if the following was called

```python
main(action="encrypt", msg="Aloha, World", key='')
```
An example of decrypting
```text
> python3 src/subcipher.py -d "9HUqv, VUEHQ" "0XkDwIrGzYv17QfNiqgbZHJ5UhKEljCTRnxA9uaySWopM6emc2dP4sL83BVtFO"
Decrypted message is: Aloha, World
```
or via calling main directly
```python
main(action="decrypt", msg="9HUqv, VUEHQ", key="0XkDwIrGzYv17QfNiqgbZHJ5UhKEljCTRnxA9uaySWopM6emc2dP4sL83BVtFO")
```

> [!IMPORTANT]
> Make sure that your output matches the formatting above exactly. We will be using an autograder to check your code,
> and typos will cause you to loose points!

> [!WARNING]
> In windows, use `python` in place of `python3` when running the program from the command line.

### Testing

Testing is a bit different with this program, as you can't just run the [test_input_output_subcipher.py](../tests/test_input_output_subcipher.py) directly in VS Code. Instead, you will need to go to the command line and run the program. See the comments in the file directly, but for quick reference you will run the test from the homework directory by

```terminal
python3 src/test_input_output_subcipher.py
```

The reason for the change, is we don't actually know the name of the functions you will create. As such, the test is just rerunning the whole program every time grabbing what is printed to the screen. This type of testing is often done and falls into a category called integration testing.

> [!TIP]
> We have also added a [test_subcipher.py](../tests/test_subcipher.py) which you can add your own
> unit tests / function based tests. If you are feeling like a challenge you should create
> the unit tests on your own and build out the file! However, this is not a requirement.
>
> You can also use [doctest](https://realpython.com/python-doctest/) for unit testing! It all depends a bit on how you design the program. To run doctest, your command would be
> ```
> python3 -m doctest -v src/subcipher.py
> ```


### Additional Specifications

* When encrypting a message, you should print to standard out, replacing the values after the `=` sign.
  ```
  Encrypted=(The Encrypted Message)
  Key=(The key / ciphertext)
  ```
  for example for clarity - notice, it is everything after the `=` sign (we split on the first `=` )
  ```text
  Encrypted=T6mfP, 0mw6b
  Key=X8aq4vpsR1PuBbGSyfQZ36HJminw5j7xKEWAT9edklNzLDUhIgFctMo2YV0OCr
  ```

* When decrypting a message, you only need to print out

  ```
  Decrypted message is: (The Decrypted Message)
  ```

* Encrypting can have a provided key, but if that key is the empty string, it should use `RANDOM_KEY`.
* Decrypting must provide a key, and you can ignore cases if a key isn't provided (just provide an error message and
end the program)
* The only two actions are `encrypt` or `decrypt`, and they will be provided.

* If a character is not in the ciphertext/key or alphabet, you simply ignore it - including it as part of the message
  as is/without modification (example, the comma and space in Aloha, World are in the same spots in the encrypted text)

  * You will notice punctuation is not part of the text as to prevent oddities in on the command line key calls.

* The file must be named subcipher.py.
* You must write this program using good design / multiple functions fully documented.

## Program Design

The code for this assignment is relatively few lines. However, you can have both really good and really bad design. If you end up writing the entire program inside of the `main` for example, you may pass the autograder but the TAs will return the program asking you to redesign the program.  This is the type of situation where the feedback and redo (refactoring) really helps!

A few rules to think about design

* Think about isolating the various features into their own functions. What are the features, here are a few to think about
  * Ability to encrypt a string
  * Ability to decrypt a string
  * Print out the expected message for new encrypted strings
  * Print out the expected message for new decrypted strings
  * Run the main based on the parameters passed into main

> [!NOTE]
> If you can write every function where you can test it, before you finish writing the main function you are probably going down a good path.


However, you should also think about **what functions are essentially the same, but with a modification of the parameters**. As a reminder, this is called abstraction. Can any of the
tasks you are performing be abstracted into a single reusable function that is invokes? Also note, if someone else is using your code you still want to keep nice function names, so figuring out an generalized function, and leaving better named functions to call the generalized version may be ideal (think back to team activity 04).



> [!IMPORTANT]
> You need full docstrings. For any function that returns a value (and doesn't just print), you will also need examples of the input and output - including edge cases!

### Remember the mantra

1. Define
2. Document
3. Implement
4. Test



## Report.md and README.md

:fire: **Task**: Answer the questions in the [Report.md](../Report.md) and [README.md](../README.md) files.

As always you are free to ask about the questions in MS Teams, including clarifications on the code.

## Coding Practice
Looking at the coding [practice problems](https://github.com/CS5001-khoury/Resources/blob/main/PracticeProblems.md) in the class resources, you should ideally do a few
others on your own to get more practice coding.  However, you need to submit at least ONE (1)
completed practice as its own python file (which means even if the coding practice had an online
form to fill out like codingbat, you need to copy your solution to a python file).

## 📝 Grading Rubric

You need to submit the following files:

* [subcipher.py](../src/subcipher.py)
* Your Coding Practice file
* [Report.md](../Report.md)
* [README.md](../README.md) (the one with your name in it)

You are free / encouraged to submit by submitting your github repo in grade scope. This will automatically remove your tests and instructions folder in the submission, but include the other files.

### Rubric


While we provide tests, reminder, you should test your own code before submitting!

1. Learning (AG)
   * Passes basic encrypt and decrypt
2. Approaching  (AG)
   * Passes harder cases on encrypt and decrypt
3. Meets  (MG)
   * Breaks program into functions for decrypt and encrypt
   * Contains full docstring with examples for functions that are self-contained (pure)
   * Coding practice file provided
   * Report questions 1-4 answered correctly
4. Exceeds  (MG)
   * Remaining report questions answered correctly
   * Recognizes repeated code building a more generalized approach to the problem
   * Isolates printing from cipher functions / keeps a division of concerns
   * Deeper thinking answered with some thought into the answer


AG - Auto-graded
MG - Manually graded



### Submission Reminder 🚨
For manually graded elements, we only guarantee time to submit for a regrade IF you submit by the DUE DATE. Submitting late may mean it isn't possible for the MG to be graded before the AVAILABLE BY DATE, removing any windows for your to resubmit in time. While it will be graded, it is always best to submit by the due date, so you have full opportunity to improve your grade.




## Resources - For on Strings

As a reminder, you can run for on strings using the following


```python
string = "Aloha"
for character in string:
   print(character)
```

would print

```
A
l
o
h
a
```

You can also apply various string methods on the individual characters. To learn more
about string methods, here are some resources

* [W3Schools String Methods](https://www.w3schools.com/python/python_ref_string.asp)
* [Python.org Common String Operations](https://docs.python.org/3/library/string.html)
  * [Python.org String methods](https://docs.python.org/3/library/stdtypes.html#string-methods)