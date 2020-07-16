==================
Built-in Functions
==================

The Python interpreter has a number of functions and types built into it that
are always available.  They are listed here in alphabetical order.

Functions
============

.. csv-table::
   :widths: 50, 50
   :file: csv/inbuiltFunctions.csv
   :align: center 

.. |func-dict| replace:: ``dict()``
.. |func-frozenset| replace:: ``frozenset()``
.. |func-memoryview| replace:: ``memoryview()``
.. |func-set| replace:: ``set()``
.. |func-list| replace:: ``list()``
.. |func-str| replace:: ``str()``
.. |func-tuple| replace:: ``tuple()``
.. |func-range| replace:: ``range()``
.. |func-bytearray| replace:: ``bytearray()``
.. |func-bytes| replace:: ``bytes()``

.. function:: abs(x)

Return the absolute value of a number.

.. code-block:: python
   :caption: Python

   integer = -20
   print('Absolute value of -20 is:', abs(integer))
   floating = -30.33
   print('Absolute value of -30.33 is:', abs(floating))
   complex = (3 - 4j)
   print('Magnitude of 3 - 4j is:', abs(complex))

   Output:
   Absolute value of -20 is: 20
   Absolute value of -30.33 is: 30.33
   Magnitude of 3 - 4j is: 5.0

.. function:: all(iterable)

Return ``True`` if all elements of the *iterable* are true (or if the iterable is empty).


.. function:: any(iterable)

Return ``True`` if any element of the *iterable* is true.  If the iterable
is empty, return ``False``.

.. function:: ascii(object)

As :func:`repr`, return a string containing a printable representation of an
object, but escape the non-ASCII characters in the string returned by
:func:`repr` using ``\x``, ``\u`` or ``\U`` escapes. 

.. code-block:: python
   :caption: Python

   normalText = 'Python is interesting'
   print(ascii(normalText))

   otherText = 'Pythön is interesting'
   print(ascii(otherText))

   print('Pyth\xf6n is interesting')

   Output:
   Python is interesting
   Pyth\xf6n is interesting
   Pythön is interesting

.. function:: bin(x)

Convert an integer number to a binary string prefixed with "0b". The result
is a valid Python expression. If *x* is not a Python :class:`int` object, it
has to define an :meth:`__index__` method that returns an integer. Some
examples:

>>> bin(3)
'0b11'
>>> bin(-10)
'-0b1010'

If prefix "0b" is desired or not, you can use either of the following ways.

>>> format(14, '#b'), format(14, 'b')
('0b1110', '1110')
>>> f'{14:#b}', f'{14:b}'
('0b1110', '1110')

See also :func:`format` for more information.


.. class:: bool([x])

Return a Boolean value, i.e. one of ``True`` or ``False``.

.. function:: breakpoint(*args, **kws)

This function drops you into the debugger at the call site.

.. code-block:: python
   :caption: Python

   def debugger(a, b): 
      breakpoint() 
      result = a / b 
      return result 

   print(debugger(5, 0)) 

   Output:
   -> result = a / b
   (Pdb) c

   Traceback (most recent call last):
   File "c:\Users\t.py", line 7, in <module>
   print(debugger(5, 0))
   File "c:\Users\t.py", line 3, in debugger
   result = a / b
   ZeroDivisionError: division by zero

.. note:: Commands for debugging :

   * c -> continue execution
   * q -> quit the debugger/execution
   * n -> step to next line within the same function
   * s -> step to next line in this function or a called function




.. _func-bytearray:
.. class:: bytearray
   :noindex:

Return a new array of bytes.  The :class:`bytearray` class is a mutable
sequence of integers in the range 0 <= x < 256.

.. _func-bytes:
.. class:: bytes
   :noindex:

Return a new "bytes" object, which is an immutable sequence of integers in
the range ``0 <= x < 256``.  

.. function:: callable(object)

Return :const:`True` if the *object* argument appears callable,
:const:`False` if not.  If this returns ``True``, it is still possible that a
call fails, but if it is ``False``, calling *object* will never succeed.
Note that classes are callable (calling a class returns a new instance);
instances are callable if their class has a :meth:`__call__` method.

