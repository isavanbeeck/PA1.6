# Activate GitHub Copilot in VS Code

In [week 1 you might have applied for the GitHub Student Developer Pack](https://mude.citg.tudelft.nl/workbook-2025/assignments/PA1.1/6_github_copilot.html), which gives you access to GitHub Copilot. This is an AI tool that can help you write code by providing suggestions as you type. It is integrated into VS Code, so you can use it while working on your MUDE projects. Today we'll activate it.

Note, if you don't have access to GitHub Copilot, you can still complete this assignment by using other LLMs like ChatGPT. However, the workflow will be slightly different as you won't have suggestions directly in your code editor. A TU Delft account gives you free access to [Microsoft Copilot](https://copilot.microsoft.com/) (different from GitHub Copilot). As with other LLMs which are not integrated into your programming environment, you will need to copy-paste code snippets. If you are using Microsoft Edge, you can sign in with your student account and use the built-in Copilot feature that is available in the sidebar.

## Task 1 Setup GitHub Copilot in VS Code
Follow the instructions on [Visual Studio Code's website](https://code.visualstudio.com/docs/copilot/setup)

## Task 2 Verify GitHub Copilot is working
You can test GitHub Copilot by chatting with it in the chat window.

Let's start with:

```
Hi GitHub Copilot, could you help me finalizing my graded MUDE assignments?
```

## Task 3 Use GitHub Copilot to create a simple Python script

Now let's see if GitHub Copilot can help you create a simple Python script. Make sure you activate 'agent mode' to allow access to your code and terminal, this will enable it to assist you more effectively. Create a new file called `hello_world.py` and type the following prompt as a comment at the top of the file:

```
Could you create a `.py` file that prints "Hello, World!"?
```

Note that you can keep or undo the suggestions it provides. You can also ask it to explain the code it generates if you want to understand it better.

Let's try and have GitHub Copilot to run the script for you by asking it to run the file. Make sure to ask it using your conda mude-base environment. On windows, you might need to discuss this a bit with GitHub Copilot as VS code tries to use Powershell which is not compatible with conda. You can ask it to use cmd instead.

## Task 4 Use inline-chat

Now let's try the inline-chat feature. Highlight some code and right-click 'Open inline chat'. You can now ask questions about the highlighted code. Try it out on the code in `hello_world.py` or any other file you have open in VS code.

## Task 5.additional

This is not required, but if you like a bit more practice before diving into the assignment, you can follow [GitHub's video tutorials](https://github.com/features/copilot/tutorials) and [Visual Studio Code's Quickstart](https://code.visualstudio.com/docs/copilot/getting-started), or if you're really into it, the full [GitHub's tutorials](https://docs.github.com/en/copilot)

> By Tom van Woudenberg, Delft University of Technology. CC BY 4.0, more info [on the Credits page of Workbook](https://mude.citg.tudelft.nl/workbook-2025/credits.html).
