***************************
Print, Operations and Types
***************************

NOTE: I do not expect you to actually finish everything so don't worry. We'll aim to get up to step 16. 

Getting Familiar 
================

1. Get logged in. 
2. Log onto Colab
3. Get Hello World working on Colab


.. warning:: 
    Do no panic. You do not need to remember how to use Colab. I'm simply just showing you so you have some familiarity. For now, I recommend sticking with Colab.

Refreshing What We Learned
==========================

4. Go back to Colab (or use whichever programming method you prefer)
5. Enter the following into your code.

    .. code-block:: python
   
        a = 5
        a = a * 2
        
    Print out the type of :code:`a`.
    
6. Enter the following into your code 

    .. code-block:: python
   
        a = 5
        a = a * 2.5
    
    Print out the type of :code:`a`. 
    
    Is this what you expected?

7. Make two variables and assign values. Then, add them together and save the result in another variable. THEN, print out the result from the third variable. 


Kattis
======

.. admonition:: Note

    It will be a lot easier to build your solutions on Colab and then copy/paste them into Kattis. 
    

*  Kattis sign up (be sure to set affiliation) 

    * Go to settings to do this
    * Also, you might want to set your default language to Python 3
    
*  https://open.kattis.com/problems/hello (Let's get that O in IO working)   


*  https://open.kattis.com/problems/carrots (Let's now get the I in IO working)

    Although I give you a solution below, the actual task I want you to do for this step is to look at the code, read the comments, and try to figure out WTF is going on. Talk to each other. Make sure it makes sense. Take your time. Ask us questions. That's what this is all about.

   *  Here is a solution with an explanation::
   
        # This loads in the first line (it's of type STRING!)
        # For example, if we take the first sample input of --- 2 1
        # Then the contents of data after this line is complete is '2 1'
        data = input()

        # This is going to sadly be *magic* code at this stage. 
        # This line *splits* the string ('2 1' in this case)
        # into separate smaller strings. The split happens on space characters 
        # The result is a *list* of the split string (['2', '1'] in our example)
        # We then overwrite the contents of data with this result (['2', '1'])
        data = data.split()

        # Now data is a *list*. To access data from the list at a specific location
        # We just *index* the list at the desired location: data[location]
        # HOWEVER, computer scientists are weird and like to start counting at 0
        # So, when we say data[1], we are actually getting the string '1' from data
        # data[0] would give us '2' in this case (weird, I know, but deal with it)
        carrots = data[1]

        # Now we just print out what we stored in carrots
        print(carrots)
      
           
      
Back to Not Kattis
==================

1.  Seriously, look at the above code and take your time to understand it. 

2.  Go back to Colab and play around with the input function. Try different things with it. The best way to learn this stuff is to play around with the code and see what you can do with it. 

3.  To make sure you get ``input``, write some code to ask the user for their first name. Then after that, write the code to ask the user for their last name. Then, after the 2nd input, print out the first name and then the last name. **Hint:** you'll probably need variables here. 
    

More Kattis Problems
====================
Do not worry if you do not get this far. 

Grab a scrap piece of paper to start scratching your ideas down on paper.

20. https://open.kattis.com/problems/r2 (IO might be tricky, but should be similar to above so definitely try to re-use the code)
21. https://open.kattis.com/problems/faktor (IO might be tricky, but should be similar to above)   
22. https://open.kattis.com/problems/ladder (Hope you remember your Gr 10 math... if not, good thing Google exists)
23. https://open.kattis.com/problems/planina (Looks like an INTEGER SEQUENCE (if only there was an *On-line encyclopedia*).




