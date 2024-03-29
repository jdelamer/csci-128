*********
Functions
*********

.. image:: ../../img/Eniac.jpeg


Functions
=========

* Script/program files are a nice way to organize many statements
* You eventually find yourself writing the same series of statements over and over
* Imagine the following code is super important:

.. code-block:: python

    x = 10 * 2
    y = x/4
    print(y)

* OK, good, that wasn't so bad
* But now you need to do the same calculation two more times, but with 9 and then 8 instead of 10
* Now your program looks like this:

.. code-block:: python

    x = 10 * 2
    y = x/4
    print(y)
	
    x = 9 * 2
    y = x/4
    print(y)
	
    x = 8 * 2
    y = x/4
    print(y)

* That wasn't bad, but it does feel somewhat silly to copy/paste the code
* Now you realize that it should be divided by 3 instead of 4...
* So you change your code:

.. code-block:: python

	x = 10 * 2
	y = x/3
	print(y)
	
	x = 9 * 2
	y = x/3
	print(y)
	
	x = 8 * 2
	y = x/3
	print(y)


.. warning::

    This change could lead to a few mistakes. You would be lucky to not miss one modification or not creating bugs.


There's gotta' be a better way!
===============================

* We want a way to *group together sequence of statements that we frequently reuse*
* In Python, we do this with a *function*. Here's one now:

.. code-block:: python

    def my_function(a_parameter):
        b = a_parameter * 2
        print(b)
		
* Once you've defined a function, you can *call* it exactly the same way you'd call a *built-in function* like :code:`print()`.
  
* So let's use our function:
    >>> my_function(2)
    4
    
    >>> my_function(7)
    14
	
    >>> my_function('Jean')
    JeanJean

* When we *call* :code:`my_function`, Python executes the statements that
  make up the function, in order.
* Functions make code easy to reuse, easy to edit, and easy to read. More importantly they *facilitate abstraction*.	


.. admonition:: Quick Activity
    :class: activity

    Write your own function to do something with math. Honestly, whatever you want. 

Function Parameters
===================

* Note carefully the parameter (:code:`a_parameter`) in the definition of :code:`my_function`
* When you are defining a function, you want the function to be very *general*
    * You want it to work with *any possible* parameter that someone might want to give it
   
* Imagine we want to write a function to add two numbers together
    * We want to be able to have this function add **any** two numbers together

* Parameters are like variables. When you *call* the function, the first thing that happens is the parameter values get set.   
   
* To motivate this, let's go back to our previous example and throw it in a function:

.. code-block:: python
   
    def a_function():
        x = 10 * 2
        y = x/4
        return y

* This function is kinda' stuck; it will only ever do multiply 10 by 2, and then divide it by 4...
* Instead, we'll give it parameters:

.. code-block::

	def a_function(a_value, another_value):
	   x = a_value * 2
	   y = x/another_value
	   return y

* And we can call it like this:

.. code-block::

    a_function(10, 4)

* If this is scaring you, chill
* Like it or not, you've been doing this for years in math class

.. math::

    f(x) = x + 5
   
* This is a math *function* that takes a *parameter* 
* What happens if you say... f(5)
    * :math:`f(5) = 5 + 5`
    * :math:`f(5) = 10`

* It's the same in programming!
   
   
* Let's do one more example with adding two numbers::

    def return_print(a, b):
        return a + b

* Now that the function is defined, we can *call* it. Like this:

    >>> return_print(5, 2)
    7

* The *call* :code:`return_print(5, 2)` gets handled like this:
    * Python checks to see if it knows about a function named :code:`return_print`
        * We just defined `return_print`, so it does.
    * When we defined it, we told Python it should have two parameters: :code:`a` and :code:`b`.
    * Python now takes the values in the call (in this case, :code:`5` and :code:`2`) and assigns those
     values to the function parameters :code:`a` and :code:`b`.
        * In other words, the first thing Python does in this case is set :code:`a = 5` and :code:`b = 2`, just like variables. 
    * Then Python executes the body of the function, with the parameters having their new values.
    * Then it *return* the sum of :code:`a` and :code:`b`, meaning it send back the value to your *main* code.

     
* What happens if we don't give it enough, or too many parameters?

Abstraction: first steps
========================

* Why is abstraction important?

.. admonition:: Activity
    :class: activity

    Write down a "program" to make spaghetti (not in python, like on paper). You can only use the following statements: 

    * ``locate [object]`` 
    * ``grasp [limb]`` 
    * ``release [limb]`` 
    * ``move_limb_to [location]``
    * ``wait [time in seconds]``

    Assume you start from a clean, empty, kitchen.