.. function:: chr(i)

Return the string representing a character whose Unicode code point is the
integer *i*.  For example, ``chr(97)`` returns the string ``'a'``, while
``chr(8364)`` returns the string ``'€'``. This is the inverse of :func:`ord`.

The valid range for the argument is from 0 through 1,114,111 (0x10FFFF in
base 16).  :exc:`ValueError` will be raised if *i* is outside that range.


.. decorator:: classmethod

Transform a method into a class method.

A class method receives the class as implicit first argument, just like an
instance method receives the instance. To declare a class method, use this
idiom::

   class C:
   @classmethod
   def f(cls, arg1, arg2, ...): ...

.. seealso:: To learn more about static ,class and instance methods see :doc:`../ObjectOrientedProgramming/Static_Instance_ClassMethods`

.. function:: compile(source, filename, mode, flags=0, dont_inherit=False, optimize=-1)

Compile the *source* into a code or AST object.  Code objects can be executed
by :func:`exec` or :func:`eval`.  *source* can either be a normal string, a
byte string, or an AST object.  Refer to the :mod:`ast` module documentation
for information on how to work with AST objects.

.. code-block:: python
   :caption: Python

   srcCode = 'x = 10\ny = 20\nmul = x * y\nprint("mul =", mul)'
   execCode = compile(srcCode, 'mulstring', 'exec') 
   exec(execCode) 

   Output:
   mul = 200

.. important::

   1. If the Python code is in string form or is an AST object, and you want to change it to a code object, then you can use compile() method.
   2. The code object returned by the compile() method can later be called using methods like: exec() and eval() which will execute dynamically generated Python code.


.. note::

   When compiling a string with multi-line code in ``'single'`` or
   ``'eval'`` mode, input must be terminated by at least one newline
   character.  This is to facilitate detection of incomplete and complete
   statements in the :mod:`code` module.

.. warning::

   It is possible to crash the Python interpreter with a
   sufficiently large/complex string when compiling to an AST
   object due to stack depth limitations in Python's AST compiler.

.. class:: complex([real[, imag]])

Return a complex number with the value *real* + *imag*\*1j or convert a string
or number to a complex number.  If the first parameter is a string, it will
be interpreted as a complex number and the function must be called without a
second parameter.  The second parameter can never be a string. Each argument
may be any numeric type (including complex).  If *imag* is omitted, it
defaults to zero and the constructor serves as a numeric conversion like
:class:`int` and :class:`float`.  If both arguments are omitted, returns
``0j``.

.. note::

   When converting from a string, the string must not contain whitespace
   around the central ``+`` or ``-`` operator.  For example,
   ``complex('1+2j')`` is fine, but ``complex('1 + 2j')`` raises
   :exc:`ValueError`.

.. function:: delattr(object, name)

This is a relative of :func:`setattr`.  The arguments are an object and a
string.  The string must be the name of one of the object's attributes.  The
function deletes the named attribute, provided the object allows it.  For
example, ``delattr(x, 'foobar')`` is equivalent to ``del x.foobar``.


.. _func-dict:
.. class:: dict(**kwarg)

Python dictionary is an unordered collection of items. Each item of a dictionary has a key/value pair.
::

   my_dict = {'name': 'John', 1: [2, 4, 3]}

.. seealso::

   :doc:`../DataTypes/Dictionary`


 
.. function:: dir([object])

Without arguments, return the list of names in the current local scope.  With an
argument, attempt to return a list of valid attributes for that object.

The default :func:`dir` mechanism behaves differently with different types of
objects, as it attempts to produce the most relevant, rather than complete,
information:

* If the object is a module object, the list contains the names of the module's
  attributes.

* If the object is a type or class object, the list contains the names of its
  attributes, and recursively of the attributes of its bases.

* Otherwise, the list contains the object's attributes' names, the names of its
  class's attributes, and recursively of the attributes of its class's base
  classes.

