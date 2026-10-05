# Programming assignment 1.6: BotHeat.py

You can preview the instructions of this assignment on https://mude.citg.tudelft.nl/workbook-2026/assignments/PA1.6/README.html. After the deadline, this link will include solutions. The preview without solutions will remain available here: https://mude.citg.tudelft.nl/workbook-2026/no_solutions/assignments/PA1.6/README.html. All files of an assignment can be downloaded as [`.zip`-file](https://mude.citg.tudelft.nl/workbook-2026/_custom_downloads/assignments/PA1.6/all_files_PA_1_6.zip) to your computer.

To activate autograding, create a new repository on github from this template repository https://github.com/MUDE-2026/PA1.6_template and push your work to the assignment branch.

Before you can start this assignment, read the theory pages in the book chapter [Large language models](https://mude.citg.tudelft.nl/book/2026/programming/week_1_6.html):
- [Effective prompting](https://mude.citg.tudelft.nl/book/2026/programming/week_1_5/effective-prompting.html)
- [Generating code exercise](https://mude.citg.tudelft.nl/book/2026/programming/week_1_5/generating-code.html)
- [Debugging errors exercise](https://mude.citg.tudelft.nl/book/2026/programming/week_1_5/debugging-errors.html)
- [The importance of human-in-the-loop](https://mude.citg.tudelft.nl/book/2026/programming/week_1_5/human-in-the-loop.html)

In this assignment you’ll make exercises on the following topics:

- Python in `.py` files
    - [Python scripts in VS Code](./1_py_files.md)
- Coding with AI in VS code.
    - [Activate GitHub Copilot in VS Code](./2_activate_github_copilot.md)
    - [Programming a Thermostat with AI](./3_LLMs_in_Practice.md). Beware, the third assignment can be a bit of a challenge. But try to co-program with GitHub Copilot! There's no need to complete it fully.

The autograder checks the following aspects of your work for each push to GitHub:

- You've created a new python script called `my_first_script.py` which returns correct results
- You've completed the thermostat scripts. Note that this doesn't require you to write all code yourself, you can use GitHub Copilot to help you. Furthermore, part of it is already implemented, and not all missing parts of the package are required to be completed
  - The onoff controller works correctly:
    - Turns heating on when the temperature drops below the lower deadband limit.
    - Turns heating off when the temperature rises above the upper deadband limit.
    - Maintains the current state when the temperature is within the deadband.
    - Activates a safety cutoff and turns heating off if the temperature reaches the safety high limit.
  - The predictive on/off controller passes the following tests:
    - It turns heating off early if the predicted temperature will exceed the upper deadband limit, even if the current temperature is below the threshold.
    - It turns heating on when the temperature is falling and the predicted value will drop below the lower deadband limit.

This assignment is due on 10:45, Wednesday, October 7, 2026.

> By Tom van Woudenberg and Stanislaw Ostyk-Narbutt, Delft University of Technology. CC BY 4.0, more info [on the Credits page of Workbook](https://mude.citg.tudelft.nl/workbook-2026/credits.html).
