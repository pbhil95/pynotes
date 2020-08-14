==================
Python Data Types
==================

Built-in Data Types
======================

In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

.. csv-table::
   :header: Type,Example
   :widths: 30, 70
   :file: csv/data_types.csv
   :align: center 

.. note::

    **None** is special data type with a single value. It is used to signify the absence of value/false in a
    situation. It is represented by ``None``.

Getting the Data Type
========================

You can get the data type of any object by using the ``type()`` function:

Print the data type of the variable x:
::

    x = 5
    print(type(x))

.. container:: outputs

    | **OUTPUT :**
    | <class 'int'> 

Setting the Data Type
==========================

In Python, the data type is set when you assign a value to a variable:

.. csv-table::
   :header: Example,Data Type
   :widths: 80, 20
   :file: csv/DataTypesExample.csv
   :align: center 