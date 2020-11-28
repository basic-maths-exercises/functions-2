# Passing variables

Now that you have written your first Python function you need to spend a little more time understanding how to write programs well.  The code that you have just written should have looked something like the code in `main.py`.  As you can see by writing the code this way we have reduced the number of lines from 32 to 14, which is a good thing.  There is some bad programming practise in this code, however, which I would like to highlight in this exercise so that you can try to avoid doing it in future.

The bad practice in this code is associated with the variable `xvalues`.  This variable can is used within the function even though it not been passed to it like the variables `a`, `b` and `c`.  `xvalues` is thus what is referred to as a global variable in that every part of our program (the code that is both within the function and outside the function) can access its value.  In a short program like this one using global variables is not that bad as the definition of `xvalues` appears close to the definition of the function.  If the code were much longer, however, then the definitions of these two object might be much further apart.  Having python functions that use global variables makes your code difficult to read.  You should thus avoid using global variables as much as possible. 

__With that in mind, I would like you to rewrite the quadratic function in `main.py`.__  In your new code, however, you will pass `xvalues` to `quadratic` so the first line of the definition of `quadratic` function will look like this:

````
def quadratic( xvalues, a, b, c )
````

When you then call `quadratic` to generate the y-values for the graphs you will need to pass `xvalues` from the calling code to the function.  Your function call will look like this;

````
yv = quadratic( xvalues, a, b, c )
````
