# Python scripts in VS Code 

So far we have mostly been using Jupyter notebooks, with a few examples of importing functions using `*.py` files. However, it is important to recognize that Jupyter notebooks are not the only way to run Python code. With your MUDE setup of conda and VS Code it is very easy to execute the contents of a `*.py` file directly, with output being generated in the command line interface. This workflow is called scripting and the contents of the `*.py` files are referred to as scripts.

## Task 1 Execute python script from VS Code
Try running a script by opening `script.py` in the editor and clicking the triangular `Run Python files` button in the top right corner. You should see a simple message printed in the Command Line Interface (CLI), e.g., cmd if you are using Windows.

## Task 2 Execute python script from CLI
You can also execute python script from the CLI (either from the terminal in VS code or any terminal). Make sure you are in the correct directory.

```
conda activate mude-base
```

This makes sure you run python from the correct conda environment. After that you can execute files with:

```
python script.py
```

Note that if you get stuck in the Python interpreter in your CLI, you can type `exit()` to get back to the native CLI prompt.

## Task 3 Create your own python script
Create a new file called `my_first_script.py` and add the following code. Complete it by filling in the missing parts:

```python
import numpy as np

def nerdy_computation(x):
    """Returns the sum of the squares of the first x natural numbers using numpy."""
    # YOUR CODE HERE
    return # YOUR CODE HERE

print("Hello MUDE! Let's compute something nerdy:")
result = nerdy_computation(10)
print(f"The sum of the squares of the first 10 natural numbers is {result}")
```

> By Tom van Woudenberg, Delft University of Technology. CC BY 4.0, more info [on the Credits page of Workbook](https://mude.citg.tudelft.nl/workbook-2025/credits.html).
