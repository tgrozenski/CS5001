# Homework 05 Report

1. What does the `in` operator do? Provide examples of the `in` using strings and lists (or tuples). 

In is a very powerful operator because it can search a list for something and return true if it exists in it. This is incredibly useful for searching for substrings, or determining if a space is present in a string before splitting it. 

Example with integers: 
```python
int_list: list[int] = [0,1,2,3,4,5,6,7,8,9]
if(1 in int_list):
    print("this list contains the value 1")
```

Example with Strings: 
```python
greetings: list[str] = ["hello", "howdy", "hi", "what's up"]
if("what's up" in greetings):
    print("this list has what's up")
```

Example with tuple: 
```python
guess_rating: tuple[str, int] = [("Jurassic Park", 5), ("Lego Movie", 4), ("Emoji Movie", 1)]
guess = ("Lego Movie", 4)
if(guess in guess_rating):
    print("Guess correct")
else:
    print("Guess wrong")
```
   
2. Taking a moment to research, why would one want to use .casefold() instead of .lower() in python when comparing strings? Please include the reference on where you find the information.
To be honest I had used .lower() and all the tests passed so I thought I was good. After reading an article by [GeeksforGeeks](https://www.geeksforgeeks.org/difference-between-casefold-and-lower-in-python/) I learned that .casefold() is able to convert non ascii characters where lower is only able to convert ascii. This makes the casefold method more suitable for most situations where performance isn't a major concern. 

1. For each of the three sequential types you have learned (list, string, tuple) - label as mutable or immutable (refer to the team activity).
   * string - immutable
   * list - mutable
   * tuple - immutable

2. Explain mutability and immutability in your own words.

Mutability means that an object can be directly changed, or mutated to be reassigned to some new value. This means that if something is mutable it can be directly changed memory and reassigned to some new value. If something is immutable it means that python will change it through making copies of it. For example if i try to do .casefold() on a string it will not be changed because it is immutable, but if we store this copy in a new variable we can change the value. A list is an example of a sequence that is mutable meaning we can index into the last element and change it arbitrarily. 

3. Given the following code:

    ```python
    def mystery_function(x):
        x = 100

    x = 1
    print(x)
    mystery_function(x)
    print(x)
    ```

* What is the output of the code above?

The output is 1 both times. 
  
* Explain why the output is what it is.

The output is not changed because it is a copy of that variable that gets passed into the function as an argument not the actual x variable.  

6. Given the following code:

    ```python
    def mystery_function(x):
        x[0] = 100

    x = [1, 2, 3]
    print(x)
    mystery_function(x)
    print(x)
    ```
* What is the output of the code above? 

The output is 1,2,3 then 100,2,3 

* Explain why the output is what it is.

The output is like this because lists are mutable and thus instead of a copy being passed into the function a reference to the list is passed in which is allowed to be mutated in python. 

7. Would happen if `x` was a tuple? What is generated when you try to run the code above with a tuple?

    ```
    TypeError: 'tuple' object does not support item assignment
    ```
    This is generated because tuples are immutable and only support accessing items with the square bracket syntax not mutating them. 


8. Given the following code:

    ```python
    def mystery_function(x):
        x[1][0] = 100

    x = (3, [1, 2, 3], [4, 5, 6])
    print(x)
    mystery_function(x)
    print(x)
    ```

* What is the output of the code above?
    (3, [1, 2, 3], [4, 5, 6])
    (3, [100, 2, 3], [4, 5, 6])

## Deeper Thinking

We talked a lot about immutable and mutable. Why would this matter? Take a moment to describe in your own words why computers would care. Pay particular attention to how computers store data in memory, and how making something immutable may help with that storage.

Immutable and mutable are very important concepts because programmers need to be very deliberate when it comes to data. If certain values are changing in memory unintentionally this will lead to buggy and unreliable code. Programmers often default to keeping things as immutable if they know that it isn't something that is meant to change and being very deliberate about their usage of mutable variables. From a performance perspective keeping values immutable makes sense since you can just pass a pointer to an address in memory instead of a copy of that value. To protect from memory bugs python then decides that objects that are passed by reference are immutable. Creating a new copy of a value can be very waseful when it comes to memory, but it can be necessary sometimes. Memory bugs are some of the most dangerous bugs from a cybersecurity standpoint, so it would make sense that a language like python might choose to keep strings as immutable and but leave lists mutable. Allowing mutable objects to be changed in an immutable tupple is very strange behavior in my opinion, and bit inconsistant. 
