=====================
Python Dictionary
=====================

.. index:: ! Dictionary

Dictionary
===========

A dictionary is a collection which is unordered, changeable and indexed. In Python
dictionaries are written with curly brackets, and they have keys and values.
::

    #  Create and print a dictionary:
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    print(thisdict)

.. container:: outputs

    | **OUTPUT :**
    | {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

Dictionary Methods
--------------------

Python has a set of built-in methods that you can use on dictionaries.

.. csv-table::
   :header: Method,Description
   :widths: 30, 70
   :file: ../csv/dict_method.csv
   :align: center 

Accessing Items
-----------------

You can access the items of a dictionary by referring to its key name, inside square brackets:
::

    # Get the value of the "model" key:
    x = thisdict["model"]

.. function:: get()

There is also a method called get() that will give you the same result:
::

    # Get the value of the "model" key:
    x = thisdict.get("model")

Change Values
---------------

You can change the value of a specific item by referring to its key name:

::

    # Change the "year" to 2018:
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    thisdict["year"] = 2018


Loop Through a Dictionary
--------------------------

You can loop through a dictionary by using a for loop.
When looping through a dictionary, the return value are the keys of the dictionary, but there
are methods to return the values as well.

Print all key names in the dictionary, one by one:

::

    for x in thisdict:
    print(x)

.. container:: outputs

    | **OUTPUT :**
    | brand
    | model
    | year


Print all values in the dictionary, one by one:

::

    for x in thisdict:
    print(thisdict[x])

.. container:: outputs

    | **OUTPUT :**
    | Ford
    | Mustang
    | 1964


You can also use the values() method to return values of a dictionary:

.. function:: d_nm.values()

::

    for x in thisdict.values():
    print(x)


.. function:: items()

Loop through both keys and values, by using the items() method:

::

    for x, y in thisdict.items():
    print(x, y)

.. container:: outputs

    | **OUTPUT :**
    | brand Ford
    | model Mustang
    | year 1964


Check if Key Exists
---------------------

To determine if a specified key is present in a dictionary use the in keyword:

::

    # Check if "model" is present in the dictionary:
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

.. container:: outputs

    | **OUTPUT :**
    | Yes, 'model' is one of the keys in the thisdict dictionary


Dictionary Length
----------------------

.. function:: len()
   :noindex:

To determine how many items (key-value pairs) a dictionary has, use the len() function.
::

    Print the number of items in the dictionary:
    print(len(thisdict))

.. container:: outputs

    | **OUTPUT :**
    | 3

Adding Items
-------------

Adding an item to the dictionary is done by using a new index key and assigning a value to it:

::

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    thisdict["color"] = "red"
    print(thisdict)

.. container:: outputs

    | **OUTPUT :**
    | {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


Removing Items
------------------

There are several methods to remove items from a dictionary:

.. function:: pop()

The :func:`pop()` method removes the item with the specified key name:

::

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    thisdict.pop("model")
    print(thisdict)

.. container:: outputs

    | **OUTPUT :**
    | {'brand': 'Ford', 'year': 1964}


.. function:: popitem()

The :func:`popitem()` method removes the last inserted item (in versions before 3.7, a random item is removed instead):

::

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    thisdict.popitem()
    print(thisdict)

.. container:: outputs

    | **OUTPUT :**
    | {'brand': 'Ford', 'year': 1964}


The del keyword removes the item with the specified key name:

::

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    del thisdict["model"]
    print(thisdict)

.. container:: outputs

    | **OUTPUT :**
    | {'brand': 'Ford', 'year': 1964}


The :keyword:`del` keyword can also delete the dictionary completely:

::

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    del thisdict
    print(thisdict)

.. container:: outputs

    | **OUTPUT :**
    | This will cause an error because "thisdict" no longer exists.


.. function:: clear()

The :func:`clear()` method empties the dictionary:

::

    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    thisdict.clear()
    print(thisdict)

.. container:: outputs

    | **OUTPUT :**
    | {}

Copy a Dictionary
--------------------

You cannot copy a dictionary simply by typing ``dict2 = dict1`` , because: dict2 will only be
a reference to dict1 , and changes made in dict1 will automatically also be made in
dict2 .

.. function:: copy()

There are ways to make a copy, one way is to use the built-in Dictionary method :func:`copy()`.
::

    # Make a copy of a dictionary with the copy() method:
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
    }
    mydict = thisdict.copy()
    print(mydict)

.. container:: outputs

    | **OUTPUT :**
    | {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


Another way to make a copy is to use the built-in function dict() .
::

    # Make a copy of a dictionary with the dict() function:
    thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    6"year": 1964
    }
    mydict = dict(thisdict)
    print(mydict)


Nested Dictionaries
--------------------

A dictionary can also contain many dictionaries, this is called nested dictionaries.
::

    # Create a dictionary that contain three dictionaries:
    myfamily = {
    "child1" : {
    "name" : "Emil",
    "year" : 2004
    },
    "child2" : {
    "name" : "Tobias",
    "year" : 2007
    },
    "child3" : {
    "name" : "Linus",
    "year" : 2011
    }
    }

Or, if you want to nest three dictionaries that already exists as dictionaries:

Create three dictionaries, then create one dictionary that will contain the other three
::

    dictionaries:
    child1 = {
    "name" : "Emil",
    "year" : 2004
    }
    7child2 = {
    "name" : "Tobias",
    "year" : 2007
    }
    child3 = {
    "name" : "Linus",
    "year" : 2011
    }
    myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
    }

The dict() Constructor
-----------------------

