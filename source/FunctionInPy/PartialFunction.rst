=============================
Partial Functions in Python
=============================

Introduction
===================

Partial functions allow us to fix a certain number of arguments of a function and generate a new function.

Example:
---------------
::

    from functools import partial 

    def f(a, b, c, x): 

        return 1000*a + 100*b + 10*c + x 

    g = partial(f, 3, 1, 4) 

    print(g(5)) 

.. container:: outputs

    | **OUTPUT :**
    | 3145

In the example we have pre-filled our function with some constant values of ``a, b and c. And g()`` just takes a single argument i.e. the variable x.

Another Example :
-----------------------

::

    from functools import *

    def add(a, b, c): 

        return 100 * a + 10 * b + c 

    add_part = partial(add, c = 2, b = 1) 

    print(add_part(3)) 

.. container:: outputs

    | **OUTPUT :**
    | 312

**Partial functions can be used to derive specialized functions from general functions and therefore help us to reuse our code.**