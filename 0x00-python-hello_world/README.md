
0x00. Python - Hello, World
 Level: Novice
 By Guillaume, CTO at Holberton School
 Weight: 1
 Ongoing project - started 01-03-2022, must end by 01-04-2022 (in about 12 hours) - you're done with 22% of tasks.
 Checker was released at 01-03-2022 12:00 AM
 QA review fully automated.
Concepts
For this project, students are expected to look at this concept:

Python programming


Author’s disclaimer
Welcome to the Python world!

After 3 months of C, you will start Python today.
The first projects are more "C-oriented" - no tricks, no funky syntax - simple!
If you've already played with Python, don't worry, fun things will come.
You'll soon find that with Python (and the majority of higher level languages), there are ten different ways to do the same thing. Some tasks will expect only one implementation, while other tasks will have multiple possible implementations.
Like C, Python also has a linter / style guide like Betty, called PEP8, also now known as PyCode. At Holberton, we won't start off with using PyCode, because it's much more strict compared to PEP8. Don't worry if you see a warning when you are running PEP8, you can ignore it.

Enjoy!

- Guillaume, CTO at Holberton
Resources
Read or watch:

The Python tutorial (only the first three chapters below)
Whetting Your Appetite
Using the Python Interpreter
An Informal Introduction to Python (Read up until “3.1.2. Strings” included)
How To Use String Formatters in Python 3
Learn to Program
More Control Flow Tools (Read until “4.6. Defining Functions” included)
Myths about Indentation
IndentationError
How To Use String Formatters in Python 3
Learn to Program
Learn to Program 2 : Looping
PEP 8 – Style Guide for Python Code
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
Why Python programming is awesome
Who created Python
Who is Guido van Rossum
Where does the name ‘Python’ come from
What is the Zen of Python
How to use the Python interpreter
How to print text and variables using print
How to use strings
What are indexing and slicing in Python
What is the official Holberton Python coding style and how to check your code with PEP 8
Why indentation is so important in Python
How to use the if, if ... else statements
How to use comments
How to affect values to variables
How to use the while and for loops
How is Python’s for different from C‘s?
How to use the break and continues statements
How to use else clauses on loops
What does the pass statement do, and when to use it
How to use range
What is a function and how do you use functions
What does return a function that does not use any return statement
Scope of variables
What’s a traceback
What are the arithmetic operators and how to use them
Requirements
Python Scripts
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/python3
A README.md file at the root of the holbertonschool-higher_level_programming repo, containing a description of the repository
A README.md file, at the root of the folder of this project, is mandatory
Your code should use the PEP 8 style (version 1.7.*)
All your files must be executable
The length of your files will be tested using wc
More Info
Zen
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
Install PEP8
Pycodestyle is now the new standard of Python style code, but at school we will use PEP8, version 1.7.* Don’t worry, pycodestyle is based on pep8. The hardest part now is to install it for Python 3:

Regular Ubuntu 14.04 install
$ sudo apt-get install python3-pep8
Using Pip3
Install Pip3
$ sudo apt-get install python3-pip
Install Pep8
$ sudo apt-get install python3-pip
$ sudo pip3 install -Iv pep8==1.7.0
-> Make sure you have the right version

$ pep8 --version
1.7.0
$
Finally, if you can’t make it work, please use the “container-on-demand” tool to “PEP8” your files in a pre-configured container.





Quiz questions
Show

Tasks
0. Hello, print
mandatory
Write a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.

Use the function print
guillaume@ubuntu:~/py/0x00$ ./0-print.py 
"Programming is like building a multilingual puzzle
guillaume@ubuntu:~/py/0x00$
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x00-python-hello_world
File: 0-print.py
   
1. Copy - Cut - Paste
mandatory
Complete this 1-edges.py

You can find the source code 1-edges.py
You are not allowed to use any loops or conditional statements
Your program should be exactly 8 lines long
word_first_3 should contain the first 3 letters of the variable word
word_last_2 should contain the last 2 letters of the variable word
middle_word should contain the value of the variable word without the first and last letters
guillaume@ubuntu:~/py/0x00$ ./1-edges.py
First 3 letters: Hol
Last 2 letters: on
Middle word: olberto
guillaume@ubuntu:~/py/0x00$ wc -l 1-edges.py
8 1-edges.py
guillaume@ubuntu:~/py/0x00$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x00-python-hello_world
File: 1-edges.py
   
2. Positive anything is better than negative nothing
mandatory
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print whether the number stored in the variable number is positive or negative.

You can find the source code 2-pon.py
The variable number will store a different value every time you will run this program
You don’t have to understand what import, random. randint do. Please do not touch this code
The output of the program should be:
The number, followed by
if the number is greater than 0: is positive
if the number is 0: is zero
if the number is less than 0: is negative
followed by a new line
guillaume@ubuntu:~/0x00$ ./2-positive_or_negative.py 
-4 is negative
guillaume@ubuntu:~/0x00$ ./2-positive_or_negative.py 
0 is zero
guillaume@ubuntu:~/0x00$ ./2-positive_or_negative.py 
-3 is negative
guillaume@ubuntu:~/0x00$ ./2-positive_or_negative.py 
-10 is negative
guillaume@ubuntu:~/0x00$ ./2-positive_or_negative.py 
10 is positive
guillaume@ubuntu:~/0x00$ ./2-positive_or_negative.py 
-5 is negative
guillaume@ubuntu:~/0x00$ ./2-positive_or_negative.py 
6 is positive
guillaume@ubuntu:~/0x00$ ./2-positive_or_negative.py 
7 is positive
guillaume@ubuntu:~/0x00$ ./2-positive_or_negative.py 
5 is positive
guillaume@ubuntu:~/0x00$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x00-python-hello_world
File: 2-positive_or_negative.py
   
