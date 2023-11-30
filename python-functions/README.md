Requirements
Python Scripts
Recommended editors: Visual studio code
All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
All your files should end with a new line
A README.md file at the root of the python-coding repo, containing a description of the repository
A README.md file, at the root of the folder of this project, is mandatory
The length of your files will be tested using wc

0. a + b
mandatory
Write a function that adds two integers and returns the result.

Prototype: def add(a, b):
Returns the value of a + b
You are not allowed to import any module
You don’t need to understand __import__

guillaume@ubuntu:~/$ cat 0-main.py
#!/usr/bin/env python3
add = #__import__('0-sum').add

print(add(1, 2))
print(add(98, 0))
print(add(100, -2))

guillaume@ubuntu:~/$ ./0-main.py
3
98
98
guillaume@ubuntu:~/$ 