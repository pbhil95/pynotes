==============================
File Objects in Python
==============================

A file object allows us to use, access and manipulate all the user accessible files. One can read and write any such files.
When a file operation fails for an I/O-related reason, the exception IOError is raised. This includes situations where the operation is not defined for some reason, like ``seek()`` on a tty device or writing a file opened for reading.

Files have the following methods:

``open()``
============

Opens a file in given access mode.
::
    
    open(file_address, access_mode) 

Examples of accessing a file: A file can be opened with a built-in function called ``open()``. This function takes in the file’s address and the access_mode and returns a file object.

There are different types of access_modes:

* ``r``: Opens a file for reading only
* ``r+``: Opens a file for both reading and writing
* ``w``: Opens a file for writing only
* ``w+``: Open a file for writing and reading.
* ``a``: Opens a file for appending
* ``a+``: Opens a file for both appending and reading

When you add ``'b'`` to the access modes you can read the file in binary format rather than the default text format. It is used when the file to be accessed is not in text.

``read([size])``
=================

It reads the entire file and returns it contents in the form of a string. Reads at most size bytes from the file (less if the read hits EOF before obtaining size bytes). If the size argument is negative or omitted, read all data until EOF is reached.
::

        f = open(__file__, 'r') 

        text = f.read(10) 

        print(text) 

        f.close() 

``readline([size])``
======================

It reads the first line of the file i.e till a newline character or an EOF in case of a file having a single line and returns a string. If the size argument is present and non-negative, it is a maximum byte count (including the trailing newline) and an incomplete line may be returned. An empty string is returned only when EOF is encountered immediately.
::

    f = open(__file__, 'r') 

    text = f.readline(20) 

    print(text) 

    f.close() 

``readlines([sizehint])``
===========================

It reads the entire file line by line and updates each line to a list which is returned.Read until EOF using readline() and return a list containing the lines thus read. If the optional sizehint argument is present, instead of reading up to EOF, whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read.
::

    f = open(__file__, 'r') 

    text = f.readlines(25) 

    print(text) 

    f.close() 

``write(string)``
=================

It writes the contents of string to the file. It has no return value. Due to buffering, the string may not actually show up in the file until the flush() or close() method is called.
::

    f = open(__file__, 'w') 

    line = 'Welcome Geeks\n'

    f.write(line) 

    f.close() 

**More Examples in different modes:**

Reading and Writing a file
----------------------------
::

    f = open(__file__, 'r+') 

    lines = f.read() 

    f.write(lines) 

    f.close() 

Writing and Reading a file
---------------------------
::

    f = open(__file__, 'w+') 

    lines = f.read() 

    f.write(lines) 

    f.close() 

Appending a file
--------------------
::

    f = open(__file__, 'a') 

    lines = 'Welcome Geeks\n'

    f.write(lines) 

    f.close() 

Appending and reading a file 
------------------------------
::

    f = open(__file__, 'a+') 

    lines = f.read() 

    f.write(lines) 

    f.close() 

``writelines(sequence)``
==========================

It is a sequence of strings to the file usually a list of strings or any other iterable data type. It has no return value.
::

    f = open(__file__, 'a+') 

    lines = f.readlines() 

    f.writelines(lines) 

    f.close()

``tell()``
===========

It returns an integer that tells us the file object’s position from the beginning of the file in the form of bytes
::

    f = open(__file__, 'r') 

    lines = f.read(10) 

    print(f.tell()) 

    f.close()

``seek(offset, from_where)``
==============================

It is used to change the file object’s position. Offset indicates the number of bytes to be moved. from_where indicates from where the bytes are to be moved.
::

    f = open(__file__, 'r') 

    lines = f.read(10) 

    print(lines) 

    print(f.seek(2,2)) 

    lines = f.read(10) 

    print(lines) 

    f.close() 

``flush()``
=============

Flush the internal buffer, like stdio‘s ``fflush()``. It has no return value. ``close()`` automatically flushes the data but if you want to flush the data before closing the file then you can use this method.
::

    f = open(__file__, 'r') 

    lines = f.read(10) 

    f.flush() 

    print(f.read()) 

    f.close()

``fileno()``
==============

Returns the integer file descriptor that is used by the underlying implementation to request I/O operations from the operating system.
::

    f = open(__file__, 'r') 

    print(f.fileno()) 

    f.close()

``isatty()``
===================

Returns True if the file is connected to a tty(-like) device and False if not.
::

    f = open(__file__, 'r') 

    print(f.isatty()) 

    f.close() 

``next()``
=============

It is used when a file is used as an iterator. The method is called repeatedly. This method returns the next input line or raises StopIteration at EOF when the file is open for reading( behaviour is undefined when opened for writing).
::

    f = open(__file__, 'r') 

    try: 

    while f.next(): 

    print(f.next()) 

    except: 

    f.close()

``truncate([size])``
=====================

Truncate the file’s size. If the optional size argument is present, the file is truncated to (at most) that size. The size defaults to the current position. The current file position is not changed. Note that if a specified size exceeds the file’s current size, the result is platform-dependent: possibilities include that the file may remain unchanged, increase to the specified size as if zero-filled, or increase to the specified size with undefined new content.
::

    f = open(__file__, 'w') 

    f.truncate(10) 

    f.close()

``close()``
=============

Used to close an open file. A closed file cannot be read or written any more.
::

    f = open(__file__, 'r') 

    f.close() 

Attributes
=================

**closed:** returns a boolean indicating the current state of the file object. It returns true if the file is closed and false when the file is open.

**encoding:** The encoding that this file uses. When Unicode strings are written to a file, they will be converted to byte strings using this encoding.

**mode:** The I/O mode for the file. If the file was created using the open() built-in function, this will be the value of the mode parameter.

**name:** If the file object was created using open(), the name of the file.

**newlines:** A file object that has been opened in universal newline mode have this attribute which reflects the newline convention used in the file. The value for this attribute are “\r”, “\n”, “\r\n”, None or a tuple containing all the newline types seen.

**softspace:** It is a boolean that indicates whether a space character needs to be printed before another value when using the print statement.
::

    f = open(__file__, 'a+') 

    print(f.closed) 

    print(f.encoding) 

    print(f.mode) 

    print(f.newlines) 

    print(f.softspace) 
