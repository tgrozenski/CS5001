# Report 


1. When you fail to add a base case in recursion, you will return a error value (crashing your program). What is the error value? If you don't know, try running the following code...
```python
def factorial(n):
    return n * factorial(n-1)
```
2. Describe a base case in your own words. What is the base case needed for the code above?
A base case is the smallest and simplest case, it is when you want your recursion to stop and without it your code would go un infinitely. Because of this it is similar to a loop variable, like how we might use index to stop iterating once we reach an index of (n - 1). For this factorial function i would write something like:
```python
def factorial(n):
    if(n == 1):
        return n
    return n * factorial(n-1)
```
This is necessary because without this instead of stopping at 0 without this control flow statement we would multiply n by 0 effectively resetting all our progress. This conditional allows us to make sure we are not multiplying by zero, if we continued after 1 we would accomplish nothing by multiplying 1 to our number.   

3. Thinking about for-in loops, they all work on sequential data, so based on that, what is each "item" for each of these sequential data types. Separate each item by a comma after the => symbol. 
    * Example: range(1, 3) => 1, 2
    * ('aloha', 'world') => 'aloha', 'world'
    * ['aloha', 'world'] => 'aloha', 'world'
    * 'aloha world' => 'a', 'l', 'o', 'h', 'a', ' ', 'w', 'o', 'r', 'l', 'd'

4. For this for-in loop, write an equivalent while loop. 
```python
for i in range(1, 10, 2):
    print(i)
```
```python
i = 1
while(i < 10):
    print(i)
    i+=2
```

## Deeper Thinking

The fibonacci sequence is a very famous sequence found in nature. It is defined as the sum of the previous two numbers in the sequence. The first two numbers are 0 and 1. So the sequence goes 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, etc. If you do a quick search online, you will find that it can be written both recursively and iteratively.

For this deeper thinking, you will work on an experiment. Write a recursive fibonacci function and an iterative fibonacci function. Then, time how long it takes to run each function for the first 30 fibonacci numbers. You can use the following code to time your functions. 


```python

import time

def fibonacci_iterative(n):
    last = 0
    current = 1
    for i in range(n):
        temp = current
        current = last + current
        last = temp
        print(current)

def fibonacci_recursive(n, current = 1, last = 0):
    if(n == 1):
        return
    n -= 1
    temp = current
    current = current + last
    last = temp
    print(current)
    return fibonacci_recursive(n, current, last)


def time_function(func, *args):
  # Get the start time
  start = time.time()
  # Call the function with the given arguments
  result = func(*args)
  # Get the end time
  end = time.time()
  # Calculate the elapsed time
  elapsed = end - start
  # Return the result and the elapsed time
  return result, elapsed

def main():

    print("Fibonacci(10) =", time_function(fibonacci_iterative, 10))
    print("Fibonacci(20) =", time_function(fibonacci_iterative, 20))
    print("Fibonacci(30) =", time_function(fibonacci_iterative, 30))

    print("Fibonacci(10) =", time_function(fibonacci_recursive, 10))
    print("Fibonacci(20) =", time_function(fibonacci_recursive, 20))
   print("Fibonacci(30) =", time_function(fibonacci_recursive, 30))

if __name__ == "__main__":
    main()

```

Report on your results here:

iterative approach:
Fibonacci(10) = (55, 1.9073486328125e-06)
Fibonacci(20) = (6765, 2.1457672119140625e-06)
Fibonacci(30) = (832040, 1.1920928955078125e-06)

recursive approach:
Fibonacci(10) = (55, 3.337860107421875e-06)
Fibonacci(20) = (6765, 7.62939453125e-06)
Fibonacci(30) = (832040, 8.106231689453125e-06)

Which one takes longer? Why do you think that is? 

The recursive functions took longer, and one of the reasons could habe been how I programmed the recursive function. Maybe if it had been more optimized it would have performed better. I think that recursive functions give more flexibility to the programmer to improve performance. I think that the iterative approach is meant to be used for most problems, so maybe language designers give more attention and work to it. I also found it interesting that the iterative approach stayed mostly consistant when it came to time, somehow taking less time to calculate 30 than 20. This looks like a hint to me that there are iterative optimizations that do not occur in a recursive function. The recursive approach is significantly slower, in python at least, so it makes sense to choose a loop if you're doing something where performance could be a real concern. 