.. admonition:: Activity
    :class: activity

    Write down a "program" to make spaghetti (not in python, like on paper). You can use plain English prose and assume you are addressing a human being.

* You've now written programs at two levels of abstraction. Which was easier?
* Functions allow us to build *towers of abstraction*. 
    * A low level function might worry about how to set the individual pixels of the display to show the letter ``A`` . 
        * Consider ``print()``
    * Would you want to cut-and-paste that code every time you needed to print ``A``?
    * Instead, we have a function called ``print()`` that hides all those messy details from us.
    * We call ``print()``, ``print()`` calls other functions, which call other functions, which call other functions...

    * Without organizing things into *levels of abstraction* writing complex software would be impossibly difficult.

* Forget programming. In the rest of your life, learning to think in terms of levels of abstraction is a hugely important skill.
  
* In fact, think about us. 
    * When you move your arms, did you explicitly think about firing neurons, flexing muscles and moving tendons?
    * When driving a car, do you think about the pistons firing? 


Back to concrete things...
==========================

* The general format for defining a function is::

	def function_name(p1, p2, p3, p4, ... ):
		statement 1
		statement 2
		...
		statement m
		
* ``function_name`` is... the name of the function. This can be almost whatever you want.
* ``p1, p2`` , etc. are called the *parameters*, you can have as many as you like and call them almost whatever you want. 
* You tell Python which statements make up the *body* of the function by using *indentation*.
    * This is a somewhat unique feature of Python. 
        * And somewhat hated by some people. 
    * Many other languages use pairs like ``begin, end`` , ``do, done`` or ``{, }`` to delimit the body of a function.

.. admonition:: Activity
    :class: activity

    Write a function ``catstr`` which takes two strings as parameters and then prints out the concatenation of the strings. e.g., if I call ``catstr('Hello ','world!')`` it will print ``Hello world!``.

   
   
.. admonition:: Activity
    :class: activity

    **NOTE:** This one is tricky but super important to understand. If you're still stuck after class, be sure to take your time to figure this out.
   
    Now write a function ``crosscat`` that will take *four* strings and print out the concatenation of the first and third string, and then, on a new line, the concatenation of the second and fourth string. **BUT**: your function isn't allowed to use a ``print`` function! You can, however, use your ``catstr`` function.

		
Execution Flow
==============

* Python executes one statement at a time
* To make sense of programs, we need to know *which* instruction gets executed *when*
* In a program, the statements get executed in the order in which they appear in the program, top to bottom of the file
    * Later, we'll learn how to jump around
* What happens when a function gets called? Let's trace through this program::

    def do_stuff(a, b):
        c = b * 2
        d = (a+4) * 2
        c = d + c
        return c
	
    x = 2
    y = 3
    z = do_stuff(x, y)
    print(z)
    print("where am I?")

* So what happens is:
    * Program starts at the top, and computer sees that a function is being *declared* (not called yet)
        * NOT RUN YET THOUGH!
    * Computer basically skips down to where the function ends
    * We assign some values to variables   
    * Python makes a note of where the function is being called from
    * The *flow of execution* passes to the function
    * Python executes each statement in the function, in order
    * At the end of the function, control returns to the point from which the function was called	

   
Function values
===============

* Notice how ``do_stuff`` ended with a ``return`` statement
* The ``return`` statement tells Python: "*return* this value to whoever called this function"
* With ``return``, *functions* evaluate into *values*.
* Consider:
    >>> print(do_stuff(2, 2))
    16
    
    >>> print(do_stuff(4, 4))
    24
	
    >>> print(do_stuff(2, 2) + do_stuff(4, 4))
    40
    
* When Python hits a ``do_stuff``, it goes and *does stuff* (executes the function).
* Because that function ends in a ``return``, when execution flow comes back to the calling program, the call to ``do_stuff`` gets replaced with whatever value got ``return`` ed.

.. admonition:: Activity
    :class: activity

    * Write a function ``no_stuff(a, b)`` which is identical to ``do_stuff(a, b)`` **except** it does not contain a ``return`` statement.
    * What happens when you try this?
        >>> print(no_stuff(2, 2))
    * What happens when you try this?
        >>> print(do_stuff(2, 2))

.. Warning::

    The difference between a ``print`` and a ``return`` is **HUGE**, yet, every year this difference ends up being a problem for many students. Make sure to take your time understanding the difference. Take your time. Play around. Remember, playing around with Python is the best way to learn this stuff.   


.. admonition:: Activity
    :class: activity

    Write a function ``compmag(r,m)`` to compute, and return, the magnitude of a complex number. It should take the real component of the number as parameter ``r`` and the imaginary component as ``m``.
   
    Remember that :math:`|r + mi| = \sqrt{r-2 + m-2}` (if this looks scary, all I really want you do to is the right hand side of the equation) 
   
    Say, does Python have a square root function?
    How would you find it?


	
	
