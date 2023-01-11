*********************
Functions and turtles
*********************

Remember, the point of the lab is **not** to complete the tasks. The point of the labs is to understand why the code you have written does what it does. Do not rush through the steps. Take your time and understand everything we are doing. The understanding is important, **not** just knocking off the tasks. 


Before Kattis
=============

**NOTE:**  :doc:`If you forget how to do the function, go back to the class notes. </topic3>`

In this lab you will aply what you learned on something different: Turtle!

Turtle is a old drawing tool in python.


1. Open colab. On a first cell copy, paste and execute the next lines:

.. code-block::

    !pip3 install ColabTurtle
    from ColabTurtle.Turtle import *

2. Turtle propose different functions listed below. Try them and understand how they work!

   *  :code:`forward(unit)`: Moves the turtle in the direction it is facing, by :code:`unit` pixels.
   *  :code:`backward(units)`: Moves the turtle in the opposite of the direction it is facing, by :code:`unit` pixels.
   *  :code:`right(degrees)`: Turns the turtle to right by the given :code:`degrees` many degrees.
   *  :code:`left(degrees)`: Turns the turtle to left by the given :code:`degrees` many degrees.
   *  :code:`penup()`: Lifts the pen, turtles movement will not draw anything after this function is called.
   *  :code:`pendown()`: Puts the pen down, causing the turtle movements to start drawing again.
   *  :code:`home()`: Takes the turtle to the beginning position and angle. The turtle will continue drawing during this operation if the pen is down.
   *  :code:`clear()`: Clear any drawing on the screen.

3. Write a function :code:`reset()` that return the turtle fome and clear any drawing.

4. Write a **function** called :code:`square(unit)` that takes one integer as parameter, and draw a square of :code:`unit` side length. Call the function to verify its correctness with he below code.

    .. code-block:: python
    
        square(100)


5. Write a **function** called :code:`rectangle(width, height)` that takes two integers as parameters, and draw a rectangle. Call the function to verify its correctness witht he below code.

    .. code-block:: python
    
        rectangle(200, 100)

5. Write a **function** called :code:`rhombus(angle_1, angle_2, unit)` that takes three integers as parameters, and draw a rhonbus (or diamond). Call the function to verify its correctness with he below code.

    .. code-block:: python
    
        rhombus(70,110, 100)

   **Note: A Pen and paper can help on this one.**


6. Modify the previous functions to take one new parameter :code:`colorstring`. :code:`colorstring` will be the color of the pen.

   To modify the color you can use the function :code:`pencolor(colorstring)`.


7.  Write a **function** called :code:`three_squares(unit, space)` that takes two integers as parameters, and draw three squares of side length :code:`unit` separated by a length of :code:`space`. Call the function to verify its correctness with he below code.

   .. code-block::

    three_squares(100, 20)

   **Note: You should use the square function defined before. You only need to make sure that you move the turtle without drawing between the squares.**



Kattis Problems
===============

Continue the previous Kattis problems.

Remember, here is *magic* code we needed last week::
   
    data = input()       # Read a WHOLE, SINGLE line of input
    data = data.split()  # Split string into individual pieces
    a_var = int(data[0]) # Take string from data[X], convert it to int...   
    b_var = int(data[1]) # ... And store it in some variable

.. warning::
   
    The above will only work for certain situations, so you will need to hack this to make it work for specific cases!!!!!!!!!!!!!


Grab a scrap piece of paper to start scratching your ideas down on paper. Paper and pencil is where a lot of **programming** happens. 

Skip any of the following problems if you did them already. 

1. https://open.kattis.com/problems/hello 
2. https://open.kattis.com/problems/carrots 
3.  https://open.kattis.com/problems/r2
4.  https://open.kattis.com/problems/faktor (This one is kinda' a brain teaser. It requires the simplest of math, but it's not trivial.)
5.  https://open.kattis.com/problems/ladder (Hope you remember your Gr 10 math... if not, good thing Google exists)
6.  https://open.kattis.com/problems/planina (Looks like an INTEGER SEQUENCE (if only there was an *On-line encyclopedia*).

7.  `Go to Kattis and sort the problems by difficulty <https://open.kattis.com/problems?order=problem_difficulty>`_. Read them, understand the problem, then see if you can figure any out. Most you can't yet, but still see what you can do and what you CAN'T.  Try to figure out *why* you can't.  

**ENSURE WE HAVE RECORDED YOUR COMPLETION. FAILURE TO DO SO WILL RESULT IN A GRADE OF 0!**
