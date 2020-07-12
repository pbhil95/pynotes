================
Python Sets
================

Learning Objectives:
====================

At the end of this chapter the students will be able to understand:

* :ref:`set`
* :ref:`Python-Set-Operations`
* :ref:`Set-Programming-Example`
* :ref:`Python-Built-in-set-methods`

.. _set:

set
=====

Mathematically a set is a collection of items not in any particular order. A Python set is similar to this mathematical definition with below additional conditions.

* The elements in the set cannot be duplicates.
* The elements in the set are immutable(cannot be modified) but the set as a whole is mutable.
* There is no index attached to any element in a python set. So they do not support any indexing or slicing operation.

Creating a set
================

**The set can be created by enclosing the comma-separated immutable items with the curly braces** ``{}``. Python also provides the set() method, which can be used to create the set by the passed sequence.

Using curly braces
-------------------
::

    Days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}    
    print(Days)    
    print(type(Days))    
    print("looping through the set elements ... ")    
    for i in Days:    
        print(i)    

.. container:: outputs

    | **OUTPUT :**
    | {'Friday', 'Tuesday', 'Monday', 'Saturday', 'Thursday', 'Sunday', 'Wednesday'}
    | <class 'set'>
    | looping through the set elements ... 
    | Friday
    | Tuesday
    | Monday
    | Saturday
    | Thursday
    | Sunday
    | Wednesday

Using ``set()`` method
--------------------------
::

    Days = set(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])    
    print(Days)    
    print(type(Days))    
    print("looping through the set elements ... ")    
    for i in Days:    
        print(i)    

.. container:: outputs

    | **OUTPUT :**
    | {'Friday', 'Wednesday', 'Thursday', 'Saturday', 'Monday', 'Tuesday', 'Sunday'}
    | <class 'set'>
    | looping through the set elements ... 
    | Friday
    | Wednesday
    | Thursday
    | Saturday
    | Monday
    | Tuesday
    | Sunday

Checking immutability of Set
==============================

It can contain any type of element such as integer, float, tuple etc. But mutable elements (list, dictionary, set) can't be a member of set. Consider the following example.
::
      
    set1 = {1,2,3, "JavaTpoint", 20.5, 14}  
    print(type(set1))  
      
    set2 = {1,2,3,["Javatpoint",4]}  
    print(type(set2))  

.. container:: outputs

    | **OUTPUT :**
    | <class 'set'>
    |
    | Traceback (most recent call last)
    | <ipython-input-5-9605bb6fbc68> in <module>
    | #Creating a set which holds mutable elements
    | set2 = {1,2,3,["Javatpoint",4]}
    | print(type(set2))
    | TypeError: unhashable type: 'list'

In the above code, we have created two sets, the set set1 have immutable elements and set2 have one mutable element as a list. While checking the type of set2, it raised an error, which means set can contain only immutable elements.

**Creating an empty set is a bit different because empty curly {} braces are also used to create a dictionary as well. So Python provides the set() method used without an argument to create an empty set.**
::
      
    set3 = {}  
    print(type(set3))     
      
    set4 = set()  
    print(type(set4))  

.. container:: outputs

    | **OUTPUT :**
    | <class 'dict'>
    | <class 'set'>

Checking uniqueness of Set
==============================

Let's see what happened if we provide the duplicate element to the set.
::

    set5 = {1,2,4,4,5,8,9,9,10}  
    print("Return set with unique elements:",set5)  

.. container:: outputs

    | **OUTPUT :**
    | Return set with unique elements: {1, 2, 4, 5, 8, 9, 10}

In the above code, we can see that set5 consisted of multiple duplicate elements when we printed it remove the duplicity from the set.

Adding items to the set
==========================

Python provides the ``add()`` method and ``update()`` method which can be used to add some particular item to the set. The ``add()`` method is used to add a single element whereas the ``update()`` method is used to add multiple elements to the set. Consider the following example.

