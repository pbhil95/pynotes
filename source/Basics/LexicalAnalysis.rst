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
* :ref:`keywords`
* :ref:`literals`
* :ref:`operators`
* :ref:`punctuators`

    
Tokens are usually separated by white space.

.. _identifiers:

identifiers
------------

An identifier or variable is anything that the user gives a name to. For example method names, variable names, dictionary names, class names, etc are all identifiers.

**In Python,** :keyword:`keywords` **are reserved identifiers which cannot be used as names for the variables in a program.**

.. seealso::

    for valid identifiers check rules here.. :ref:`rules-for-variables-naming`

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