The resulting list is sorted alphabetically.  For example:

   >>> import struct
   >>> dir()# show the names in the module namespace  # doctest: +SKIP
   ['__builtins__', '__name__', 'struct']
   >>> dir(struct)# show the names in the struct module # doctest: +SKIP
   ['Struct', '__all__', '__builtins__', '__cached__', '__doc__', '__file__',
   '__initializing__', '__loader__', '__name__', '__package__',
   '_clearcache', 'calcsize', 'error', 'pack', 'pack_into',
   'unpack', 'unpack_from']
   >>> class Shape:
   ...  def __dir__(self):
   ...return ['area', 'perimeter', 'location']
   >>> s = Shape()
   >>> dir(s)
   ['area', 'location', 'perimeter']

.. note::

   Because :func:`dir` is supplied primarily as a convenience for use at an
   interactive prompt, it tries to supply an interesting set of names more
   than it tries to supply a rigorously or consistently defined set of names,
   and its detailed behavior may change across releases.  For example,
   metaclass attributes are not in the result list when the argument is a
   class.


.. function:: divmod(a, b)

Take two (non complex) numbers as arguments and return a pair of numbers
consisting of their quotient and remainder when using integer division.
::

   >>> divmod(56, 9)
   (6, 2)


.. function:: enumerate(iterable, start=0)

