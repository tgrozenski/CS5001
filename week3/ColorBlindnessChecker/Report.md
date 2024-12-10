# Report

Please answer the questions below. Make sure to ask questions if you have them. 


For all these questions, it is recommended you open up IDLE or the python interpreter and try out the code.  You can also use the python visualizer to help you visualize the code.  You can find the visualizer here: [http://www.pythontutor.com/visualize.html#mode=edit](http://www.pythontutor.com/visualize.html#mode=edit)

1. Thinking about functions, a common design is to have functions that do one thing and do it well.  This is called the Single Responsibility Principle.  What are some advantages of this design?
     
   Some advantages are that your code will be very modular in design. If every function does just one thing it is very easy to determine where a bug is coming from. With your code less interconnected it is easier to make changes to the design because ideally a change to one function will not affect another. Furthermore, testing is also easier when you only have to think of one output of a function instead of multple. For example it is a lot more complicated to test a function that gets input, manipulates that input, prints something out, and then returns something else. The test cases for this function would have to be very intricate and debugging will be more difficult.
2. Looking at the Single Responsibility Principle, why would it be bad design to have a function both print and return a value?
   Having a function print and return a value is bad design because the function now has two responsibillities, breaking the single responsability principle. The example provided is simple enough to likely not cause any issues, but this is bad habit to get into as a programmer because it is not managing complexity. It also may make the code less understandable for other programmers because it will be unclear what the function does since printing and returning a value are similar conceptually but different operations.
3. In practice, prints are often isolated to a certain set of functions, and every other function returns values - including strings to print. While we did not follow this rule strictly for this assignment, what are some advantages of this design? 
   
   Littering a program with print statements is not an ideal way to test because it could be difficult to find them and remember why they are printing something out where they are. Overall it is a much messier approach than than returning strings and testing strings; a better testing pattern was using the unit test class in python and the assert function to check the output of functions against their expected output.
4. A **pure** function is defined as

   * the function return values are identical for identical arguments (no variation with local static variables, non-local variables, mutable reference arguments or input streams), and
   * the function has no side effects (no mutation of local static variables, non-local variables, mutable reference arguments or input/output streams).
   * Given that definition, which functions in color_tester.py and color_blindness_driver.py are pure functions?
   * All functions in color_tester.py are pure except for main and different colors, main uses the output stream and differnet colors uses a global variable. 
   * In color_blindness_driver.py all are except for print_html_values, get_html_hex, and main. These three functions use either input or output streams.

5. color_tester.py has a variable at the top MIN_DIFFERENCE. Why would it be helpful to declare a variable like this?
   
   The MIN_DIFFERENCE is a global variable and can be accessed anywhere in the file. It is helpful because this is something that should not ever change but will need to be accessed multiple times. With this global variable we can make it clear what the MIN_DIFFERENCE instead of writing 0.5 throughout the function.
6. What `scope` does MIN_DIFFERENCE have?
   Global scope meaning it is acessable anywhere in the file.
7. Take a look at the following code:
    ```python
    def get_name(which):
        if which == 1:
            which = 13
            return "Who"
        else:
            which = 3
            return "Strange"

    def welcome():
        print("Welcome Doctor?")
        which = 0
        name = get_name(1)
        print(which)
        print(f"Doctor {name}")
    
    welcome() ## execute the above
    ```
    Here is a link if you want to visualize it: [Visualize](https://pythontutor.com/render.html#code=def%20get_name%28which%29%3A%0A%20%20%20%20if%20which%20%3D%3D%201%3A%0A%20%20%20%20%20%20%20%20which%20%3D%2013%0A%20%20%20%20%20%20%20%20return%20%22Who%22%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20which%20%3D%203%0A%20%20%20%20%20%20%20%20return%20%22Strange%22%0A%0Adef%20welcome%28%29%3A%0A%20%20%20%20print%28%22Welcome%20Doctor%3F%22%29%0A%20%20%20%20which%20%3D%200%0A%20%20%20%20name%20%3D%20get_name%281%29%0A%20%20%20%20print%28which%29%0A%20%20%20%20print%28f%22Doctor%20%7Bname%7D%22%29%0A%0Awelcome%28%29%20%23%23%20execute%20the%20above&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false)

    * What is printed on `print(which)`? What about `print(f"Doctor {name}")` (really, use the visualizer)? 

    On `print(which)` 0 is printed because the `which` variable is an integer with the value of 0, it is important to note that this which variable is different from the one present in `get_name()`. That variable is passed into the function as an argument and is a different although it shares the same name. On the line that prints `print(f"Doctor {name}")` name is equal to the return value of `get_name(1)` which is a string "Who". What ends up getting printed is `Doctor Who`.
    * Why is this the case?

    Which remains unchanged because it is out of scope in the get name function. In the get_name function the `which` variable that is mutated is separate from the which variable in the `welcome` function.

## Deeper Thinking

Inclusive design often goes beyond accessible design, and is a major area of research in computer science. Take time to read up on resources, and write a paragraph (minimum) on what you learned. Make sure to include links to any resources you used. In the paragraph, I encourage you to reflect on your own experiences with inclusive design (or lack of inclusive design), and how you can use this knowledge in your own work. Also, why does this matter at all? 

I read an article by Geeks for Geeks called [Inclusive Design](https://www.geeksforgeeks.org/inclusive-design/), and learned a lot about what it means to design inclusively. Inclusive design is essential to make your software more accessible to more people, and this means considering the needs of all your users not just the average user. This is a challenge because there is often pressure to push out software quickly, but it is something that is worth it because you reach more people. I was realizing the fact that if you had a very similar program to someone elses program but yours was designed inclusively and theirs wasn't your sofware would be superior despite most of the core functionality being identical. Furthermore I liked how the article talked about how inclusive design can actually spur innovations that other users may appreciate too. Seeing inclusive design as a spark for creativity and innovation is a better way of looking at it as opposed to simply complying with regulation or trying to increase your audience. As someone who struggles with mild dyslexia and ADHD a wide variety of tools and different ways of doing things benefit me greatly. As programmers we are tasked with embracing the diversity of our users and creating a more inclusive software experience. 