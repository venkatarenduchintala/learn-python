# Chapter 3 - Functions
# Exercise 3.1 Write a function named right_justify that takes a string named s as a 
# parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70
# of the display.

def right_justify(s):
    l = len(s);
    print(' '*(70-l) + s);


right_justify('monty');

# Exercise 3.2 A function object is a value you can assign to a variable or pass as an argument. For
# example, do_twice is a function that takes a function object as an argument and calls it twice:
# def do_twice(f):
# f()
# f()
# Here’s an example that uses do_twice to call a function named print_spam twice.
# def print_spam():
# print('spam')
# do_twice(print_spam)
# 1. Type this example into a script and test it.
# 2. Modify do_twice so that it takes two arguments, a function object and a value, and calls the
# function twice, passing the value as an argument.
# 3. Copy the definition of print_twice from earlier in this chapter to your script.
# 4. Use the modified version of do_twice to call print_twice twice, passing 'spam' as an
# argument.
# 5. Define a new function called do_four that takes a function object and a value and calls the
# function four times, passing the value as a parameter. There should be only two statements in
# the body of this function, not four.

def print_twice(arg):
    print(arg);
    print(arg);

def do_twice(f, value):
    f(value);
    f(value);

def do_four(f, value):
    do_twice(f, value);
    do_twice(f, value);

do_twice(print, 'spam');
print('');

do_four(print, 'spam');

# Exercise 3.3 Note: This exercise should be done using only the statements and other features we have learned so far
# 1. Write a function that draws a grid like the following:
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# |         |         |
# |         |         |
# |         |         |
# |         |         |
# + - - - - + - - - - +
# Hint: to print more than one value on a line, you can print a comma-separated sequence of values:
# print('+', '-')
# By default, print advances to the next line, but you can override that behavior and put a space at the end, like this:
# print('+', end=' ')
# print('-')
# The output of these statements is '+ -' on the same line. The output from the next print statement would begin on the next line.
# 2. Write a function that draws a similar grid with four rows and four columns

def do_twice(f):
    f();
    f();

def do_four(f):
    do_twice(f);
    do_twice(f);

def print_beam():
    print('+ - - - -', end=' ');

def print_post(spaces):
    print('|' + ' '*spaces, end=' ');

def print_plus():
    print('+', end=' ' );

def print_dash():
    print('-', end=' ');

def print_end():
    print();

def print_beams():
    do_twice(print_beam);

def print_posts(spaces):
    do_twice(print_post(spaces));

def print_grid():
    # n x n grid
    print_beams();
    print_plus();
    print_end();

    print_posts();
    print_post()

print_grid();
