=======================
Built-in Exceptions
=======================

Exception hierarchy
====================

.. literalinclude:: ExceptionHierachy.txt

Built-in Exceptions Python
==============================

.. csv-table::
   :header: Exception,Cause of Error
   :widths: 30, 70
   :file: csv/BuiltInErrors.csv
   :align: center 

Exceptions
==============

Before you start learning the built-in exceptions, let's just quickly revise the four main components of exception handling:

* **Try:** It will run the code block in which you expect an error to occur.
* **Except:** Here, you will define the type of exception you expect in the try block (built-in or custom).
* **Else:** If there isn't any exception, then this block of code will be executed (consider this as a remedy or a fallback option if you expect a part of your script to produce an exception).
* **Finally:** Irrespective of whether there is an exception or not, this block of code will always be executed.

Type Error
------------
::

    a = 2
    b = 'DataCamp'
    a + b

.. container:: outputs

    | **OUTPUT :**
    | TypeError Traceback (most recent call last)
    | <ipython-input-7-86a706a0ffdf> in <module>
    |  1 a = 2
    |  2 b = 'DataCamp'
    | ----> 3 a + b
    | TypeError: unsupported operand type(s) for +: 'int' and 'str'


Zero Division Error
-----------------------
::

    100 / 0

.. container:: outputs

    | **OUTPUT :**
    | ZeroDivisionError Traceback (most recent call last)
    | <ipython-input-43-e9e866a10e2a> in <module>
    | ----> 1 100 / 0


Keyboard Interrupt Error
---------------------------

The ``KeyboardInterrupt`` exception is raised when you try to stop a running program by pressing ctrl+c or ctrl+z in a command line or interrupting the kernel in Jupyter Notebook. Sometimes you might not intend to interrupt a program, but by mistake, it happens, in which case using exception handling to avoid such issues can be helpful.

In the below example, if you run the cell and interrupt the kernel, the program will raise a ``KeyboardInterrupt exception. inp = input()`` Let's now handle the KeyboardInterrupt exception.
::

    try:
        inp = input()
        print ('Press Ctrl+C or Interrupt the Kernel:')
    except KeyboardInterrupt:
        print ('Caught KeyboardInterrupt')
    else:
        print ('No exception occurred')

.. container:: outputs

    | **OUTPUT :**
    | Caught KeyboardInterrupt

Standard Error
-----------------

Let's learn about some of the standard errors that could usually occur while programming.
Arithmetic Error

* **Zero Division Error**
* **OverFlow Error**
* **Floating Point Error**

All of the above exceptions fall under the Arithmetic base class and are raised for errors in arithmetic operations, as discussed here.

Zero Division
++++++++++++++++

When the divisor (second argument of the division) or the denominator is zero, then the resultant raises a zero division error.
::

    try:  
        a = 100 / 0
        print (a)
    except ZeroDivisionError:  
            print ("Zero Division Exception Raised." )
    else:  
        print ("Success, no error!")

.. container:: outputs

    | **OUTPUT :**
    | Zero Division Exception Raised.

OverFlow Error
+++++++++++++++++

The Overflow Error is raised when the result of an arithmetic operation is out of range. OverflowError is raised for integers that are outside a required range.
::

    try:  
        import math
        print(math.exp(1000))
    except OverflowError:  
            print ("OverFlow Exception Raised.")
    else:  
        print ("Success, no error!")

.. container:: outputs

    | **OUTPUT :**
    | OverFlow Exception Raised.

Assertion Error
----------------------

When an assert statement is failed, an Assertion Error is raised.

Let's take an example to understand the assertion error. Let's say you have two variables a and b, which you need to compare. To check whether a and b are equal or not, you apply an assert keyword before that, which will raise an Assertion exception when the expression will return false.
::

    try:  
        a = 100
        b = "DataCamp"
        assert a == b
    except AssertionError:  
            print ("Assertion Exception Raised.")
    else:  
        print ("Success, no error!")

.. container:: outputs

    | **OUTPUT :**
    | Assertion Exception Raised.

Attribute Error
-------------------

When a non-existent attribute is referenced, and when that attribute reference or assignment fails, an attribute error is raised.

In the below example, you can observe that the Attributes class object has no attribute with the name attribute.
::

    class Attributes(object):
        a = 2
        print (a)

    try:
        object = Attributes()
        print (object.attribute)
    except AttributeError:
        print ("Attribute Exception Raised.")

.. container:: outputs

    | **OUTPUT :**
    | 2
    | Attribute Exception Raised.

Import Error
---------------

ImportError is raised when you try to import a module that does not exist (unable to load) in its standard path or even when you make a typo in the module's name.
::

    import nibabel

