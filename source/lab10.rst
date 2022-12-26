*******
Lab #10
*******


**1**

Write a code to swap the content of two variables, such as:

.. code-block:: python

    a = 3
    b = 29

**2**

Write a function that will take two strings as parameters and return their concatenation.


**3**

Give an example if values for `a`, `b` and `c` that will cause the code to print `X` and `Y`.

.. code-block:: python

    def dumb_function(a,b,c):
    if a < b and a < c:
        print("W")
    else:
        print("X")
        if b == c:
            print("Y")
        elif b < c:
            print("Z")
        else:
            print("Q")

**4**

Write a function `findMinIndex(aList)` that takes a list, searches the list for the index of the smallest element in the list, and return the index. If there are multiple copies if the smallest element return the first one. 

**You may not use the built-in functions min, index, find, etc.**

.. code-block:: python

    def findMinIndex(aList):
        # Implement here

**5**

Write a function ``printDownRight(mat)`` that will print out all the contents of a 2D matrix ``mat`` along the diagonal starting at the top left and ending at the bottom right.

