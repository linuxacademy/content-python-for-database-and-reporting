# Lesson Title

Using and Evaluating Both Code and Markdown Cells

## Description

**Note: The Playground Server must have started Jupyter Notebook server and your local machine must be connected as described in _Installing Jupyter Notebooks, Opening a Notebook, and Setting the Kernel, Part 3_.**

### Cells

0. Jupyter Notebooks are composed of cells.  The two types of cells we will use will be `code` and `markdown`.  Cells can be any size and the information in a `code` cell is available to all cells below it.

#### `Markdown` Cells

1. Start a new notebook by selecting the `New` dropdown near the top on the right and then select `Python 3`.

1. In the first cell of the notebook, set it's cell type to `Markdown`.  Then paste the following into the cell.

    ``` text
    # Markdown Cell

    - It is designed to allow for text explanations
    - Can be used to create intricate layout including tables with extra packages
    - Can create ordered and unordered lists
    - Can create code snippets
    - This is the *[Markdown Guide](https://www.markdownguide.org)*.
    ```

1. Evaluate the cell by selecting shift-return. You can click the link in the above cell to get more information about writing in Markdown.  Notice that the rendered Markdown replaces the text you entered.  You can click on the cell to return to the markdown text, make changes, and re-evaulate.

#### `Code` Cells

1. `Code` cells evaluate the text added to it by the language selected as the `Kernal.`  In this case `Python 3`.

2. In a `code` cell use python and a for loop to print the numbers 0 - 4.

    ``` python
    for i in range(5):
        print(i)
    ```

3. Now evaluate the cell, exactly like you did with the `markdown` cell.  Notice that the output for a code cell is displayed directly below it.

4. Now have the cell print 0 - 10, by changing the value in `range` and re-evaluating the cell.  _Don't forget python indexes starting at 0 and range does ends at the last value and does not process it._

5. In a new `code` cell, enter the following:

    ``` python
    a = 'apples'
    b = 'bananas'
    x = 8
    y = -23
    ```

    **Before evaluating the cell think about these two questions.**

      1. What is going to be the result of evaluating this cell?
      1. What will be the output?

1. Now evaluate the cell.  Were you surprised by the output?  There was no output because all the cell does is assign values to variables. There are no print statements or return statements.

1. In a new `code` cell, print the variables we just assinged in the previous cell.

    ``` python
    print(f"a = {a}")
    print(f"b = {b}")
    print(f"x = {x}")
    print(f"y = {y}")
    ```

1. In a new `code` cell:

    ``` python
    print(f"x * a = {a*x}")
    ```

1. Now we are going to examine the changes made in cells before the one we are looking at. In the cell where variables were assigned change `a = "apples"` to `a = "pears"`.  Don't forget to re-evaluate the cell.

    **Consider the follwoing questions:**
    1. Why were the cells after this cell not changed?  
    1. What is the value of `a`?
    1. What will happen if we re-evaluate the cell where be multiply `a` and `x`, but not the cell where we print the value of `a`?

1. Re-evaluate the cell where `a` and `x` are multiplied.  Did the cell where the value of `a` was printed change?

1. Examine the selections under `Cell` dropdown.  Do you see an easier way to make a change at the top of the notebook and have it propagate through all the cells?  
    _Hint: Run All Below_

1. In a cell at the end of the notebook enter the following code block.  This will import the math module so we can use square root and then defines a function to take the square root of any number provided.

    ``` python
    import math

    def get_sqr_root(x):
      return print(f"The square root of {x} is {math.sqrt(x)}")
    ```

1. Now in a new cell evaluate the square root of 16.

    ``` python
    get_sqr_root(16)
    ```

1. In a cell below that evaluate the square root of 100.

1. Finally, using the `Insert` dropdown menu, insert a cell before the cell where we multiplied `a` with `x`. In this new cell determine the square root of 25.
    - How can the function work before it is defined?  
    - _**PLEASE NOTE: THIS IS NOT GOOD PRACTICE!**_

## Tags

`Using Python for Data Management and Reporting` `python` `jupyter notebooks` `centos 7` `pyenv` `pipenv` `markdown`

## Video
