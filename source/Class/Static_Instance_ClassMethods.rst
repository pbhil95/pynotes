===============================
Class and Instance Attributes
===============================

Introduction
==============

* Regular (instance) methods need a class instance and can access the instance through ``self``. **They can read and modify an objects state freely.**

* Class methods, marked with the ``@classmethod`` decorator, don’t need a class instance. **They can’t access the instance (self) but they have access to the class itself via cls.**

* Static methods, marked with the ``@staticmethod`` decorator, **don’t have access to cls or self.** They work like regular functions but belong to the class’s namespace.

.. tip:: 
    Static and class methods communicate and (to a certain degree) enforce developer intent about class design. This can have maintenance benefits.

Static Methods
===============

We used class attributes as public attributes in the previous section. Of course, we can make public attributes private as well. We can do this by adding the double underscore again. If we do so, we need a possibility to access and change these private class attributes. We could use instance methods for this purpose:

.. code-block:: python
    :caption: Python

    class Robot:
        __counter = 0
        
        def __init__(self):
            type(self).__counter += 1
            
        def RobotInstances(self):
            return Robot.__counter
            

    if __name__ == "__main__":
        x = Robot()
        print(x.RobotInstances())
        y = Robot()
        print(x.RobotInstances())
    
    Output:
    1
    2

This is not a good idea for two reasons: First of all, because the number of robots has nothing to do with a single robot instance and secondly because we can't inquire the number of robots before we create an instance. If we try to invoke the method with the class name Robot.RobotInstances(), we get an error message, because it needs an instance as an argument:

.. code-block:: python
    :caption: Python

    Robot.RobotInstances()

    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-35-f53600e3296e> in <module>
    ----> 1 Robot.RobotInstances()

    TypeError: RobotInstances() missing 1 required positional argument: 'self'

The next idea, which still doesn't solve our problem, is omitting the parameter "self":

.. code-block:: python
    :caption: Python

    class Robot:
        __counter = 0
        
        def __init__(self):
            type(self).__counter += 1
            
        def RobotInstances():
            return Robot.__counter

Now it's possible to access the method via the class name, but we can't call it via an instance:

.. code-block:: python
    :caption: Python
    
    from static_methods2 import Robot
    Robot.RobotInstances()

    Output::
    0
    x = Robot()
    x.RobotInstances()

    ---------------------------------------------------------------------------
    TypeError                                 Traceback (most recent call last)
    <ipython-input-40-4d5e11c3474a> in <module>
        1 x = Robot()
    ----> 2 x.RobotInstances()

    TypeError: RobotInstances() takes 0 positional arguments but 1 was given

    The call "x.RobotInstances()" is treated as an instance method call and an instance method needs a reference to the instance as the first parameter.

**So, what do we want? We want a method, which we can call via the class name or via the instance name without the necessity of passing a reference to an instance to it.**

**The solution lies in static methods, which don't need a reference to an instance. It's easy to turn a method into a static method.** All we have to do is to add a line with :func:`staticmethod` directly in front of the method header. It's the decorator syntax.

You can see in the following example that we can now use our method RobotInstances the way we want:

.. code-block:: python
    :caption: Python

    class Robot:
        __counter = 0
        
        def __init__(self):
            type(self).__counter += 1
            
        @staticmethod
        def RobotInstances():
            return Robot.__counter
            

    if __name__ == "__main__":
        print(Robot.RobotInstances())
        x = Robot()
        print(x.RobotInstances())
        y = Robot()
        print(x.RobotInstances())
        print(Robot.RobotInstances())
    
    Output:
    0
    1
    2
    2

Class Methods
==============

Static methods shouldn't be confused with class methods. Like static methods class methods are not bound to instances, but unlike static methods class methods are bound to a class. The first parameter of a class method is a reference to a class, i.e. a class object. They can be called via an instance or the class name.