3. The last digit
mandatory
This program will assign a random signed number to the variable number each time it is executed. Complete the source code in order to print the last digit of the number stored in the variable number.

You can find the source code 3-last_digit.py
The variable number will store a different value every time you will run this program
You don’t have to understand what import, random.randint do. Please do not touch this code. This line should not change: number = random.randint(-10000, 10000)
The output of the program should be:
The string Last digit of, followed by
the number, followed by
the string is, followed by the last digit of number, followed by
if the last digit is greater than 5: the string and is greater than 5
if the last digit is 0: the string and is 0
if the last digit is less than 6 and not 0: the string and is less than 6 and not 0
followed by a new line
guillaume@ubuntu:~/0x00$ ./3-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/0x00$ ./3-last_digit.py
Last digit of -626 is -6 and is less than 6 and not 0
guillaume@ubuntu:~/0x00$ ./3-last_digit.py
Last digit of 1144 is 4 and is less than 6 and not 0
guillaume@ubuntu:~/0x00$ ./3-last_digit.py
Last digit of -9200 is 0 and is 0
guillaume@ubuntu:~/0x00$ ./3-last_digit.py
Last digit of 5247 is 7 and is greater than 5
guillaume@ubuntu:~/0x00$ ./3-last_digit.py
Last digit of -9318 is -8 and is less than 6 and not 0
guillaume@ubuntu:~/0x00$ ./3-last_digit.py
Last digit of 3369 is 9 and is greater than 5
guillaume@ubuntu:~/0x00$ ./3-last_digit.py
Last digit of -5224 is -4 and is less than 6 and not 0
guillaume@ubuntu:~/0x00$ ./3-last_digit.py
Last digit of -4485 is -5 and is less than 6 and not 0
guillaume@ubuntu:~/0x00$ ./3-last_digit.py
Last digit of 3850 is 0 and is 0
guillaume@ubuntu:~/0x00$ ./3-last_digit.py
Last digit of 5169 is 9 and is greater than 5
guillaume@ubuntu:~/0x00$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x00-python-hello_world
File: 3-last_digit.py
   
4. Hexadecimal printing
mandatory
Write a program that prints all numbers from 0 to 98 in decimal and in hexadecimal (as in the following example)

You can only use one print function with string format
You can only use one loop in your code
You are not allowed to store numbers or strings in a variable
You are not allowed to import any module
guillaume@ubuntu:~/0x00$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
3 = 0x3
4 = 0x4
5 = 0x5
6 = 0x6
7 = 0x7
8 = 0x8
9 = 0x9
10 = 0xa
11 = 0xb
12 = 0xc
13 = 0xd
14 = 0xe
15 = 0xf
16 = 0x10
17 = 0x11
18 = 0x12
...
96 = 0x60
97 = 0x61
98 = 0x62
guillaume@ubuntu:~/0x00$
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x00-python-hello_world
File: 4-print_hexa.py
   
5. 00...99
mandatory
Write a program that prints numbers from 0 to 99.

Numbers must be separated by ,, followed by a space
Numbers should be printed in ascending order, with two digits
The last number should be followed by a new line
You can only use no more than 2 print functions with string format
You can only use one loop in your code
You are not allowed to store numbers or strings in a variable
You are not allowed to import any module
guillaume@ubuntu:~/0x00$ ./5-print_comb2.py
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99
guillaume@ubuntu:~/0x00$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x00-python-hello_world
File: 5-print_comb2.py
   
6. Inventing is a combination of brains and materials. The more brains you use, the less material you need
mandatory
Write a program that prints all possible different combinations of two digits.

Numbers must be separated by ,, followed by a space
The two digits must be different
01 and 10 are considered the same combination of the two digits 0 and 1
Print only the smallest combination of two digits
Numbers should be printed in ascending order, with two digits
The last number should be followed by a new line
You can only use no more than 3 print functions with string format
You can only use no more than 2 loops in your code
You are not allowed to store numbers or strings in a variable
You are not allowed to import any module
guillaume@ubuntu:~/0x00$ ./6-print_comb3.py
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
guillaume@ubuntu:~/0x00$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x00-python-hello_world
File: 6-print_comb3.py
   
7. a + b
mandatory
Write a function that adds two integers and returns the result.

Prototype: def add(a, b):
Returns the value of a + b
You are not allowed to import any module
You don’t need to understand __import__

guillaume@ubuntu:~/0x00$ cat 7-main.py
#!/usr/bin/env python3
add = __import__('7-add').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))

guillaume@ubuntu:~/0x00$ ./7-main.py
3
98
98
guillaume@ubuntu:~/0x00$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x00-python-hello_world
File: 7-add.py
   
8. a ^ b
mandatory
Write a function that computes a to the power of b and return the value.

Prototype: def pow(a, b):
Returns the value of a ^ b
You are not allowed to import any module
You don’t need to understand __import__

guillaume@ubuntu:~/0x00$ cat 8-main.py
#!/usr/bin/env python3
pow = __import__('8-pow').pow

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))

guillaume@ubuntu:~/0x00$ ./8-main.py
4
9604
1
0.0001
-1024
guillaume@ubuntu:~/0x00$ 
Repo:

GitHub repository: holbertonschool-higher_level_programming
Directory: 0x00-python-hello_world
File: 8-pow.py
   
Copyright © 2021 Holberton Inc, All rights reserved.
