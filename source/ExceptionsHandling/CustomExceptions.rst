.. index::
   index: Custom Exceptions

===============================
Custom Exceptions in Python
===============================

Python has numerous built-in exceptions that force your program to output an error when something in the program goes wrong. However, sometimes you may need to create your own custom exceptions that serve your purpose.

Creating Custom Exceptions
=============================

In Python, users can define custom exceptions by creating a new class. **This exception class has to be derived, either directly or indirectly, from the built-in Exception class**. Most of the built-in exceptions are also derived from this class.

Example: User-Defined Exception in Python
-----------------------------------------------------

In this example, we will illustrate how user-defined exceptions can be used in a program to raise and catch errors.

This program will ask the user to enter a number until they guess a stored number correctly. To help them figure it out, a hint is provided whether their guess is greater than or less than the stored number.
::

    class Error(Exception):
        """Base class for other exceptions"""
        pass

    class ValueTooSmallError(Error):
        """Raised when the input value is too small"""
        pass

    class ValueTooLargeError(Error):
        """Raised when the input value is too large"""
        pass

    number = 10

    while True:
        try:
            i_num = int(input("Enter a number: "))
            if i_num < number:
                raise ValueTooSmallError
            elif i_num > number:
                raise ValueTooLargeError
            break
        except ValueTooSmallError:
            print("This value is too small, try again!")
            print()
        except ValueTooLargeError:
            print("This value is too large, try again!")
            print()

    print("Congratulations! You guessed it correctly.")

Here is a sample run of this program.

.. container:: outputs

    | **OUTPUT :**
    | Enter a number: 12
    | This value is too large, try again!
    |
    | Enter a number: 0
    | This value is too small, try again!
    |
    | Enter a number: 8
    | This value is too small, try again!
    |
    | Enter a number: 10
    | Congratulations! You guessed it correctly.

We have defined a base class called ``Error``.

The other two exceptions (``ValueTooSmallError`` and ``ValueTooLargeError``) that are actually raised by our program are derived from this class. This is the standard way to define user-defined exceptions in Python programming, but you are not limited to this way only.

Customizing Exception Classes
================================

We can further customize this class to accept other arguments as per our needs.

**Let's look at one example:**
::

    class SalaryNotInRangeError(Exception):
        """Exception raised for errors in the input salary.

        Attributes:
            salary -- input salary which caused the error
            message -- explanation of the error
        """

        def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
            self.salary = salary
            self.message = message
            super().__init__(self.message)


    salary = int(input("Enter salary amount: "))
    if not 5000 < salary < 15000:
        raise SalaryNotInRangeError(salary)

.. container:: outputs

    | **OUTPUT :**
    | Enter salary amount: 2000
    | Traceback (most recent call last):
    |  File "<string>", line 17, in <module>
    |    raise SalaryNotInRangeError(salary)
    | __main__.SalaryNotInRangeError: Salary is not in (5000, 15000) range

Here, we have overridden the constructor of the Exception class to accept our own custom arguments salary and message. Then, the constructor of the parent Exception class is called manually with the self.message argument using ``super()``.
