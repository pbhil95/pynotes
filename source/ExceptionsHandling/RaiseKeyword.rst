========================================
raise keyword with example in Python
========================================

.. index::
   single: raise keyword

Python raise keyword
======================

``except`` is a keyword (case-sensitive) in python, it is used to raise an Exception/Error with a customized message and stops the execution of the programs.

It is very useful when you want to work with the input validations. For example – if you are working with the positive numbers and someone inputs a negative number, in this case, we can raise an error and stop the program’s execution.

**Syntax of raise keyword:**
::

    if test_condition:
        raise Exception(Message)

**Example:**
::

        Input:
        string = "Hello"

        if string=="Hello" or string=="Hi" or string=="Bye":
            raise Exception("This word is not allowed")

        Output:
        Exception: This word is not allowed

Python examples of raise keyword
-------------------------------------

**Example 1: Input a positive number and raise an exception if input is a negative value .**
::

    # python code to demonstrate example of 
    # raise keyword 

    # Input a positive number and raise an exception 
    # if input is a negative value 

    num = int(input("Enter a positive number: "))

    if num<0:
        raise Exception("Please input only positive value ")

    print("num = ", num)

**First run:**

.. container:: outputs

    | **OUTPUT :**
    | Enter a positive number: 20
    | num =  20

**Second run:**

.. container:: outputs

    | **OUTPUT :**
    | Enter a positive number: -10
    | Traceback (most recent call last):
    |  File "/home/main.py", line 10, in <module>
    |    raise Exception("Please input only positive value ")
    | Exception: Please input only positive value

**Example 2: Input a string and raise an exception on specific words.**
::

    # python code to demonstrate example of 
    # raise keyword 

    # Input a string and raise an exception on specific words

    string = input("Input a string: ")

    # words - we are checking
    # 'Hello', 'Hi' or 'Bye'
    if string=="Hello" or string=="Hi" or string=="Bye":
        raise Exception("This word is not allowed")

    print("The input was: ", string)


**First run:**

.. container:: outputs

    | **OUTPUT :**
    | Input a string: IncludeHelp
    | The input was:  IncludeHelp

**Second run:**

.. container:: outputs

    | **OUTPUT :**
    | Input a string: Hello 
    | Traceback (most recent call last):
    |  File "/home/main.py", line 11, in <module>
    |    raise Exception("This word is not allowed")
    | Exception: This word is not allowed

**Third run:**

.. container:: outputs

    | **OUTPUT :**
    | Input a string: Bye
    | Traceback (most recent call last):
    |  File "/home/main.py", line 11, in <module>
    |    raise Exception("This word is not allowed")
    | Exception: This word is not allowed
