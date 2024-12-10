# Report


1. What is the difference between a file and a directory?

A directory is like a folder that can store many types of files. Both are important and useful, there are also many variations of files types and some variations of folder types as well. 

2. What is the difference between a relative and absolute path?

I did not know anything about this so I read [This](https://www.redhat.com/en/blog/linux-path-absolute-relative). A path describes a location. If you have a file three directories deep you could cd several times to access it, but it might be faster to do 

```bash
    cat dir1/dir2/dir3/myfile.txt
```
You can always get the absolute path of a file using the realpath command
```bash 
    realpath myfile.txt
```
An absolute path makes no assumptions about where you are in the computer, and starts from the absolute start of your hard drive. It is basically a complete path. 

When it comes to relative path, relative paths often use to go up a parent directory to access something else. Suppose you wanted to list the files in the directory above you. You could do ls .. to see the parent directory files. You could even go cat ../somefileinparentfir.txt, allowing you to use a relative path to access something without going there. A relative path can include temporarily traveling up directories based on where you are, an absolute path only travels down directories.

3. What is the difference between a text file and a binary file?

A text file is a plaintext file which is readable text for humans. A binary file is in the form of one's an zeros and needs to be decompiled for humans to understand it. Binary is machine readable and optimized for machine use not human use. 

4. When looking at program arguments, which is the first argument (sys.argv[0]) in the list for all python files?
   
The first argument is the src/doc_stats.py if ran from the command line or /Users/tylergrozenski/hw_four_and_up/homework-08-tgrozenski/src/doc_stats.py if ran using the run button in VScode. This is the first command line argument we passed which is the location of the python file we are asking python to execute.  

5. List three python exceptions or errors, and what their purpose. For example, a ValueError represents an error when a value has the right type but inappropriate value. You can find a list here: https://docs.python.org/3/library/exceptions.html. Ideally, pick ones you have seen before! 

The first exception is Attribute Error which is raised when you try to use a method that a type does not have. For example if I tried to do the following it would raise an attribute error because integer objects have no len method like string objects do
```python
    i = 100
    print(i.__len__())
```

The next exception I have seen is indexError which is another exception and occurs when you try to access an element of a sequence that does not exist
```python
    my_list: = [0,1,2]
    print(my_list[3])
```

The next exception I have seen is recursionError which occurs if you reach the recursion limit python has set. Knowing that recursion works by taking some memory on the stack for each recursive call to the function, it is likely that python uses this to prevent a stack overflow by setting aside a limit to how much memory a recursive function can use.
```python
    my_list: = [0,1,2]
    print(my_list[3])
```

## Deeper Thinking

In this assignment, your capability to analyze and represent data greatly increased
because you are now able to handle files. Files hold the "state" of information (data)
in a computer, and because of them, we can save our state and return to a certain state between computer runs. 

However, for file types to make sense, there needs to be specifications. A specification
is an agreed upon format for how to represent data. For example, the .csv file format
is a specification for how to represent data in a comma separated value file. Many groups are formed to create specifications, and they are often open source. One  well known one is the [W3C](https://www.w3.org/), which creates specifications for the web with the [HTML](https://html.spec.whatwg.org/) standard being the most well known.

Task: Write a small paragraph (3-5 sentences) about how you think specifications are created, and why they are important. You can use the W3C and HTML as an example, or any other specification you find interesting. If you look at HTML bonus if you create small webpage in HTML to show off your knowledge! (You can upload the .html repo with your submission)

In reading on W3C's website it is clear that web standards are very important because they can allow developers to make interesting experiences that will be available on whatever device. These decisions are reached through consensus rather than one central power that calls all of the shots. As I think of the importance of standards I am reminded too of the importance of conventions. Even though we don't need to write code that has good style it makes working with others a lot easier if all of our code is formatted the same. I see conventions in a similar way; they might not be necessary for your project in a vacuum, but when working with others they may be absolutely necessary. Something like html allows us to all write website layouts that browsers can understand, and because of standards others can understand and hopefully use the site as well. 