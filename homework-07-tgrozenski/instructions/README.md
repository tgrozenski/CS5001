# Homework 07 - Recursion and For Loops

For this homework you will be focusing on recursion and for loops. Additionally, you will explore how projects are often made up of many files, each file (known as a module in python) containing functions that are related to each other in some way. 

## Provided Code and Files
For this assignment, there are four files provided to you.
* [doc_stats.py](../src/doc_stats.py) - this is the main "driver" of the program. In fact, it's only purpose is to run this particular program. All code is provided, no need to edit. 
* [doc_view.py](../src/doc_view.py) - this file contains all the interaction with the client (print and input). The "view" is often used in a lot of design paradigms, as the layer that interacts with the client. By containing your interaction to the view layer, it is easier to swap out the different modalities in which one interacts (console, websites, mobile apps, VR, etc) without having to modify the entire program. All code is provided, no need to edit.
* [word_lib.py](../src/word_lib.py) - This file contains three functions that gives you information about a word. The function signatures (def, and docstring) are provided, but you will need to implement the function bodies. While they can be implemented with loops, we are asking you to implement them recursively to practice recursion.
* [doc_stats_builder.py](../src/doc_stats_builder.py) - This file contains the function that builds various statistics about a "document" (a documents is a list of text strings). The function signatures (def, and docstring) are provided, but you will need to implement the function bodies. In this case, for-in loops are the best way to implement these functions, and we are encouraging you to use them to practice for-in loops. 

While it is optional, you may want to consider using Git to copy the code to your computer. See the [Resources](#using-git-to-copy-the-code) section for more information. Throughout the rest of the semester are going to build up to you using github, as that is the standard for later courses and the industry standard. Right now, it is optional! 

> [!IMPORTANT]  
> Make sure to read through all the files. Looking at the imports, get a sense of how they all interact together. 
> Ask questions on teams if you are unsure how the files interact together!

# Part 1: word_lib.py

:fire: **Task**: Implement the three functions in [word_lib.py](../src/word_lib.py) **recursively**.

The three functions listed in word_lib.py are about looking at a string (technically does not have to be a single word..). While each one can be implemented using a loops, we are asking you to implement them recursively. This is a case of practice makes perfect, and recursion is a topic that takes a lot of practice to get used to. Make sure to take a look at your Team Activity for the module and the provided code. We intentionally built in similar activities, so you can practice the same concepts in a different context.

> Docstring Examples  
> Pay particular attention to the docstring examples. Arguably, these are NOT complete, so you may
> want to add some other examples using the same format to help you understand the edge cases. (see [Testing](#testing))

# Part 2: doc_stats_builder.py

:fire: **Task**: Implement the three functions in [doc_stats_builder.py](../src/doc_stats_builder.py) using for-in loops.

Each function in doc_stats_builder.py is about building a statistic about a document. If you read the doc_view.py file, you will notice a document is being built from a client typing multiple lines in a console. It then returns a tuple of strings, where each string is a line of the document. That means for each function, you can assume a document will look like this:

```python
doc = ("This is the first line",
       "This is the second line",
       "This is the third line",
       "This is the fourth line",
       "This is the fifth line")

line_count = len(doc) # 5
print(f"Line count: {line_count}")
counter = 0
for line in doc:
    print(counter, line) # prints every line of the document to the screen, with a counter in front of it
    counter += 1
```
The output would be

```text
Line count: 5
0 This is the first line
1 This is the second line
2 This is the third line
3 This is the fourth line
4 This is the fifth line
```

Remember, you can grab individual words from a string using the same syntax as a list. For example:

```python
line = "Aloha! World"

for word in line.split(): #splits via spaces/whitespace, returns a list of words
    print(word)
```
prints: 

```text
Aloha!
World
```

> [!TIP]
> for some functions you are looking at lines, others you are looking at words within each line, so a nested loop may be needed.

> [!TIP]
> Make use of your three functions you wrote in word_lib.py!

## Testing
In general, you always want to test functions individually and then everything working together as a group (called interaction testing). You will notice, that in [doc_stats_builder.py](../src/doc_stats_builder.py) and [word_lib.py](../src/word_lib.py) there are docstring examples. These are examples of how the function should work. You can use these as a starting point for your testing. Also, if you have doctest installed (which it should be by default), you can run the doctests in the docstrings just by executing the file. See the resources for doctest. However, the examples are not complete (they don't test edge cases). You should add additional examples to the docstrings to help you test your code.

> [!CAUTION]
> Don't forget to add edge cases to your docstring examples.

For testing, you should make sure your docstrings are complete, and run doctests. We are intentionally not providing an exact copy for the autograder, as eventually you will be in classes without autograders. You will need to think about how you can debug, or more importantly carefully think about the test cases you write to cover every case. 

### Integration Testing - Don't forget
Integration testing is testing how the functions work together. In this case, you can use the doc_stats.py file to test how the functions work together. This actually executes the program, which you can run with various examples,and then save the output of the runs to make sure they are working! 




## Report.md and README.md

:fire: **Task**: Answer the questions in the [Report.md](../Report.md) and [README.md](../README.md) files.

As always you are free to ask about the questions in MS Teams, including clarifications on the code.

## Coding Practice
Looking at the coding [practice problems](https://github.com/CS5001-khoury/Resources/blob/main/PracticeProblems.md) in the class resources, you should ideally do a few
others on your own to get more practice coding.  However, you need to submit at least ONE (1)
completed practice as its own python file (which means even if the coding practice had an online
form to fill out like codingbat, you need to copy your solution to a python file).

## 📝 Grading Rubric


1. Learning (AG)
   * word_lib - palindrome works on easy conditions
   * word_lib - count vowels works on easy conditions
   * word_lib - clean_word works on easy cases
   * word_lib - palindrome works on edge cases
   * word_lib - count vowels works on edge cases
   * word_lib - clean_word works on edge cases
2. Approaching  (AG)
   * doc_stats_builder - line_count works
   * doc_stats_builder - word_count works
   * doc_stats_builder - vowel_count works
   * doc_stats_builder - word palindromes works
   * doc_stats_builder - sentence palindromes works
   * Passes style checker
3. Meets  (MG)
   * Uses Recursion for word_lib, and for-in loops for doc_stats_builder
   * Evidence of testing and running the program
     * Including adding additional examples in doctests than those provided
   * Proper comments and docstrings throughout code 
4. Exceeds  (MG)
   * Report.md questions are all correct
   * Deeper thinking answered with some thought into the answer including data from experiment.
  
     

AG - Auto-graded  
MG - Manually graded



### Submission Reminder 🚨
For manually graded elements, we only guarantee time to submit for a regrade IF you submit by the DUE DATE. Submitting late may mean it isn't possible for the MG to be graded before the AVAILABLE BY DATE, removing any windows for your to resubmit in time. While it will be graded, it is always best to submit by the due date, so you have full opportunity to improve your grade.

## 📚 Resources
* [Python Recursion](https://realpython.com/python-thinking-recursively/)
* [Python For Loops](https://realpython.com/python-for-loop/)
* [Python Doctest](https://docs.python.org/3/library/doctest.html)
* [Python Doctest Tutorial](https://pymotw.com/3/doctest/)
* [Python Doctest Tutorial 2](https://realpython.com/python-doctest/)
* [Getting Started with Git](https://docs.github.com/en/get-started/getting-started-with-git) 
 