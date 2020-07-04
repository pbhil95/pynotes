==============
Python Tuple
==============

Tuple
========

A tuple in Python is similar to a list. **The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list**.

Creating a Tuple
==================

A tuple is created by placing all the items (elements) inside parentheses ``()``, separated by commas. The parentheses are optional, however, it is a good practice to use them.

A tuple can have any number of items and they may be of different types (integer, float, list, string, etc.).
::

    my_tuple = ()
    print(my_tuple)

    my_tuple = (1, 2, 3)
    print(my_tuple)

    my_tuple = (1, "Hello", 3.4)
    print(my_tuple)

    my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
    print(my_tuple)

.. container:: outputs

    | **OUTPUT :**
    | ()
    | (1, 2, 3)
    | (1, 'Hello', 3.4)
    | ('mouse', [8, 4, 6], (1, 2, 3))

A tuple can also be created without using parentheses. This is known as tuple packing.
::

    my_tuple = 3, 4.6, "dog"
    print(my_tuple)
    a, b, c = my_tuple
    print(a)      
    print(b)      
    print(c)      

.. container:: outputs

    | **OUTPUT :**
    | (3, 4.6, 'dog')
    | 3
    | 4.6
    | dog

**Creating a tuple with one element is a bit tricky. Having one element within parentheses is not enough. We will need a trailing comma to indicate that it is, in fact, a tuple.**
::

    my_tuple = ("hello")
    print(type(my_tuple))  

    my_tuple = ("hello",)
    print(type(my_tuple))  

    my_tuple = "hello",
    print(type(my_tuple))  

.. container:: outputs

    | **OUTPUT :**
    | <class 'str'>
    | <class 'tuple'>
    | <class 'tuple'>

Access Tuple Elements
=======================

There are various ways in which we can access the elements of a tuple.

Indexing
---------

We can use the index operator [] to access an item in a tuple, where the index starts from 0.

So, a tuple having 6 elements will have indices from 0 to 5. Trying to access an index outside of the tuple index range(6,7,... in this example) will raise an IndexError.

The index must be an integer, so we cannot use float or other types. This will result in TypeError.

Likewise, nested tuples are accessed using nested indexing, as shown in the example below.
::

    my_tuple = ('p','e','r','m','i','t')
    print(my_tuple[0])   
    print(my_tuple[5])   
    
    n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
    print(n_tuple[0][3])       
    print(n_tuple[1][1])       

.. container:: outputs

    | **OUTPUT :**
    | p
    | t
    | s
    | 4

Negative Indexing
------------------

Python allows negative indexing for its sequences.

The index of -1 refers to the last item, -2 to the second last item and so on.
::

    my_tuple = ('p', 'e', 'r', 'm', 'i', 't')
    print(my_tuple[-1])
    print(my_tuple[-6])

.. container:: outputs

    | **OUTPUT :**
    | t
    | p

Slicing
---------

We can access a range of items in a tuple by using the slicing operator colon :.
::

    my_tuple = ('p','r','o','g','r','a','m','i','z')
    print(my_tuple[1:4])
    print(my_tuple[:-7])
    print(my_tuple[7:])
    print(my_tuple[:])

.. container:: outputs

    | **OUTPUT :**
    | ('r', 'o', 'g')
    | ('p', 'r')
    | ('i', 'z')
    | ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

Changing a Tuple
==================

Unlike lists, tuples are immutable.

This means that elements of a tuple cannot be changed once they have been assigned. But, if the element is itself a mutable data type like list, its nested items can be changed.

We can also assign a tuple to different values (reassignment).
::

    my_tuple = (4, 2, 3, [6, 5])
    my_tuple[3][0] = 9    
    print(my_tuple)
    my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
    print(my_tuple)

.. container:: outputs

    | **OUTPUT :**
    | (4, 2, 3, [9, 5])
    | ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')

**We can use + operator to combine two tuples. This is called concatenation.**

We can also repeat the elements in a tuple for a given number of times using the * operator.

Both + and * operations result in a new tuple.
::

    print((1, 2, 3) + (4, 5, 6))
    print(("Repeat",) * 3)

.. container:: outputs

    | **OUTPUT :**
    | (1, 2, 3, 4, 5, 6)
    | ('Repeat', 'Repeat', 'Repeat')

Deleting a Tuple
==================

As discussed above, we cannot change the elements in a tuple. It means that we cannot delete or remove items from a tuple.

Deleting a tuple entirely, however, is possible using the keyword del.
::

    my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
    del my_tuple
    print(my_tuple)

.. container:: outputs

    | **OUTPUT :**
    | Traceback (most recent call last):
    |  File "<string>", line 12, in <module>
    | NameError: name 'my_tuple' is not defined

Tuple Methods
==============

Methods that add items or remove items are not available with tuple. Only the following two methods are available.

Some examples of Python tuple methods:
::

    my_tuple = ('a', 'p', 'p', 'l', 'e',)
    print(my_tuple.count('p'))  
    print(my_tuple.index('l'))  

.. container:: outputs

    | **OUTPUT :**
    | 2
    | 3


Advantages of Tuple over List
==============================

Since tuples are quite similar to lists, both of them are used in similar situations. However, there are certain advantages of implementing a tuple over a list. Below listed are some of the main advantages:

* We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
* Since tuples are immutable, iterating through a tuple is faster than with list. So there is a slight performance boost.
* Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
* If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

Converting list to a Tuple
===========================

Code for converting a list and a string into a tuple 
::

    list1 = [0, 1, 2] 
    print(tuple(list1)) 
    print(tuple('python')) # string 'python' 

.. container:: outputs

    | **OUTPUT :**
    | (0, 1, 2)
    | ('p', 'y', 't', 'h', 'o', 'n')

Basic Tuples Operations
========================

Tuples respond to the + and * operators much like strings; they mean concatenation and repetition here too, except that the result is a new tuple, not a string.

In fact, tuples respond to all of the general sequence operations we used on strings in the previous chapter.

.. csv-table::
   :header: Python Expression,Results,Description
   :widths: 40, 30,30
   :file: csv/touple1.csv
   :align: center 

Indexing, Slicing, and Matrixes
================================

Since tuples are sequences, indexing and slicing work the same way for tuples as they do for strings, assuming the following input −
::

    T=('C++', 'Java', 'Python')

.. csv-table::
   :header: Python Expression,Results,Description
   :widths: 30, 30,40
   :file: csv/touple2.csv
   :align: center 