It is also possible to use the dict() constructor to make a new dictionary:
::

    thisdict = dict(brand="Ford", model="Mustang", year=1964)
    # note that keywords are not string literals
    # note the use of equals rather than colon for the assignment
    print(thisdict)

.. container:: outputs

    | **OUTPUT :**
    | {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

.. function:: update()

In Python Dictionary, update() method updates the dictionary with the elements from the another dictionary object or from an iterable of key/value pairs.

Update with another Dictionary:
::

    # Dictionary with three items  
    Dictionary1 = { 'A': 'Geeks', 'B': 'For', } 
    Dictionary2 = { 'B': 'Geeks' } 
    
    # Dictionary before Updation 
    print("Original Dictionary:") 
    print(Dictionary1) 
    
    # update the value of key 'B' 
    Dictionary1.update(Dictionary2) 
    print("Dictionary after updation:") 
    print(Dictionary1)

.. container:: outputs

    | **OUTPUT :**
    | Original Dictionary:
    | {'A': 'Geeks', 'B': 'For'}

    | Dictionary after updation:
    | {'A': 'Geeks', 'B': 'Geeks'}

Update with an iterable:
::

    # Dictionary with single item  
    Dictionary1 = { 'A': 'Geeks'} 
    
    # Dictionary before Updation 
    print("Original Dictionary:") 
    print(Dictionary1) 
    
    # update the Dictionary with iterable 
    Dictionary1.update(B = 'For', C = 'Geeks') 
    print("Dictionary after updation:") 
    print(Dictionary1) 

.. container:: outputs

    | **OUTPUT :**
    | Original Dictionary:
    | {'A': 'Geeks'}
    | Dictionary after updation:
    | {'C': 'Geeks', 'B': 'For', 'A': 'Geeks'}

.. function:: setdefault()

Dictionary in Python is an unordered collection of data values, used to store data values like a map, which unlike other Data Types that hold only single value as an element, Dictionary holds key : value pair.
::

    # Dictionary with single item  
    Dictionary1 = { 'A': 'Geeks', 'B': 'For', 'C': 'Geeks'} 
    
    # using setdefault() method 
    Third_value = Dictionary1.setdefault('C') 
    print("Dictionary:", Dictionary1) 
    print("Third_value:", Third_value) 

.. container:: outputs

    | **OUTPUT :**
    | Dictionary: {'A': 'Geeks', 'C': 'Geeks', 'B': 'For'}
    | Third_value: Geeks

.. function:: keys()

keys() method in Python Dictionary, returns a view object that displays a list of all the keys in the dictionary.
::

    Dictionary1 = {'A': 'Geeks', 'B': 'For'} 

    # Printing keys of dictionary 
    print("Keys before Dictionary Updation:") 
    keys = Dictionary1.keys() 
    print(keys) 

    # adding an element to the dictionary 
    Dictionary1.update({'C':'Geeks'}) 

    print('\nAfter dictionary is updated:') 
    print(keys) 

.. container:: outputs

    | **OUTPUT :**
    | Keys before Dictionary Updation:
    | dict_keys(['B', 'A'])
    |
    | After dictionary is updated:
    | dict_keys(['B', 'A', 'C'])

.. function:: has_key()

In Python Dictionary, has_key() method returns true if specified key is present in the dictionary, else returns false.
::

    Dictionary1 = { 'A': 'Geeks', 'B': 'For', 'C': 'Geeks' } 
    print("Dictionary to be checked: ") 
    print(Dictionary1) 

    print(Dictionary1.has_key('A')) 
    print(Dictionary1.has_key('For'))

.. container:: outputs

    | **OUTPUT :**
    | Dictionary to be checked: 
    | {'A': 'Geeks', 'C': 'Geeks', 'B': 'For'}
    | True
    | False

.. function:: fromkeys()

Generate a dictionary from the given keys.
::

    seq = { 'a', 'b', 'c', 'd', 'e' } 
    lis1 = [ 2, 3 ] 

    res_dict = dict.fromkeys(seq, lis1) 

    # Printing created dict 
    print ("The newly created dict with list values : "+ str(res_dict))

    # appending to lis1 
    lis1.append(4) 
      
    # Printing dict after appending 
    print ("The dict with list values after appending : "+ str(res_dict)) 

.. container:: outputs

    | **OUTPUT :**
    | The newly created dict with list values : {‘d’: [2, 3], ‘e’: [2, 3], ‘c’: [2, 3], ‘a’: [2, 3], ‘b’: [2, 3]}
    | The dict with list values after appending : {‘d’: [2, 3, 4], ‘e’: [2, 3, 4], ‘c’: [2, 3, 4], ‘a’: [2, 3, 4], ‘b’: [2, 3, 4]}

.. function:: cmp()

Python dictionary method cmp() compares two dictionaries based on key and values.

**This method returns 0 if both dictionaries are equal, -1 if dict1 < dict2 and 1 if dict1 > dic2**
::

    dict1 = {'Name': 'Zara', 'Age': 7};
    dict2 = {'Name': 'Mahnaz', 'Age': 27};
    dict3 = {'Name': 'Abid', 'Age': 27};
    dict4 = {'Name': 'Zara', 'Age': 7};
    print "Return Value : %d" %  cmp (dict1, dict2)
    print "Return Value : %d" %  cmp (dict2, dict3)
    print "Return Value : %d" %  cmp (dict1, dict4)

.. container:: outputs

    | **OUTPUT :**
    | Return Value : -1
    | Return Value : 1
    | Return Value : 0


