====================
String Formatting
====================

Learning Objectives:
====================

At the end of this chapter the students will be able to understand:

* :ref:`1-formatting-using-percentage-symbol`
* :ref:`2-str.format()`
* :ref:`3-f-Strings`
* :ref:`Speed-comparison`
* :ref:`Formatting-Types`

.. _1-formatting-using-percentage-symbol:

1. Formatting using percentage symbol
=====================================
.. code-block:: python
    :caption: Python

    >>> name = "Eric"
    >>> age = 74
    >>> "Hello, %s. You are %s." % (name, age)
    'Hello Eric. You are 74.'

.. _2-str.format():

2. str.format()
=================

With str.format(), the replacement fields are marked by curly braces:

.. code-block:: python
    :caption: Python

    >>> "Hello, {}. You are {}.".format(name, age)
    'Hello, Eric. You are 74.'

You can reference variables in any order by referencing their index:

.. code-block:: python
    :caption: Python

    >>>"Hello, {1}. You are {0}.".format(age, name)
    'Hello, Eric. You are 74.'

But if you insert the variable names, you get the added perk of being able to pass objects and then reference parameters and methods in between the braces:

.. code-block:: python
    :caption: Python

    >>> person = {'name': 'Eric', 'age': 74}
    >>> "Hello, {name}. You are {age}.".format(name=person['name'], age=person['age'])
    'Hello, Eric. You are 74.'

You can also use \** to do this neat trick with dictionaries:

.. code-block::  python
    :caption: Python

    >>> person = {'name': 'Eric', 'age': 74}
    >>> "Hello, {name}. You are {age}.".format(**person)
    'Hello, Eric. You are 74

.. _3-f-Strings:

3. f-Strings
=============

The syntax is similar to the one you used with str.format() but less verbose. Look at how easily readable this is:

.. code-block:: python
    :caption: Python

    >>> name = "Eric"
    >>> age = 74
    >>> f"Hello, {name}. You are {age}."
    'Hello, Eric. You are 74.'

It would also be valid to use a capital letter F:

.. code-block:: python
    :caption: Python

    >>> F"Hello, {name}. You are {age}."
    'Hello, Eric. You are 74.'

You could also call functions. Here’s an example:

.. code-block:: python
    :caption: Python

    >>> def to_lowercase(input):
    ...     return input.lower()
    >>> name = "Eric Idle"
    >>> f"{to_lowercase(name)} is funny."
    'eric idle is funny.'

Multiline f-Strings
--------------------

You can have multiline strings:

.. code-block:: python
    :caption: Python

    >>> name = "Eric"
    >>> profession = "comedian"
    >>> affiliation = "Monty Python"
    >>> message = (
    ...     f"Hi {name}. "
    ...     f"You are a {profession}. "
    ...     f"You were in {affiliation}."
    ... )
    >>> message
    'Hi Eric. You are a comedian. You were in Monty Python.'

.. _Speed-comparison:

Speed comparison
=================

**The f in f-strings may as well stand for “fast.”**

| f-strings are faster than both %-formatting and str.format(). As you already saw, f-strings are expressions evaluated at runtime rather than constant values.

| Here’s a speed comparison:

.. code-block:: python
    :caption: Python

    >>> import timeit
    >>> timeit.timeit("""name = "Eric"
    ... age = 74
    ... '%s is %s.' % (name, age)""", number = 10000)
    0.003324444866599663

.. code-block:: python
    :caption: Python

    >>> timeit.timeit("""name = "Eric"
    ... age = 74
    ... '{} is {}.'.format(name, age)""", number = 10000)
    0.004242089427570761

.. code-block:: python
    :caption: Python

    >>> timeit.timeit("""name = "Eric"
    ... age = 74
    ... f'{name} is {age}.'""", number = 10000)
    0.0024820892040722242


f'string with Dictionaries
===========================

If you are going to use single quotation marks for the keys of the dictionary, then remember to make sure you’re using double quotation marks for the f-strings containing the keys.

| This will work:

.. code-block:: python
    :caption: Python

    >>> comedian = {'name': 'Eric Idle', 'age': 74}
    >>> f"The comedian is {comedian['name']}, aged {comedian['age']}."
    The comedian is Eric Idle, aged 74.


.. _Formatting-Types:

Formatting Types
====================

.. csv-table::
   :header: Type,Description
   :widths: 20, 80
   :file: csv/formmatingtypes.csv
   :align: center 

.. _`:<`:

:<
---

>>> txt = "We have {:<8} chickens."
>>> print(txt.format(49))

Output:

>>> We have 49       chickens.

.. _`:+`:

:+
---

>>> txt = "The temperature is between {:+} and {:+} degrees celsius."

>>> print(txt.format(-3, 7))

Output:

>>> The temperature is between -3 and +7 degrees celsius.

.. _`:o`:

:o
---

>>> txt = "The octal version of {0} is {0:o}"

>>> print(txt.format(10))

Output:

>>> The octal version of 10 is 12 

.. _`:f`:

:f
---

>>> txt = "The price is {:.2f} dollars."
>>> print(txt.format(45))

Output:

>>> The price is 45.00 dollars.