.. container:: outputs

    | **OUTPUT :**
    | ModuleNotFoundError Traceback (most recent call last)
    | <ipython-input-6-9e567e3ae964> in <module>
    | ----> 1 import nibabel
    | ModuleNotFoundError: No module named 'nibabel'

Lookup Error
----------------

Lookup Error acts as a base class for the exceptions that occur when a key or index used on a mapping or sequence of a list/dictionary is invalid or does not exists.

The two types of exceptions raised are:

* **KeyError**
* **IndexError**

Key Error
++++++++++++++

If a key you are trying to access is not found in the dictionary, a key error exception is raised.
::

    try:  
        a = {1:'a', 2:'b', 3:'c'}  
        print (a[4])  
    except LookupError:  
        print ("Key Error Exception Raised.")
    else:  
        print ("Success, no error!")

.. container:: outputs

    | **OUTPUT :**
    | Key Error Exception Raised.

Index Error
+++++++++++++++++++

When you are trying to access an index (sequence) of a list that does not exist in that list or is out of range of that list, an index error is raised.
::

    try:  
        a = ['a', 'b', 'c']  
        print (a[4])  
    except LookupError:  
        print ("Index Error Exception Raised, list index out of range")
    else:  
        print ("Success, no error!")

.. container:: outputs

    | **OUTPUT :**
    | Index Error Exception Raised, list index out of range

Memory Error
--------------------

Out of Memory Error
++++++++++++++++++++++

Memory errors are mostly dependent on your systems RAM and are related to Heap. If you have large objects (or) referenced objects in memory, then you will see OutofMemoryError (Source). It can be caused due to various reasons:

* Using a 32-bit Python Architecture (Maximum Memory Allocation given is very low, between 2GB - 4GB).
* Loading a very large data file
* Running a Machine Learning/Deep Learning model and many more.

Recursion Error
------------------------

It is related to stack and occurs when you call functions. As the name suggests, recursion error transpires when too many methods, one inside another is executed (one with an infinite recursion), which is limited by the size of the stack.

Name Error
----------------

Name Error is raised when a local or global name is not found.

In the below example, ans variable is not defined. Hence, you will get a name error.
::

    try:
        print (ans)
    except NameError:  
        print ("NameError: name 'ans' is not defined")
    else:  
        print ("Success, no error!")

.. container:: outputs


    | **OUTPUT :**
    | NameError: name 'ans' is not defined

Runtime Error
-----------------------

Not Implemented Error
+++++++++++++++++++++++++++

This section of the tutorial is derived from this Source. Runtime Error acts as a base class for the NotImplemented Error. Abstract methods in user-defined classes should raise this exception when the derived classes override the method.
::

    class BaseClass(object):
        """Defines the interface"""
        def __init__(self):
            super(BaseClass, self).__init__()
        def do_something(self):
            """The interface, not implemented"""
            raise NotImplementedError(self.__class__.__name__ + '.do_something')

    class SubClass(BaseClass):
        """Implementes the interface"""
        def do_something(self):
            """really does something"""
            print (self.__class__.__name__ + ' doing something!')
    
    SubClass().do_something()
    BaseClass().do_something()

.. container:: outputs

    | **OUTPUT :**
    | SubClass doing something!

    | NotImplementedError Traceback (most recent call last)
    | <ipython-input-1-57792b6bc7e4> in <module>
    |  14
    |  15 SubClass().do_something()
    | ---> 16 BaseClass().do_something()

    | <ipython-input-1-57792b6bc7e4> in do_something(self)
    |  5  def do_something(self):
    |  6   """The interface, not implemented"""
    | ----> 7   raise NotImplementedError(self.__class__.__name__ + '.do_something')
    |  8
    |  9 class SubClass(BaseClass):
    | 
    | NotImplementedError: BaseClass.do_something

Type Error
--------------

Type Error Exception is raised when two different or unrelated types of operands or objects are combined.

In the below example, an integer and a string are added, which results in a type error.
::

    try:
        a = 5
        b = "DataCamp"
        c = a + b
    except TypeError:
        print ('TypeError Exception Raised')
    else:
        print ('Success, no error!')

.. container:: outputs

    | **OUTPUT :**
    | TypeError Exception Raised

Value Error
---------------

Value error is raised when the built-in operation or a function receives an argument that has a correct type but invalid value.

In the below example, the built-in operation float receives an argument, which is a sequence of characters (value), which is invalid for a type float.
::

    try:
        print (float('DataCamp'))
    except ValueError:
        print ('ValueError: could not convert string to float: \'DataCamp\'')
    else:
        print ('Success, no error!')

.. container:: outputs

    | **OUTPUT :**
    | ValueError: could not convert string to float: 'DataCamp'
