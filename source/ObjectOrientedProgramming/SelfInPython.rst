==================
Self in Python
==================

Introduction
=============

.. note::

    * The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

    * It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.

But before talking about the self keyword (which is actually not a python keyword or any special literal), first, let’s recall what are class variables and instance variables. **Class variables are variables that are being shared with all instances (objects) which were created using that particular class.** So when accessed a class variable from any instance, the value will be the same. **Instance variables, on the other hand, are variables which all instances keep for themselves (i.e a particular object owns its instance variables). So typically values of instance variables differ from instance to instance.**

Class variables
==================

Class variables in python are defined just after the class definition and outside of any methods:
::

    class SomeClass:
        variable_1 = "This is a class variable"
        variable_2 = 100   #this is also a class variable

instance variables
=====================

Unlike class variables, instance variables should be defined within methods:
::

    class SomeClass:
        variable_1 = "This is a class variable"
        variable_2 = 100    #this is also a class variable.

        def __init__(self, param1, param2):
            self.instance_var1 = param1
            #instance_var1 is a instance variable
        self.instance_var2 = param2   
            #instance_var2 is a instance variable


Difference between class and instance variables
==================================================

Let’s instantiate above class and do some introspections about those instances and above class:
::

    >>> obj1 = SomeClass("some thing", 18) 
    #creating instance of SomeClass named obj1
    >>> obj2 = SomeClass(28, 6) 
    #creating a instance of SomeClass named obj2

    >>> obj1.variable_1
    'a class variable'

    >>> obj2.variable_1
    'a class variable'

So as seen above, both obj1 and obj2 gives the same value when variable_1 is accessed, which is the normal behavior that we should expect from a class variable.

Let’s find about instance variables:
::

    >>> obj1.instance_var1
    'some thing'
    >>> obj2.instance_var1
    28

So the expected behavior of instance variables can be seen above without any error. That is, both obj1 and obj2 have two different instance variables for themselves.

self — intuition
===================

Some of you may have got it by now, or some may have got it partially; anyway, the self in python represents or points the instance which it was called. Let’s clarify this with an example:
::

    class SomeClass:
        def __init__(self):
            self.arr = [] 
            #All SomeClass objects will have an array arr by default
        
        def insert_to_arr(self, value):
            self.arr.append(value)

So now let’s create two objects of SomeClass and append some values for their arrays:
::

    obj1 = SomeClass()
    obj2 = SomeClass()
    obj1.insert_to_arr(6)

.. Note::

    Unlike some other languages, when a new object is created in python, it does not create a new set of instance methods to itself. So instance methods lie within the class object without being created with each object initialization — nice way to save up memory. Recall that python is a fully object oriented language and so a class is also an object. So it lives within the memory.

Being said that, let’s look at the above example. There we have created obj1 and are calling the instance method ``insert_to_arr()`` of SomeClass while passing an argument 6. **But now how does that method know “which object is calling me and whose instance attributes should be updated”. Here, to whose arr array should I append the value 6? Ok, now I think you got it. That’s the job of self.** Behind the scene, in every instance method call, python sends the instance also with that method call. So what actually happens is, python convert the above calling of the instance method to something like below:
::

    SomeClass.inseart_to_arr(obj1, 6)

Now you know why you should always use self as the first parameter of instance methods in python and what really happens behind the scene when we call an instance method.

Self Can Be Avoided
======================

By now you are clear that the object (instance) itself is passed along as the first argument, automatically. This implicit behavior can be avoided while making a static method. Consider the following simple example:
::

    class A(object):

        @staticmethod
        def stat_meth():
            print("Look no self was passed")

Here, ``@staticmethod`` is a function decorator which makes ``stat_meth()`` static. Let us instantiate this class and call the method.

::

    >>> a = A()
    >>> a.stat_meth()
    Look no self was passed

From the above example, we can see that the implicit behavior of passing the object as the first argument was avoided while using a static method. All in all, static methods behave like the plain old functions (Since all the objects of a class share static methods).
::

    >>> type(A.stat_meth)
    <class 'function'>
    >>> type(a.stat_meth)
    <class 'function'>