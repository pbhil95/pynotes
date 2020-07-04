===============
Python Lists
===============

Learning Objectives:
====================

At the end of this chapter the students will be able to understand:

* :ref:`list`
* :ref:`list-methods`

Python Collections (Arrays)
============================

There are four collection data types in the Python programming language:

* List is a collection which is ordered and changeable. Allows duplicate members.
* Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
* Set is a collection which is unordered and unindexed. No duplicate members.
* Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

*When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.*

.. _list:

List
======

A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

Create a List
--------------
::

    thislist = ["apple", "banana", "cherry"]
    print(thislist)

.. container:: outputs

    | **OUTPUT :**
    | ['apple', 'banana', 'cherry']

::

    # empty list
    my_list = []

    # list of integers
    my_list = [1, 2, 3]

    # list with mixed data types
    my_list = [1, "Hello", 3.4]

    # nested list
    my_list = ["mouse", [8, 4, 6], ['a']]

Access Items
--------------

You access the list items by referring to the index number:

**Print the second item of the list:**
::

    thislist = ["apple", "banana", "cherry"]
    print(thislist[1])

.. container:: outputs

    | **OUTPUT :**
    | banana

::

    # Nested List
    n_list = ["Happy", [2, 0, 1, 5]]

    # Nested indexing
    print(n_list[0][1])

    print(n_list[1][3])

    # Error! Only integer can be used for indexing
    print(my_list[4.0])

Negative Indexing
------------------

Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.

**Print the last item of the list:**
::

    thislist = ["apple", "banana", "cherry"]
    print(thislist[-1])

.. container:: outputs

    | **OUTPUT :**
    | cherry

Range of Indexes
------------------

You can specify a range of indexes by specifying where to start and where to end the range.When specifying a range, the return value will be a new list with the specified items.

**Return the third, fourth, and fifth item:**
::

    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[2:5])

.. container:: outputs

    | **OUTPUT :**
    | ['cherry', 'orange', 'kiwi']

.. note::
    
    The search will start at index 2 (included) and end at index 5 (not included).Remember that the first item has index 0.

By leaving out the start value, the range will start at the first item:

**This example returns the items from the beginning to "orange":**
::

    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[:4])

.. container:: outputs

    | **OUTPUT :**
    | ['apple', 'banana', 'cherry', 'orange']

By leaving out the end value, the range will go on to the end of the list:

**This example returns the items from "cherry" and to the end:**
::

    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[2:])

.. container:: outputs

    | **OUTPUT :**
    | ['cherry', 'orange', 'kiwi', 'melon', 'mango']

Range of Negative Indexes
---------------------------

Specify negative indexes if you want to start the search from the end of the list:

**This example returns the items from index -4 (included) to index -1 (excluded)**
::

    thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
    print(thislist[-4:-1])

.. container:: outputs

    | **OUTPUT :**
    | ['orange', 'kiwi', 'melon']

Change Item Value
-------------------

To change the value of a specific item, refer to the index number:

**Change the second item:**
::

    thislist = ["apple", "banana", "cherry"]
    thislist[1] = "blackcurrant"
    print(thislist)

.. container:: outputs

    | **OUTPUT :**
    | ['apple', 'blackcurrant', 'cherry']

Loop Through a List
---------------------

You can loop through the list items by using a for loop:

**Print all items in the list, one by one:**
::

    thislist = ["apple", "banana", "cherry"]
    for x in thislist:
    print(x)

.. container:: outputs

    | **OUTPUT :**
    | apple
    | banana
    | cherry

You will learn more about for loops in our Python For Loops Chapter.
Check if Item Exists.To determine if a specified item is present in a list use the in keyword:

**Check if "apple" is present in the list:**
::

    thislist = ["apple", "banana", "cherry"]
    if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

.. container:: outputs

    | **OUTPUT :**
    | Yes, 'apple' is in the fruits list

List Length
-------------

To determine how many items a list has, use the
len() function:

**Print the number of items in the list:**
::

    thislist = ["apple", "banana", "cherry"]
    print(len(thislist))

.. container:: outputs

    | **OUTPUT :**
    | 3

Add Items
-----------

.. function:: append()

To add an item to the end of the list, use the append() method:

**Using the append() method to append an item:**
::

    thislist = ["apple", "banana", "cherry"]
    thislist.append("orange")
    print(thislist)

.. container:: outputs

    | **OUTPUT :**
    | ['apple', 'banana', 'cherry', 'orange']
    
.. function:: insert()

To add an item at the specified index, use the insert() method:

**Insert an item as the second position:**
::

    thislist = ["apple", "banana", "cherry"]
    thislist.insert(1, "orange")
    print(thislist)

.. container:: outputs

    | **OUTPUT :**
    | ['apple', 'orange', 'banana', 'cherry']

Remove Item
-------------

.. function:: remove()

**There are several methods to remove items from a list:**

**The remove() method removes the specified item:**
::

    thislist = ["apple", "banana", "cherry"]
    thislist.remove("banana")
    print(thislist)

.. container:: outputs

    | **OUTPUT :**
    | ['apple', 'cherry']

.. _func-pop:

.. function:: pop() 
    :noindex:

**The pop() method removes the specified index, (or the last item if index is not specified):**
::

    thislist = ["apple", "banana", "cherry"]
    thislist.pop()
    print(thislist)