.. code-block:: python
    :caption: Python

    class Robot:
        __counter = 0
        
        def __init__(self):
            type(self).__counter += 1
            
        @classmethod
        def RobotInstances(cls):
            return cls, Robot.__counter
            

    if __name__ == "__main__":
        print(Robot.RobotInstances())
        x = Robot()
        print(x.RobotInstances())
        y = Robot()
        print(x.RobotInstances())
        print(Robot.RobotInstances())

.. code-block::
    :caption: Output

    (<class '__main__.Robot'>, 0)
    (<class '__main__.Robot'>, 1)
    (<class '__main__.Robot'>, 2)
    (<class '__main__.Robot'>, 2)

Class Methods vs. Static Methods and Instance Methods
=======================================================

This example will demonstrate the usefulness of class methods in inheritance. We define a class :class:`Pet` with a method :func:`about`. This method should give some general class information. The class :class:`Pet` will be inherited in a subclass :class:`Dog` and :class:`Cat`. The method :func:`about` will be inherited as well. We will demonstrate that we will encounter problems, if we define the method :func:`about` as a normal instance method or as a static method. We will start by defining :func:`about` as an instance method:

.. code-block:: python
    :caption: Python
    
    class Pet:
        _class_info = "pet animals"

        def about(self):
            print("This class is about " + self._class_info + "!")   
        
    class Dog(Pet):
        _class_info = "man's best friends"

    class Cat(Pet):
        _class_info = "all kinds of cats"

    p = Pet()
    p.about()
    d = Dog()
    d.about()
    c = Cat()
    c.about()

.. code-block:: 
    :caption: Output

    This class is about pet animals!
    This class is about man's best friends!
    This class is about all kinds of cats!

**This may look alright at first at first glance. On second thought we recognize the awful design. We had to create instances of the Pet, Dog and Cat classes to be able to ask what the class is about. It would be a lot better, if we could just write** ``Pet.about()``, ``Dog.about()`` **and** ``Cat.about()`` **to get the previous result. We cannot do this. We will have to write** ``Pet.about(p)``, ``Dog.about(d)`` **and** ``Cat.about(c)`` **instead.**

**Now, we will define the method "about" as a "staticmethod" to show the disadvantage of this approach.** As we have learned previously in our tutorial, a staticmethod does not have a first parameter with a reference to an object. So about will have no parameters at all. Due to this, we are now capable of calling :func:`about` without the necessity of passing an instance as a parameter, i.e. "Pet.about()", "Dog.about()" and "Cat.about()". Yet, a problem lurks in the definition of :func:`about`. The only way to access the ``_class_info`` is putting a class name in front. We arbitrarily put in "Pet". We could have put there "Cat" or "Dog" as well. No matter what we do, the solution will not be what we want:

.. code-block:: python
    :caption: Python

    class Pet:
        _class_info = "pet animals"

        @staticmethod
        def about():
            print("This class is about " + Pet._class_info + "!")   
        
    class Dog(Pet):
        _class_info = "man's best friends"

    class Cat(Pet):
        _class_info = "all kinds of cats"

    Pet.about()
    Dog.about()
    Cat.about()

.. code-block:: 
    :caption: Output

    This class is about pet animals!
    This class is about pet animals!
    This class is about pet animals!

*In other words, we have no way of differenciating between the class Pet and its subclasses Dog and Cat.The problem is that the method "about" does not know that it has been called via the Pet, the Dog or the Cat class .*

**A classmethod is the solution to all our problems. We will decorate** :func:`about` **with a classmethod decorator instead of a staticmethod decorator:**

.. code-block:: python
    :caption: Python

    class Pet:
        _class_info = "pet animals"

        @classmethod
        def about(cls):
            print("This class is about " + cls._class_info + "!")   
        
    class Dog(Pet):
        _class_info = "man's best friends"

    class Cat(Pet):
        _class_info = "all kinds of cats"

    Pet.about()
    Dog.about()
    Cat.about()

.. code-block::
    :caption: Output

    This class is about pet animals!
    This class is about man's best friends!
    This class is about all kinds of cats!