Composition
===========

* Python functions can be *composed* just like mathematical functions.
* We've already seen ``print`` composed with ``do_stuff``
* We can nest functions, too:
    >>> do_stuff(do_stuff(2, 2), do_stuff(2, 2))
    72
* If you get confused tracing nested functions, just remember:
    * Functions get *evaluted* and turned into values
    * Find a function you can evaluate
    * Evaluate it
    * Cross out the function and replace it with the *value* it returns
    * Keep doing this until you're down to one value.

.. admonition:: Activity
    :class: activity

    Figure out the value of ``do_stuff(do_stuff(2, 2), (do_stuff(2, 2) + do_stuff(4, 4)) )`` using only *pen and paper*. No computers!

.. admonition:: Activity
    :class: activity

    Figure out the value of ``no_stuff(no_stuff(2, 2), (no_stuff(2, 2) + no_stuff(4, 4)) )`` using only *pen and paper*. No computers!
	
Variable scope
==============

* If you set a variable inside a function, it is *local* to that function.
* No other function can see a function's local variables. They are *local*. Consider this code::

    def do_more(a, b):
        c = 2*a + b
        return c


* What happens if I do this:
    >>> print do_more(4, 4)
    12

    >>> print(c)
    NameError: name 'c' is not defined
	
* Error! But ``c`` is defined in ``do_more``! Why did we get an error?
* Moral of the story: variables have *scope*. This can actually be a surprisingly delicate concept and we'll come back to it later.	
	
Optional parameters for functions
=================================

* Sometimes you want a function to have an optional parameter, with a pre-specified default value.
* This is done very easily::

    def my_function(a, b, c=3):
        do_stuff()
      
* When you call ``my_function(5, 12)``, ``a`` will have value ``5``, ``b`` value ``12`` and ``c`` value ``3``.
* Because we specified a *default* value for ``c``, we don't have to provide one when we call the function.
* If we want to *override* the default, though, we can: ``my_function(4, 3, 2)``.

* A reasonable example::

    def time_to_fall(d, a=9.807):
        return math.sqrt(2*d/a)	
	
Import
======

* Another practical matter: sometimes you want to make a big library of functions. Maybe related to analysis data from your research. 
* You'd like to access some of those functions from another program that you're writing.
* If you put your functions in a file called 'myfuncs.py', you can *import* them into another program like this:
    >>> from myfuncs import *
* (The ``*`` here means *everything*)
* You could also use:
    >>> import myfuncs
* This is my preferred way
* **BUT**, this adds a namespace. To access a function called ``do_stuff`` in the file ``myfunc`` after this style of ``import``, you'd have to type
    >>> myfuncs.do_stuff(...)

Import --- MORE
===============

* Can also import other people's functions
* 	>>> import math
* 	>>> import numpy	


Comments
========

* You can add *comments* to your code in Python with ``#``::

    do_something()
    # We just did something
    # Now we'll do something else
    do_something_else() # doing something else
   
* As soon as Python sees ``#`` it ignores the rest of the current line
* Writing comments makes your code *easier to read*
* Especially 6 weeks later when you have to change it


* And *especially* when someone else has to make sense of your code
* Comments shouldn't just repeat what's obvious from reading the code
* They should provide a *higher level* description of what's happening.
* Find a healthy balance that works for you

Function headers
================

* Because so much of our programming consists of pasting together functions... it is of special
  importance to document what a function does.
* We do this with a *function header*:

.. code-block:: python

    def set_up_cities(names):
        """
        Set up a collection of cities (world) for our simulator.
        Each city is a 3 element list, and our world will be a list of cities.
        
        :param names: A list with the names of the cities in the world.
        
        :return: a list of cities
        """

        print 1 + 2

* The stuff between the ``"""`` is the function header and should appear *immediately after* the ``def``.
* It should explain what the function is going to do, in plain English. If I have to read the function code to figure out what it does, your header description sucks.
* It should explain *every* parameter.
* If the function returns something, it should explain that too

This might all seem like a lot of extra work. And it is. But it's *less* work than trying to figure out how everything works after you've been away from the code for 2 months.

You don't believe me. You'll leave this course and go write code with no comments. Seriously, you will. You might *mean* to write comments, but you won't. You're just too *busy*.
 
Then, at some later point, you'll have to go back to your code. It won't have comments. You'll have no clue how anything works. It'll take you a day or two just to figure out what you'd done before.

After that happens enough times, you'll start writing comments.


	