Using ``add()`` method
------------------------
.. _set-add:

.. function:: add() 
    :noindex:

::

    Months = set(["January","February", "March", "April", "May", "June"])    
    print("\nprinting the original set ... ")    
    print(months)    
    print("\nAdding other months to the set...");    
    Months.add("July");    
    Months.add ("August");    
    print("\nPrinting the modified set...");    
    print(Months)    
    print("\nlooping through the set elements ... ")    
    for i in Months:    
        print(i)    

.. container:: outputs

    | **OUTPUT :**
    | printing the original set ... 
    | {'February', 'May', 'April', 'March', 'June', 'January'}
    |
    | Adding other months to the set...
    |
    | Printing the modified set...
    | {'February', 'July', 'May', 'April', 'March', 'August', 'June', 'January'}
    |
    | looping through the set elements ... 
    | February
    | July
    | May
    | April
    | March
    | August
    | June
    | January 

**To add more than one item in the set, Python provides the** ``update()`` **method. It accepts iterable as an argument.**

Consider the following example.

Using ``update()`` function
---------------------------------
.. _set-update:

.. function:: update() 
    :noindex:

::

    Months = set(["January","February", "March", "April", "May", "June"])    
    print("\nprinting the original set ... ")    
    print(Months)    
    print("\nupdating the original set ... ")    
    Months.update(["July","August","September","October"]);    
    print("\nprinting the modified set ... ")     
    print(Months);  

.. container:: outputs

    | **OUTPUT :**
    | printing the original set ... 
    | {'January', 'February', 'April', 'May', 'June', 'March'}
    |
    | updating the original set ... 
    | printing the modified set ... 
    | {'January', 'February', 'April', 'August', 'October', 'May', 'June', 'July', 'September', 'March'}

Removing items from the set
============================

Python provides the ``discard()`` method and ``remove()`` method which can be used to remove the items from the set. **The difference between these function, using** ``discard()`` **function if the item does not exist in the set then the set remain unchanged whereas** ``remove()`` **method will through an error.**




Using ``discard()`` method
------------------------------
.. function:: discard()

::

    months = set(["January","February", "March", "April", "May", "June"])    
    print("\nprinting the original set ... ")    
    print(months)    
    print("\nRemoving some months from the set...");    
    months.discard("January");    
    months.discard("May");    
    print("\nPrinting the modified set...");    
    print(months)    
    print("\nlooping through the set elements ... ")    
    for i in months:    
        print(i)    

.. container:: outputs

    | **OUTPUT :**
    | printing the original set ... 
    | {'February', 'January', 'March', 'April', 'June', 'May'}
    |
    | Removing some months from the set...
    |
    | Printing the modified set...
    | {'February', 'March', 'April', 'June'}
    |
    | looping through the set elements ... 
    | February
    | March
    | April
    | June

Python provides also the ``remove()`` method to remove the item from the set. Consider the following example to remove the items using remove() method.

Using ``remove()`` function
-------------------------------
.. _set-remove:

.. function:: remove() 
    :noindex:

::

    months = set(["January","February", "March", "April", "May", "June"])    
    print("\nprinting the original set ... ")    
    print(months)    
    print("\nRemoving some months from the set...");    
    months.remove("January");    
    months.remove("May");    
    print("\nPrinting the modified set...");    
    print(months)    

.. container:: outputs

    | **OUTPUT :**
    | printing the original set ... 
    | {'February', 'June', 'April', 'May', 'January', 'March'}
    |
    | Removing some months from the set...
    |
    | Printing the modified set...
    | {'February', 'June', 'April', 'March'}

Using ``pop()`` function
-------------------------------
.. _set-pop:

.. function:: pop() 
    :noindex:

**We can also use the** ``pop()`` **method to remove the item. Generally, the** ``pop()`` **method will always remove the last item but the set is unordered, we can't determine which element will be popped from set.**

