==============
Python Basic
==============

Learning Objectives:
====================

At the end of this chapter the students will be able to understand:

* :ref:`interactive-mode`
* :ref:`script-mode`
* :ref:`Python-Scripts-Using-the-Command-Line`


.. _interactive-mode:

Interactive Mode
=================

Here, when we type Python statement, interpreter displays the result(s) immediately. That means, when we type Python
expression / statement / command after the prompt (>>>), the Python immediately responses with the
output of it::
   
       Python 3.x.y
       [GCC 4.x] on linux
       Type "help", "copyright", "credits" or "license" for more information.
       >>>3+4
       7

.. _script-mode:

Script Mode
============

In script mode, we type Python program in a file and then use interpreter to execute the content of the file. Working in interactive mode is convenient for beginners and for testing small pieces of code, as one can test them immediately. But for coding of more than few lines, we should always save our code so that it can be **modified and reused**.

.. code-block:: python
    :caption: sum.py

    num1 = int(input("Enter first Number :"))
    num2 = int(input("Enter Second Number: "))
    sum = num1+num2
    print("Sum of two number is :", sum)

.. container:: output

    | **OUTPUT :**
    | Enter first Number   :  5
    | Enter Second Number  :  8
    | Sum of two number is :  13


.. note::

    | Python, in `interactive mode`_, is good enough to learn, experiment or explore, but its only drawback is that we cannot save the statements and have to retype all the statements once again to re-run them.

.. _Python-Scripts-Using-the-Command-Line:

Python Scripts Using the Command-Line
======================================

.. code-block:: 
    :caption: shell

    $ python sum.py
    Hello World!

**Or**

.. code-block::
    :caption: shell

    $ sum.py
    Hello World!

*If this doesn’t work right, maybe you’ll need to check your system PATH, your Python installation, the way you created the sum.py script, the place where you saved it, and so on.*

Redirecting the Output
-----------------------

Sometimes it’s useful to save the output of a script for later analysis. Here’s how you can do that:

.. code-block::
    :caption: shell

    $ sum.py > output.txt
    Hello World!

if you want to add the output of consecutive executions to the end of output.txt, then you must use two angle brackets (>>) instead of one, just like this:

.. code-block::
    :caption: shell

    $ sum.py >> output.txt
    Hello World!