import time

def fibonacci_iterative(n):
    last = 0
    current = 1
    for i in range(n - 1):
        temp = current
        current = last + current
        last = temp
    return current

def fibonacci_recursive(n, current = 1, last = 0):
    if(n == 1):
        return current
    n -= 1
    temp = current
    current = current + last
    last = temp
    # print(current)
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