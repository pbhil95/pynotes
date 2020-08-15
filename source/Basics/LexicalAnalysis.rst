==========================
Lexical Analysis Python
==========================

.. index::
    single: tokens;identifiers
    single: tokens;literals
    single: tokens;punctuators
    single: tokens;separators

.. _tokens:

Tokens
=======

A token is the smallest element of a Python program that is meaningful to the compiler.
    
The Python parser recognizes these kinds of tokens: 
   
* :ref:`identifiers`
* :ref:`keywords <keywords>`
* :ref:`literals`
* :ref:`operators`
* :ref:`punctuators`

    
Tokens are usually separated by white space.

.. _identifiers:

identifiers
------------

An **identifier or variable** is anything that the user gives a name to. For example method names, variable names, dictionary names, class names, etc are all identifiers.

**In Python,** :keyword:`keywords` **are reserved identifiers which cannot be used as names for the variables in a program.**

Creating variables and assigning values
+++++++++++++++++++++++++++++++++++++++++++

To create a variable in Python, all you need to do is specify the variable name, and then assign a value to it.

**<variable name> = <value>**

Variable assignment works from left to right. So the following will give you an syntax error :

.. code-block:: python
    :caption: Python

    0 = x
    => Output: SyntaxError: can't assign to literal

.. tip:: You can not use python's :keyword:`keywords` as a valid variable name. You can see the list of keyword by:

    .. code-block:: python
        :caption: Python

        import keyword
        print(keyword.kwlist)

.. _rules-for-variables-naming:

Rules for variable naming
++++++++++++++++++++++++++++++++

**1. Variables names must start with a letter or an underscore.**

.. code-block::
    :caption: Python

    # valid
    x  = True 
    _y = True

    # starts with numeral
    9x = False
    => SyntaxError: invalid syntax

    # starts with symbol
    $y = False
    => SyntaxError: invalid syntax

**2. The remainder of your variable name may consist of letters, numbers and underscores.**

.. code-block:: python
    :caption: Python

    has_0_in_it = "Still Valid"

**3. Names are case sensitive.**

.. code-block:: python
    :caption: Python
    
    x = 9
    y = X*5
    =>NameError: name 'X' is not defined

.. _literals:

Literals
--------

Literal is the value assigned to a variable :
::

    # 20 is the Integer literal here 
    int a=20 
    
Literals categories :

* Integer literals

* String literals

* Boolean literals

* Character literals

* Float literals

* Null literals 

.. _punctuators:

punctuators
------------

Used to implement the grammatical and structure of a Syntax.Following
are the python punctuators:
::

    ( ) { } [ ] ; , . \ # @ : = ‘ “