.. container:: outputs

    | **OUTPUT :**
    | ['apple', 'banana']

**The del keyword removes the specified index:**
::

    thislist = ["apple", "banana", "cherry"]
    del thislist[0]
    print(thislist)

.. container:: outputs

    | **OUTPUT :**
    | ['banana', 'cherry']

**The del keyword can also delete the list completely:**
::

    thislist = ["apple", "banana", "cherry"]
    del thislist

.. _func-clear:

.. function:: clear() 
    :noindex:

**The clear() method empties the list:**
::

    thislist = ["apple", "banana", "cherry"]
    thislist.clear()
    print(thislist)

.. container:: outputs

    | **OUTPUT :**
    | []

Copy a List
-------------

.. warning::
    You cannot copy a list simply by typing list2 = 
    list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

There are ways to make a copy, one way is to use the built-in List method
copy().

.. _func-copy:

.. function:: copy() 
    :noindex:

**Make a copy of a list with the copy() method:**
::

    thislist = ["apple", "banana", "cherry"]
    mylist = thislist.copy()
    print(mylist)

.. container:: outputs

    | **OUTPUT :**
    | ['apple', 'banana', 'cherry']

Another way to make a copy is to use the built-in method list().

**Make a copy of a list with the list() method:**
::

    thislist = ["apple", "banana", "cherry"]
    mylist = list(thislist)
    print(mylist)

Join Two Lists
----------------

There are several ways to join, or concatenate, two or more lists in Python.One of the easiest ways are by using the + operator.

**Join two list:**
::

    list1 = ["a", "b" , "c"]
    list2 = [1, 2, 3]

    list3 = list1 + list2
    print(list3)

.. container:: outputs

    | **OUTPUT :**
    | ['a', 'b', 'c', 1, 2, 3]

Another way to join two lists are by appending all the items from list2 into list1, one by one:

**Append list2 into list1:**
::

    list1 = ["a", "b" , "c"]
    list2 = [1, 2, 3]

    for x in list2:
    list1.append(x)

    print(list1)

.. container:: outputs

    | **OUTPUT :**
    | ['a', 'b', 'c', 1, 2, 3]

Or you can use the extend() method, which purpose is to add elements from one list to another list:

.. function:: extend()

**Use the extend() method to add list2 at the end of list1:**
::

    list1 = ["a", "b" , "c"]
    list2 = [1, 2, 3]

    list1.extend(list2)
    print(list1)

.. container:: outputs

    | **OUTPUT :**
    | ['a', 'b', 'c', 1, 2, 3]

The list() Constructor
-------------------------

It is also possible to use the list() constructor to make a new list.

**Using the list() constructor to make a List:**
::

    thislist = list(("apple", "banana", "cherry")) print(thislist)

.. function:: sort()

The sort function can be used to sort the list in both ascending and descending order.
List's methods
::

    numbers = [1, 3, 4, 2] 
    numbers.sort() 
    print(numbers) 

    decimalnumber = [2.01, 2.00, 3.67, 3.28, 1.68] 
    decimalnumber.sort(reverse=True) 
    print(decimalnumber) 

    words = ["Geeks", "For", "Geeks"] 
    words.sort() 
    print(words)

    list1 = [(1,2),(3,3),(1,1)] 
    list1.sort(key=sortSecond)  
    print(list1) 

.. container:: outputs


    | **OUTPUT :**
    | [1, 2, 3, 4]
    | [3.67, 3.28, 2.01, 2.0, 1.68]
    | ['For', 'Geeks', 'Geeks']

.. note:: for reverse sorting ``list.sort(reverse=True)`` and sorting by second element ``list.sort(key=sortSecond)``.

.. function:: count()

``count()`` is an inbuilt function in Python that returns count of how many times a given object occurs in list.
::

    list1 = [1, 1, 1, 2, 3, 2, 1] 
    list2 = ['a', 'a', 'a', 'b', 'b', 'a', 'c', 'b']
    list3 = ['Cat', 'Bat', 'Sat', 'Cat', 'cat', 'Mat'] 

.. container:: outputs


    | **OUTPUT :**
    | 4
    | 3
    | 2

.. function:: index()

index() is an inbuilt function in Python, which searches for given element from start of the list and returns the lowest index where the element appears. 

**Syntax():**
::

    list_name.index(element, start, end)

* start (Optional) - The position from where the search begins.
* end (Optional) - The position from where the search ends.

::

    list1 = [1, 2, 3, 4, 1, 1, 1, 4, 5] 
    print(list1.index(4)) 

    list2 = ['cat', 'bat', 'mat', 'cat', 'pet'] 
    print(list2.index('cat')) 

.. container:: outputs

    | **OUTPUT :**
    | 3
    | 0

.. function:: reverse()

This function reverses the elements of list.
::

    lis = [2, 1, 3, 5, 3, 8] 
    lis.reverse()
    print(lis)

.. container:: outputs

    | **OUTPUT :**
    | [8, 3, 5, 3, 1, 2]

.. _list-methods:

List Methods
=============

.. csv-table::
   :header: Method,Description
   :widths: 30, 70
   :file: csv/list_methods.csv
   :align: center 

.. |func-pop| replace:: ``pop()``
.. |func-clear| replace:: ``clear()``
.. |func-copy| replace:: ``copy()``