Consider the following example to remove the item from the set using pop() method.
::

    Months = set(["January","February", "March", "April", "May", "June"])    
    print("\nprinting the original set ... ")    
    print(Months)    
    print("\nRemoving some months from the set...");    
    Months.pop();    
    Months.pop();    
    print("\nPrinting the modified set...");    
    print(Months)    

.. container:: outputs

    | **OUTPUT :**
    | printing the original set ... 
    | {'June', 'January', 'May', 'April', 'February', 'March'}
    | 
    | Removing some months from the set...
    |
    | Printing the modified set...
    | {'May', 'April', 'February', 'March'}

In the above code, the last element of the Month set is March but the pop() method removed the June and January because the set is unordered and the pop() method could not determine the last element of the set.

Python provides the clear() method to remove all the items from the set.

Using ``clear()`` function
-----------------------------------
.. _set-clear:

.. function:: clear() 
    :noindex:

Consider the following example.
::

    Months = set(["January","February", "March", "April", "May", "June"])    
    print("\nprinting the original set ... ")    
    print(Months)    
    print("\nRemoving all the items from the set...");    
    Months.clear()    
    print("\nPrinting the modified set...")    
    print(Months)    

.. container:: outputs

    | **OUTPUT :**
    | printing the original set ... 
    | {'January', 'May', 'June', 'April', 'March', 'February'}
    |
    | Removing all the items from the set...
    |
    | Printing the modified set...


Difference between ``discard()`` and ``remove()``
------------------------------------------------------

Despite the fact that discard() and remove() method both perform the same task, There is one main difference between discard() and remove().

If the key to be deleted from the set using discard() doesn't exist in the set, the Python will not give the error. The program maintains its control flow.

On the other hand, if the item to be deleted from the set using remove() doesn't exist in the set, the Python will raise an error.

Consider the following example.
::

    Months = set(["January","February", "March", "April", "May", "June"])    
    print("\nprinting the original set ... ")    
    print(Months)    
    print("\nRemoving items through discard() method...");    
    Months.discard("Feb");   
    print("\nprinting the modified set...")    
    print(Months)    
    print("\nRemoving items through remove() method...");    
    Months.remove("Jan")   
    print("\nPrinting the modified set...")    
    print(Months)    

.. container:: outputs

    | **OUTPUT :**

    | printing the original set ... 
    | {'March', 'January', 'April', 'June', 'February', 'May'}

    | Removing items through discard() method...

    | printing the modified set...
    | {'March', 'January', 'April', 'June', 'February', 'May'}

    | Removing items through remove() method...
    | Traceback (most recent call last):
    | File "set.py", line 9, in 
    | Months.remove("Jan")
    | KeyError: 'Jan'

.. _Python-Set-Operations:

Python Set Operations
=======================

Set can be performed mathematical operation such as ``union``, ``intersection``, ``difference``, and ``symmetric difference``. Python provides the facility to carry out these operations with operators or methods. We describe these operations as follows.


Union of two Sets
------------------
.. function:: union() 

The union of two sets is calculated by using the ``pipe (|)`` operator. The union of the two sets contains all the items that are present in both the sets.

Consider the following example to calculate the union of two sets.

using union ``|`` operator
+++++++++++++++++++++++++++++++

::

    Days1 = {"Monday","Tuesday","Wednesday","Thursday", "Sunday"}    
    Days2 = {"Friday","Saturday","Sunday"}    
    print(Days1|Days2)   

.. container:: outputs

    | **OUTPUT :**
    | {'Friday', 'Sunday', 'Saturday', 'Tuesday', 'Wednesday', 'Monday', 'Thursday'}

Python also provides the ``union()`` method which can also be used to calculate the union of two sets. Consider the following example.

using ``union()`` method
++++++++++++++++++++++++++++

::

    Days1 = {"Monday","Tuesday","Wednesday","Thursday"}    
    Days2 = {"Friday","Saturday","Sunday"}    
    print(Days1.union(Days2))   

