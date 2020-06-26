====================
Variable assignment
====================

Creating variables and assigning values
========================================

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

Rules for variable naming:
===========================

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