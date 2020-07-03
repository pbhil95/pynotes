==================
Type Conversion
==================

Type Conversion in Python
===========================

Python defines type conversion functions to directly convert one data type to another which is useful in day to day and competitive programming. 

* :func:`int(a,base)` : This function converts any data type to integer. ‘Base’ specifies the base in which string is if data type is string.

* :func:`float()` : This function is used to convert any data type to a floating point number

::

    s = "10010"

    c = int(s,2) 

    print ("After converting to integer base 2 : ", end="") 

    print (c) 

    e = float(s) 

    print ("After converting to float : ", end="") 

    print (e) 

.. container:: outputs

    | **OUTPUT :**
    | After converting to integer base 2 : 18
    | After converting to float : 10010.0

* :func:`ord()` : This function is used to convert a character to integer.

* :func:`hex()` : This function is to convert integer to hexadecimal string.

* :func:`oct()` : This function is to convert integer to octal string.

::

    s = '4'

    c = ord(s) 

    print ("After converting character to integer : ",end="") 

    print (c) 

    c = hex(56) 

    print ("After converting 56 to hexadecimal string : ",end="") 

    print (c) 

    c = oct(56) 

    print ("After converting 56 to octal string : ",end="") 

    print (c) 

.. container:: outputs

    | **OUTPUT :**
    | After converting character to integer : 52
    | After converting 56 to hexadecimal string : 0x38
    | After converting 56 to octal string : 0o70

* :func:`tuple()` : This function is used to convert to a tuple.

* :func:`set()` : This function returns the type after converting to set.

* :ref:`list` () : This function is used to convert any data type to a list type.

::

    s = 'geeks'

    c = tuple(s) 

    print ("After converting string to tuple : ",end="") 

    print (c) 

    c = set(s) 

    print ("After converting string to set : ",end="") 

    print (c) 

    c = list(s) 

    print ("After converting string to list : ",end="") 

    print (c) 

.. container:: outputs

    | **OUTPUT :**
    | After converting string to tuple : ('g', 'e', 'e', 'k', 's')
    | After converting string to set : {'k', 'e', 's', 'g'}
    | After converting string to list : ['g', 'e', 'e', 'k', 's']

* :func:`dict()` : This function is used to convert a tuple of order (key,value) into a dictionary.

* :func:`str()` : Used to convert integer into a string.

* :func:`complex(real,imag)` : : This function converts real numbers to complex(real,imag) number.

::

    a = 1

    b = 2

    tup = (('a', 1) ,('f', 2), ('g', 3)) 

    c = complex(1,2) 

    print ("After converting integer to complex number : ",end="") 

    print (c) 

    c = str(a) 

    print ("After converting integer to string : ",end="") 

    print (c) 

    c = dict(tup) 

    print ("After converting tuple to dictionary : ",end="") 

    print (c) 

.. container:: outputs

    | **OUTPUT :**
    | After converting integer to complex number : (1+2j)
    | After converting integer to string : 1
    | After converting tuple to dictionary : {'a': 1, 'f': 2, 'g': 3}

* :func:`chr(number)` : : This function converts number to its corresponding ASCII character.

::

    a = chr(76) 

    b = chr(77) 

    print(a) 

    print(b) 

.. container:: outputs

    | **OUTPUT :**
    | L
    | M