.. container:: outputs

    | **OUTPUT :**
    | {'Friday', 'Monday', 'Tuesday', 'Thursday', 'Wednesday', 'Sunday', 'Saturday'}


Intersection of two sets
--------------------------
.. function:: intersection() 

The intersection of two sets can be performed by the and & operator or the ``intersection()`` function. The intersection of the two sets is given as the set of the elements that common in both sets.

Using ``&`` operator
+++++++++++++++++++++

::

    Days1 = {"Monday","Tuesday", "Wednesday", "Thursday"}    
    Days2 = {"Monday","Tuesday","Sunday", "Friday"}    
    print(Days1&Days2)   

.. container:: outputs

    | **OUTPUT :**
    | {'Monday', 'Tuesday'}

Using ``intersection()`` method
+++++++++++++++++++++++++++++++++


::

    set1 = {"Devansh","John", "David", "Martin"}    
    set2 = {"Steve", "Milan", "David", "Martin"}    
    print(set1.intersection(set2))   

.. container:: outputs

    | **OUTPUT :**
    | {'Martin', 'David'}

::

    set1 = {1,2,3,4,5,6,7}  
    set2 = {1,2,20,32,5,9}  
    set3 = set1.intersection(set2)  
    print(set3)  

.. container:: outputs

    | **OUTPUT :**
    | {1,2,5}

The ``intersection_update()`` method
+++++++++++++++++++++++++++++++++++++++++++
.. function:: intersection_update()

The ``intersection_update()`` method removes the items from the original set that are not present in both the sets (all the sets if more than one are specified).

The ``intersection_update()`` method is different from the intersection() method since it modifies the original set by removing the unwanted items, on the other hand, the intersection() method returns a new set.

Consider the following example.
::

    a = {"Devansh", "bob", "castle"}    
    b = {"castle", "dude", "emyway"}    
    c = {"fuson", "gaurav", "castle"}    
        
    a.intersection_update(b, c)    
        
    print(a)    

.. container:: outputs

    | **OUTPUT :**
    | {'castle'}

Difference between the two sets
---------------------------------

The difference of two sets can be calculated by using the ``subtraction (-)`` operator or intersection() method. Suppose there are two sets A and B, and the difference is A-B that denotes the resulting set will be obtained that element of A, which is not present in the set B.
Python Set

Using subtraction (``-``) operator
+++++++++++++++++++++++++++++++++++++++

::

    Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
    Days2 = {"Monday", "Tuesday", "Sunday"}    
    print(Days1-Days2)   

.. container:: outputs

    | **OUTPUT :**
    | {'Thursday', 'Wednesday'}

Using ``difference()`` method
+++++++++++++++++++++++++++++++++
.. function:: difference() 

::

    Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
    Days2 = {"Monday", "Tuesday", "Sunday"}    
    print(Days1.difference(Days2))   

.. container:: outputs

    | **OUTPUT :**
    | {'Thursday', 'Wednesday'}



Symmetric Difference of two sets
---------------------------------
.. function:: symmetric_difference() 

The symmetric difference of two sets is calculated by ^ operator or symmetric_difference() method. Symmetric difference of sets, it removes that element which is present in both sets. Consider the following example:
Python Set

Using ``^`` operator
++++++++++++++++++++++++

::

    a = {1,2,3,4,5,6}  
    b = {1,2,9,8,10}  
    c = a^b  
    print(c)  

.. container:: outputs

    | **OUTPUT :**
    | {3, 4, 5, 6, 8, 9, 10}

Using ``symmetric_difference()`` method
+++++++++++++++++++++++++++++++++++++++++++

::

    a = {1,2,3,4,5,6}  
    b = {1,2,9,8,10}  
    c = a.symmetric_difference(b)  
    print(c)  

.. container:: outputs

    | **OUTPUT :**
    | {3, 4, 5, 6, 8, 9, 10}

Set comparisons
-----------------