Return an enumerate object. *iterable* must be a sequence, an
`iterator`, or some other object which supports iteration.

   >>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
   >>> list(enumerate(seasons))
   [(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
   >>> list(enumerate(seasons, start=1))
   [(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]

Equivalent to::

   def enumerate(sequence, start=0):
   n = start
   for elem in sequence:
   yield n, elem
   n += 1

.. note::
   A lot of times when dealing with iterators, we also get a need to keep a count of iterations. Python eases the programmers’ task by providing a built-in function enumerate() for this task.


.. function:: eval(expression[, globals[, locals]])

The return value is the result of
the evaluated expression. Syntax errors are reported as exceptions.  Example:

   >>> x = 1
   >>> eval('x+1')
   2

::

   from math import *
   print(eval('dir()'))

.. container:: outputs

   | **OUTPUT :**
   | ['__annotations__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'os', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
 
Restricting the Use of Available Methods and Variables in eval()
::

   from math import *
   names = {'square_root': sqrt, 'power': pow}
   print(eval('dir()', names))

   # Using square_root in Expression
   print(eval('square_root(9)', names))

.. container:: outputs

   | **OUTPUT :**  
   | ['__builtins__', 'power', 'square_root']
   | 3.0

.. function:: exec(object[, globals[, locals]])

This function supports dynamic execution of Python code. 


.. function:: filter(function, iterable)

Construct an iterator from those elements of *iterable* for which *function*
returns true.  *iterable* may be either a sequence, a container which
supports iteration, or an iterator. 


.. class:: float([x])

Return a floating point number constructed from a number or string *x*.

Examples::

   >>> float('+1.23')
   1.23
   >>> float('-12345\n')
   -12345.0
   >>> float('1e-003')
   0.001
   >>> float('+1E6')
   1000000.0
   >>> float('-Infinity')
   -inf

.. function:: format(value[, format_spec])

Convert a *value* to a "formatted" representation, as controlled by
*format_spec*.


.. _func-frozenset:
.. class:: frozenset([iterable])
   :noindex:

Return a new :class:`frozenset` object, optionally with elements taken from
*iterable*.  ``frozenset`` is a built-in class.  See :class:`frozenset` and
`types-set` for documentation about this class.

For other containers see the built-in :class:`set`, :class:`list`,
:class:`tuple`, and :class:`dict` classes, as well as the :mod:`collections`
module.


.. function:: getattr(object, name[, default])

Return the value of the named attribute of *object*.  *name* must be a string.
If the string is the name of one of the object's attributes, the result is the
value of that attribute.  For example, ``getattr(x, 'foobar')`` is equivalent to
``x.foobar``.  If the named attribute does not exist, *default* is returned if
provided, otherwise :exc:`AttributeError` is raised.


.. function:: globals()

Return a dictionary representing the current global symbol table. This is always
the dictionary of the current module (inside a function or method, this is the
module where it is defined, not the module from which it is called).


.. function:: hasattr(object, name)

The arguments are an object and a string.  The result is ``True`` if the
string is the name of one of the object's attributes, ``False`` if not. (This
is implemented by calling ``getattr(object, name)`` and seeing whether it
raises an :exc:`AttributeError` or not.)


.. function:: hash(object)

Return the hash value of the object (if it has one).  Hash values are
integers.  They are used to quickly compare dictionary keys during a
dictionary lookup.  Numeric values that compare equal have the same hash
value (even if they are of different types, as is the case for 1 and 1.0).

.. note::

   For objects with custom :meth:`__hash__` methods, note that :func:`hash`
   truncates the return value based on the bit width of the host machine.
   See :meth:`__hash__` for details.

.. function:: help([object])

Invoke the built-in help system.  (This function is intended for interactive
use.)  If no argument is given, the interactive help system starts on the
interpreter console.  If the argument is a string, then the string is looked up
as the name of a module, function, class, method, keyword, or documentation
topic, and a help page is printed on the console.  If the argument is any other
kind of object, a help page on the object is generated.


.. function:: hex(x)

Convert an integer number to a lowercase hexadecimal string prefixed with
"0x". If *x* is not a Python :class:`int` object, it has to define an
:meth:`__index__` method that returns an integer. Some examples:

   >>> hex(255)
   '0xff'
   >>> hex(-42)
   '-0x2a'

If you want to convert an integer number to an uppercase or lower hexadecimal
string with prefix or not, you can use either of the following ways:

  >>> '%#x' % 255, '%x' % 255, '%X' % 255
  ('0xff', 'ff', 'FF')
  >>> format(255, '#x'), format(255, 'x'), format(255, 'X')
  ('0xff', 'ff', 'FF')
  >>> f'{255:#x}', f'{255:x}', f'{255:X}'
  ('0xff', 'ff', 'FF')

See also :func:`format` for more information.

See also :func:`int` for converting a hexadecimal string to an
integer using a base of 16.

.. note::

   To obtain a hexadecimal string representation for a float, use the
   :meth:`float.hex` method.


.. function:: id(object)

Return the "identity" of an object.  This is an integer which
is guaranteed to be unique and constant for this object during its lifetime.
Two objects with non-overlapping lifetimes may have the same :func:`id`
value.

.. function:: input([prompt])

If the *prompt* argument is present, it is written to standard output without
a trailing newline.  The function then reads a line from input, converts it
to a string (stripping a trailing newline), and returns that.  When EOF is
read, :exc:`EOFError` is raised.  Example::

   >>> s = input('--> ')  # doctest: +SKIP
   --> Monty Python's Flying Circus
   >>> s  # doctest: +SKIP
   "Monty Python's Flying Circus"

.. seealso:: :ref:`Getting-Input-from-User-in-Python`

.. class:: int([x])
  int(x, base=10)

Return an integer object constructed from a number or string *x*, or return
``0`` if no arguments are given. 

.. function:: isinstance(object, classinfo)

Return ``True`` if the *object* argument is an instance of the *classinfo*
argument, or of a (direct, indirect or virtual <abstract base
class>) subclass thereof.  If *object* is not
an object of the given type, the function always returns ``False``.
If *classinfo* is a tuple of type objects (or recursively, other such
tuples), return `True` if *object* is an instance of any of the types.
If *classinfo* is not a type or tuple of types and such tuples,
a :exc:`TypeError` exception is raised.


.. function:: issubclass(class, classinfo)

Return ``True`` if *class* is a subclass (direct, indirect or virtual
<abstract base class>) of *classinfo*.  A
class is considered a subclass of itself. *classinfo* may be a tuple of class
objects, in which case every entry in *classinfo* will be checked. In any other
case, a :exc:`TypeError` exception is raised.


.. function:: iter(object[, sentinel])

Return an `iterator` object.  The first argument is interpreted very
differently depending on the presence of the second argument.

One useful application of the second form of :func:`iter` is to build a
block-reader. For example, reading fixed-width blocks from a binary
database file until the end of file is reached::

   from functools import partial
   with open('mydata.db', 'rb') as f:
   for block in iter(partial(f.read, 64), b''):
   process_block(block)


.. function:: len(s)

Return the length (the number of items) of an object.  The argument may be a
sequence (such as a string, bytes, tuple, list, or range) or a collection
(such as a dictionary, set, or frozen set).


.. _func-list:
.. class:: list([iterable])
   :noindex:

Rather than being a function, :class:`list` is actually a mutable
sequence type, as documented in `typesseq-list` and `typesseq`.

.. seealso:: :doc:`../DataTypes/List`

.. function:: locals()

Update and return a dictionary representing the current local symbol table.
Free variables are returned by :func:`locals` when it is called in function
blocks, but not in class blocks. Note that at the module level, :func:`locals`
and :func:`globals` are the same dictionary.

.. note::
   The contents of this dictionary should not be modified; changes may not
   affect the values of local and free variables used by the interpreter.

.. function:: map(function, iterable, ...)

Return an iterator that applies *function* to every item of *iterable*,
yielding the results.  If additional *iterable* arguments are passed,
*function* must take that many arguments and is applied to the items from all
iterables in parallel.  With multiple iterables, the iterator stops when the
shortest iterable is exhausted.  For cases where the function inputs are
already arranged into argument tuples, see :func:`itertools.starmap`\.


.. function:: max(iterable, *[, key, default])
  max(arg1, arg2, *args[, key])

Return the largest item in an iterable or the largest of two or more
arguments.

If one positional argument is provided, it should be an `iterable`.
The largest item in the iterable is returned.  If two or more positional
arguments are provided, the largest of the positional arguments is
returned.

.. _func-memoryview:
.. class:: memoryview(obj)
   :noindex:

Return a "memory view" object created from the given argument.  See
`typememoryview` for more information.


.. function:: min(iterable, *[, key, default])
  min(arg1, arg2, *args[, key])

Return the smallest item in an iterable or the smallest of two or more
arguments.

If one positional argument is provided, it should be an `iterable`.
The smallest item in the iterable is returned.  If two or more positional
arguments are provided, the smallest of the positional arguments is
returned.

.. function:: next(iterator[, default])

Retrieve the next item from the *iterator* by calling its
:meth:`~iterator.__next__` method.  If *default* is given, it is returned
if the iterator is exhausted, otherwise :exc:`StopIteration` is raised.


.. class:: object()

Return a new featureless object.  :class:`object` is a base for all classes.
It has the methods that are common to all instances of Python classes.  This
function does not accept any arguments.

.. note::

   :class:`object` does *not* have a :attr:`~object.__dict__`, so you can't
   assign arbitrary attributes to an instance of the :class:`object` class.


.. function:: oct(x)

Convert an integer number to an octal string prefixed with "0o".  The result
is a valid Python expression. If *x* is not a Python :class:`int` object, it
has to define an :meth:`__index__` method that returns an integer. For
example:

   >>> oct(8)
   '0o10'
   >>> oct(-56)
   '-0o70'

If you want to convert an integer number to octal string either with prefix
"0o" or not, you can use either of the following ways.

   >>> '%#o' % 10, '%o' % 10
   ('0o12', '12')
   >>> format(10, '#o'), format(10, 'o')
   ('0o12', '12')
   >>> f'{10:#o}', f'{10:o}'
   ('0o12', '12')

.. function:: open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

Open *file* and return a corresponding `file object`.  If the file
cannot be opened, an :exc:`OSError` is raised.

*file* is a `path-like object` giving the pathname (absolute or
relative to the current working directory) of the file to be opened or an
integer file descriptor of the file to be wrapped.  (If a file descriptor is
given, it is closed when the returned I/O object is closed, unless *closefd*
is set to ``False``.)

*mode* is an optional string that specifies the mode in which the file is
opened.  It defaults to ``'r'`` which means open for reading in text mode.
Other common values are ``'w'`` for writing (truncating the file if it
already exists), ``'x'`` for exclusive creation and ``'a'`` for appending
(which on *some* Unix systems, means that *all* writes append to the end of
the file regardless of the current seek position).  In text mode, if
*encoding* is not specified the encoding used is platform dependent:
``locale.getpreferredencoding(False)`` is called to get the current locale
encoding. (For reading and writing raw bytes use binary mode and leave
*encoding* unspecified.)  The available modes are:

.. _filemodes:

.. index::
   pair: file; modes

========= ===============================================================
Character Meaning
========= ===============================================================
``'r'``     open for reading (default)
``'w'``     open for writing, truncating the file first
``'x'``     open for exclusive creation, failing if the file already exists
``'a'``     open for writing, appending to the end of the file if it exists
``'b'``     binary mode
``'t'``     text mode (default)
``'+'``     open for updating (reading and writing)
========= ===============================================================

The default mode is ``'r'`` (open for reading text, synonym of ``'rt'``).
Modes ``'w+'`` and ``'w+b'`` open and truncate the file.  Modes ``'r+'``
and ``'r+b'`` open the file with no truncation.


.. function:: ord(c)

Given a string representing one Unicode character, return an integer
representing the Unicode code point of that character.  For example,
``ord('a')`` returns the integer ``97`` and ``ord('€')`` (Euro sign)
returns ``8364``.  This is the inverse of :func:`chr`.


.. function:: pow(base, exp[, mod])

Return *base* to the power *exp*; if *mod* is present, return *base* to the
power *exp*, modulo *mod* (computed more efficiently than
``pow(base, exp) % mod``). The two-argument form ``pow(base, exp)`` is
equivalent to using the power operator: ``base**exp``.

Here's an example of computing an inverse for ``38`` modulo ``97``::

   >>> pow(38, -1, mod=97)
   23
   >>> 23 * 38 % 97 == 1
   True

.. function:: print(*objects, sep=' ', end='\\n', file=sys.stdout, flush=False)

Print *objects* to the text stream *file*, separated by *sep* and followed
by *end*.  *sep*, *end*, *file* and *flush*, if present, must be given as keyword
arguments.

.. class:: property(fget=None, fset=None, fdel=None, doc=None)

Return a property attribute.

*fget* is a function for getting an attribute value.  *fset* is a function
for setting an attribute value. *fdel* is a function for deleting an attribute
value.  And *doc* creates a docstring for the attribute.

A typical use is to define a managed attribute ``x``::

   class C:
   def __init__(self):
   self._x = None

   def getx(self):
   return self._x

   def setx(self, value):
   self._x = value

   def delx(self):
   del self._x

   x = property(getx, setx, delx, "I'm the 'x' property.")

If *c* is an instance of *C*, ``c.x`` will invoke the getter,
``c.x = value`` will invoke the setter and ``del c.x`` the deleter.

If given, *doc* will be the docstring of the property attribute. Otherwise, the
property will copy *fget*'s docstring (if it exists).  This makes it possible to
create read-only properties easily using :func:`property` as a `decorator`::

   class Parrot:
   def __init__(self):
   self._voltage = 100000

   @property
   def voltage(self):
   """Get the current voltage."""
   return self._voltage

The ``@property`` decorator turns the :meth:`voltage` method into a "getter"
for a read-only attribute with the same name, and it sets the docstring for
*voltage* to "Get the current voltage."

A property object has :attr:`~property.getter`, :attr:`~property.setter`,
and :attr:`~property.deleter` methods usable as decorators that create a
copy of the property with the corresponding accessor function set to the
decorated function.  This is best explained with an example::

   class C:
   def __init__(self):
   self._x = None

   @property
   def x(self):
   """I'm the 'x' property."""
   return self._x

   @x.setter
   def x(self, value):
   self._x = value

   @x.deleter
   def x(self):
   del self._x

This code is exactly equivalent to the first example.  Be sure to give the
additional functions the same name as the original property (``x`` in this
case.)

The returned property object also has the attributes ``fget``, ``fset``, and
``fdel`` corresponding to the constructor arguments.


.. _func-range:
.. class:: range(stop)
  range(start, stop[, step])
   :noindex:

Rather than being a function, :class:`range` is actually an immutable
sequence type, as documented in `typesseq-range` and `typesseq`.


.. function:: repr(object)

Return a string containing a printable representation of an object.  For many
types, this function makes an attempt to return a string that would yield an
object with the same value when passed to :func:`eval`, otherwise the
representation is a string enclosed in angle brackets that contains the name
of the type of the object together with additional information often
including the name and address of the object.  A class can control what this
function returns for its instances by defining a :meth:`__repr__` method.


.. function:: reversed(seq)

Return a reverse `iterator`.  *seq* must be an object which has
a :meth:`__reversed__` method or supports the sequence protocol (the
:meth:`__len__` method and the :meth:`__getitem__` method with integer
arguments starting at ``0``).


.. function:: round(number[, ndigits])

Return *number* rounded to *ndigits* precision after the decimal
point.  If *ndigits* is omitted or is ``None``, it returns the
nearest integer to its input.

.. note::

   The behavior of :func:`round` for floats can be surprising: for example,
   ``round(2.675, 2)`` gives ``2.67`` instead of the expected ``2.68``.
   This is not a bug: it's a result of the fact that most decimal fractions
   can't be represented exactly as a float.  See `tut-fp-issues` for
   more information.


.. _func-set:
.. class:: set([iterable])
   :noindex:

Return a new :class:`set` object, optionally with elements taken from
*iterable*.  ``set`` is a built-in class.  See :class:`set` and
`types-set` for documentation about this class.

For other containers see the built-in :class:`frozenset`, :class:`list`,
:class:`tuple`, and :class:`dict` classes, as well as the :mod:`collections`
module.


.. function:: setattr(object, name, value)

This is the counterpart of :func:`getattr`.  The arguments are an object, a
string and an arbitrary value.  The string may name an existing attribute or a
new attribute.  The function assigns the value to the attribute, provided the
object allows it.  For example, ``setattr(x, 'foobar', 123)`` is equivalent to
``x.foobar = 123``.


.. class:: slice(stop)
  slice(start, stop[, step])

Return a `slice` object representing the set of indices specified by
``range(start, stop, step)``.  The *start* and *step* arguments default to
``None``.  Slice objects have read-only data attributes :attr:`~slice.start`,
:attr:`~slice.stop` and :attr:`~slice.step` which merely return the argument
values (or their default).  They have no other explicit functionality;
however they are used by Numerical Python and other third party extensions.
Slice objects are also generated when extended indexing syntax is used.  For
example: ``a[start:stop:step]`` or ``a[start:stop, i]``.  See
:func:`itertools.islice` for an alternate version that returns an iterator.


.. function:: sorted(iterable, *, key=None, reverse=False)

Return a new sorted list from the items in *iterable*.

.. decorator:: staticmethod

Transform a method into a static method.

A static method does not receive an implicit first argument. To declare a static
method, use this idiom
::

   class C:
   @staticmethod
   def f(arg1, arg2, ...):
 .....

.. seealso:: To learn more about static ,class and instance methods see :doc:`../ObjectOrientedProgramming/Static_Instance_ClassMethods`


.. _func-str:
.. class:: str(object='')
  str(object=b'', encoding='utf-8', errors='strict')
   :noindex:

Return a :class:`str` version of *object*.  See :func:`str` for details.

``str`` is the built-in string `class`.  For general information
about strings, see `textseq`.


.. function:: sum(iterable, /, start=0)

Sums *start* and the items of an *iterable* from left to right and returns the
total.  The *iterable*'s items are normally numbers, and the start value is not
allowed to be a string.

.. function:: super([type[, object-or-type]])

Return a proxy object that delegates method calls to a parent or sibling
class of *type*.  This is useful for accessing inherited methods that have
been overridden in a class.

The *object-or-type* determines the `method resolution order`
to be searched.  The search starts from the class right after the
*type*.

For example, if :attr:`~class.__mro__` of *object-or-type* is
``D -> B -> C -> A -> object`` and the value of *type* is ``B``,
then :func:`super` searches ``C -> A -> object``.

For both use cases, a typical superclass call looks like this::

   class C(B):
   def method(self, arg):
   super().method(arg) # This does the same thing as:
   # super(C, self).method(arg)

In addition to method lookups, :func:`super` also works for attribute
lookups.  One possible use case for this is calling `descriptors <descriptor>`
in a parent or sibling class.

Note that :func:`super` is implemented as part of the binding process for
explicit dotted attribute lookups such as ``super().__getitem__(name)``.
It does so by implementing its own :meth:`__getattribute__` method for searching
classes in a predictable order that supports cooperative multiple inheritance.
Accordingly, :func:`super` is undefined for implicit lookups using statements or
operators such as ``super()[name]``.

Also note that, aside from the zero argument form, :func:`super` is not
limited to use inside methods.  The two argument form specifies the
arguments exactly and makes the appropriate references.  The zero
argument form only works inside a class definition, as the compiler fills
in the necessary details to correctly retrieve the class being defined,
as well as accessing the current instance for ordinary methods.


.. _func-tuple:
.. class:: tuple([iterable])
   :noindex:

Rather than being a function, :class:`tuple` is actually an immutable
sequence type, as documented in `typesseq-tuple` and `typesseq`.


.. class:: type(object)
  type(name, bases, dict)

With one argument, return the type of an *object*.  The return value is a
type object and generally the same object as returned by
:attr:`object.__class__ <instance.__class__>`.

The :func:`isinstance` built-in function is recommended for testing the type
of an object, because it takes subclasses into account.
::

   numbers_list = [1, 2]
   print(type(numbers_list))

   numbers_dict = {1: 'one', 2: 'two'}
   print(type(numbers_dict))

   class Foo:
      a = 0

   foo = Foo()
   print(type(foo))

.. container:: outputs

   | **OUTPUT :**
   | <class 'list'>
   | <class 'dict'>
   | <class '__main__.Foo'>

.. function:: vars([object])

Return the :attr:`~object.__dict__` attribute for a module, class, instance,
or any other object with a :attr:`~object.__dict__` attribute.
**vars() returns the __dict__ attribute of the given object.**
::

   class Foo:
   def __init__(self, a = 5, b = 10):
      self.a = a
      self.b = b
   
   object = Foo()
   print(vars(Foo))
   print(vars(object))

.. container:: outputs

    | **OUTPUT :**
    | {'__module__': '__main__', '__init__': <function Foo.__init__ at 0x7f68c3557e50>, '__dict__': <attribute '__dict__' of 'Foo' objects>, '__weakref__': <attribute '__weakref__' of 'Foo' objects>, '__doc__': None}
    | 
    | {'a': 5, 'b': 10}

.. function:: zip(*iterables)

Make an iterator that aggregates elements from each of the iterables.

:func:`zip` should only be used with unequal length inputs when you don't
care about trailing, unmatched values from the longer iterables.  If those
values are important, use :func:`itertools.zip_longest` instead.

:func:`zip` in conjunction with the ``*`` operator can be used to unzip a
list::

   >>> x = [1, 2, 3]
   >>> y = [4, 5, 6]
   >>> zipped = zip(x, y)
   >>> list(zipped)
   [(1, 4), (2, 5), (3, 6)]
   >>> x2, y2 = zip(*zip(x, y))
   >>> x == list(x2) and y == list(y2)
   True


.. function:: __import__(name, globals=None, locals=None, fromlist=(), level=0)

.. note::

   This is an advanced function that is not needed in everyday Python
   programming, unlike :func:`importlib.import_module`.

For example, the statement ``import spam`` results in bytecode resembling the
following code::

   spam = __import__('spam', globals(), locals(), [], 0)

   The statement ``import spam.ham`` results in this call::

   spam = __import__('spam.ham', globals(), locals(), [], 0)

Note how :func:`__import__` returns the toplevel module here because this is
the object that is bound to a name by the :keyword:`import` statement.

On the other hand, the statement ``from spam.ham import eggs, sausage as
saus`` results in ::

   _temp = __import__('spam.ham', globals(), locals(), ['eggs', 'sausage'], 0)
   eggs = _temp.eggs
   saus = _temp.sausage

Here, the ``spam.ham`` module is returned from :func:`__import__`.  From this
object, the names to import are retrieved and assigned to their respective
names.

If you simply want to import a module (potentially within a package) by name,
use :func:`importlib.import_module`.