Python allows us to use the comparison operators i.e., <, >, <=, >= , == with the sets by using which we can check whether a set is a subset, superset, or equivalent to other set. The boolean true or false is returned depending upon the items present inside the sets.

Consider the following example.
::

    Days1 = {"Monday",  "Tuesday", "Wednesday", "Thursday"}    
    Days2 = {"Monday", "Tuesday"}    
    Days3 = {"Monday", "Tuesday", "Friday"}    
        
      
    print (Days1>Days2)     
        
      
    print (Days1<Days2)    
        
      
    print (Days2 == Days3)    

.. container:: outputs

    | **OUTPUT :**
    | True
    | False
    | False

FrozenSets
=============

The frozen sets are the immutable form of the normal sets, i.e., the items of the frozen set cannot be changed and therefore it can be used as a key in the dictionary.

The elements of the frozen set cannot be changed after the creation. We cannot change or append the content of the frozen sets by using the methods like``add()`` or ``remove()``.

The ``frozenset()`` method is used to create the frozenset object. The iterable sequence is passed into this method which is converted into the frozen set as a return type of the method.

Consider the following example to create the frozen set.
::

    Frozenset = frozenset([1,2,3,4,5])     
    print(type(Frozenset))    
    print("\nprinting the content of frozen set...")    
    for i in Frozenset:    
        print(i);    
    Frozenset.add(6)   

.. container:: outputs

    | **OUTPUT :**
    | <class 'frozenset'>
    | printing the content of frozen set...
    | 1
    | 2
    | 3
    | 4
    | 5
    | Traceback (most recent call last):
    | File "set.py", line 6, in <module>
    | Frozenset.add(6) #gives an error since we can change the content of Frozenset after creation 
    | AttributeError: 'frozenset' object has no attribute 'add'

Frozenset for the dictionary
-------------------------------

If we pass the dictionary as the sequence inside the ``frozenset()`` method, it will take only the keys from the dictionary and returns a frozenset that contains the key of the dictionary as its elements.

Consider the following example.
::

    Dictionary = {"Name":"John", "Country":"USA", "ID":101}     
    print(type(Dictionary))    
    Frozenset = frozenset(Dictionary);   
    print(type(Frozenset))    
    for i in Frozenset:     
        print(i)    

.. container:: outputs

    | **OUTPUT :**
    | <class 'dict'>
    | <class 'frozenset'>
    | Name
    | Country
    | ID


.. _Set-Programming-Example:

Set Programming Example
=========================

**Example - 1: Write a program to remove the given number from the set.**
::

    my_set = {1,2,3,4,5,6,12,24}  
    n = int(input("Enter the number you want to remove"))  
    my_set.discard(n)  
    print("After Removing:",my_set)  

.. container:: outputs

    | **OUTPUT :**
    | Enter the number you want to remove:12
    | After Removing: {1, 2, 3, 4, 5, 6, 24}

**Example - 2: Write a program to add multiple elements to the set.**
::

    set1 = set([1,2,4,"John","CS"])  
    set1.update(["Apple","Mango","Grapes"])  
    print(set1)  

.. container:: outputs

    | **OUTPUT :**
    | {1, 2, 4, 'Apple', 'John', 'CS', 'Mango', 'Grapes'}

**Example - 3: Write a program to find the union between two set.**
::

    set1 = set(["Peter","Joseph", 65,59,96])  
    set2  = set(["Peter",1,2,"Joseph"])  
    set3 = set1.union(set2)  
    print(set3)  

.. container:: outputs

    | **OUTPUT :**
    | {96, 65, 2, 'Joseph', 1, 'Peter', 59}

**Example- 4: Write a program to find the intersection between two sets.**
::

    set1 = {23,44,56,67,90,45,"Javatpoint"}  
    set2 = {13,23,56,76,"Sachin"}  
    set3 = set1.intersection(set2)  
    print(set3)  

.. container:: outputs

    | **OUTPUT :** 
    | {56, 23}

**Example - 5: Write the program to add element to the frozenset.**
::

    set1 = {23,44,56,67,90,45,"Javatpoint"}  
    set2 = {13,23,56,76,"Sachin"}  
    set3 = set1.intersection(set2)  
    print(set3)  

.. container:: outputs

    | **OUTPUT :**
    | TypeError: 'frozenset' object does not support item assignment

Above code raised an error because frozensets are immutable and can't be changed after creation.

**Example - 6: Write the program to find the issuperset, issubset and superset.**
::

    set1 = set(["Peter","James","Camroon","Ricky","Donald"])  
    set2 = set(["Camroon","Washington","Peter"])  
    set3 = set(["Peter"])  
      
    issubset = set1 >= set2  
    print(issubset)  
    issuperset = set1 <= set2  
    print(issuperset)  
    issubset = set3 <= set2  
    print(issubset)  
    issuperset = set2 >= set3  
    print(issuperset)  

.. container:: outputs

    | **OUTPUT :**
    | False
    | False
    | True
    | True

.. _set-copy:

.. function:: copy() 
    :noindex:

::

    numbers = {1, 2, 3, 4}
    new_numbers = numbers.copy()

    new_numbers.add(5)

    print('numbers: ', numbers)
    print('new_numbers: ', new_numbers)

.. container:: outputs

    | **OUTPUT :**
    | numbers:  {1, 2, 3, 4}
    | new_numbers:  {1, 2, 3, 4, 5}

.. function:: difference_update() 

::

    A = {'a', 'c', 'g', 'd'}
    B = {'c', 'f', 'g'}

    result = A.difference_update(B)

    print('A = ', A)
    print('B = ', B)
    print('result = ', result)

.. container:: outputs

    | **OUTPUT :**
    | A =  {'d', 'a'}
    | B =  {'c', 'g', 'f'}
    | result =  None


.. function:: isdisjoint() 

**The isdisjoint() method returns**

* True if two sets are disjoint sets (if ``set_a`` and ``set_b`` are disjoint sets in above syntax)
* False if two sets are not disjoint sets

::

    A = {1, 2, 3, 4}
    B = {5, 6, 7}
    C = {4, 5, 6}

    print('Are A and B disjoint?', A.isdisjoint(B))
    print('Are A and C disjoint?', A.isdisjoint(C))

.. container:: outputs

    | **OUTPUT :**
    | Are A and B disjoint? True
    | Are A and C disjoint? False

.. _set-issubset:

.. function:: issubset() 
    :noindex:

**Return Value from issubset()**

The issubset() returns

* True if A is a subset of B
* False if A is not a subset of B

::

    A = {1, 2, 3}
    B = {1, 2, 3, 4, 5}
    C = {1, 2, 4, 5}

    print(A.issubset(B))
    print(B.issubset(A))
    print(A.issubset(C))
    print(C.issubset(B))

.. container:: outputs

    | **OUTPUT :**
    | True
    | False
    | False
    | True

.. function:: issubset() 

**Return Value from issuperset()**

The issuperset() returns

* True if A is a superset of B
* False if A is not a superset of B

::

    A = {1, 2, 3, 4, 5}
    B = {1, 2, 3}
    C = {1, 2, 3}

    print(A.issuperset(B))
    print(B.issuperset(A))
    print(C.issuperset(B))

.. container:: outputs

    | **OUTPUT :**
    | True
    | False
    | True

.. _Python-Built-in-set-methods:

Python Built-in set methods
============================

.. csv-table::
   :header: Method,Description
   :widths: 30, 70
   :file: csv/set.csv
   :align: center 

.. |set-pop| replace:: ``pop()``
.. |set-clear| replace:: ``clear()``
.. |set-copy| replace:: ``copy()``
.. |set-add| replace:: ``add()``
.. |set-remove| replace:: ``remove()``
.. |set-issubset| replace:: ``issubset()``
.. |set-update| replace:: ``update()``