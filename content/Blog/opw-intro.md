Title: OPW and Tkinter!
Date: 2014-5-29 16:18
Tags: opw, python, tkinter
Slug: opw-intro
Authors: Alexis Metaireau, Conan Doyle
Summary: Describing my first day at OPW working on CPython and Turtle


After Hacker School, I got accepted to the GNOME: Outreach Program for Women (OPW), where I get to spend a summer working on CPython with none other than [Jessica Mckellar][id]. For the next three months, I'm working on making GUIs better in Python. 

It has been a week and half already, and so far I am getting my hands dirty by fixing bugs and code reviewing other people's patches. 

For this blog post, I thought I'd talk about Tkinter, the GUI module in Python, and how to start using it! 

Note: All the following examples will only work with Python 3. I'm moving on! GOOD-BYE PYTHON 2.7!!

In GUI programming, I like to think of the GUI as a tree or a graph. The root is your main GUI window, and within it contains different elements (Labels, Buttons, Images, TextBoxes, etc. Also known as Widgets), which are your children to your tree.

Let's start with Hello World. Python is cool because I can interactively mess with a module using the interpreter.

```python
>>> import tkinter as tk
>>> root = tk.Tk()
```
Notice that a window pops up! Yay, that is your root GUI window with nothing in it! Don't close this window! This will destroy the root GUI object, and you won't be able to get it back! If you did, no big deal, just instantiate another one.

Let's add a label with the word, "Hello World!"

```python
>>> w  = tk.Label(root, text="Hello, World!")
```
Wait, what? Nothing has happened... what is going on here? Where is my label?

Lets briefly go over Geometry Managers! Geometry Managers manage where widgets should go within their parent. They determine the placement of the widgets they are in charge of. There are different kinds of Geometry Managers within Tkinter. However, the most popular one is called "The Packer". The Packer sets the size of a widget by determining the size of it's children first and packing it closely together. You can put frames and padding to get the look you desire, but ultimately, your window is going to packed to the minimal size by default.

We haven't specified what type of geometry manager to use. Let's go ahead and use "The Packer" as our geometry manager! It is super easy! All we need to do is call the `pack()` method.

```python
>>> w.pack()
```

Yes! Our widget shows up! We can pass in settings to `pack` method. These settings adjust where the widget is going to appear within its container, and how it will behave when the main application window is resized. Lets try put another Label.

```python
>>> x  = tk.Label(root, text="Hello, World!")
>>> x.pack()
```

By default, the packer sets the widgets on top of each other as the window expands. However, we can change this!

```python
>>> x.pack(side='left')
```
If you didn't expand your window, then the text didn't change. However, if you expand the window, one of the labels stays on the top, while the other goes toward to the left! There are other settings, which you can find in the [Tkinter documentation.][tk]

Lets add a button that generates more labels!

```python
>>> def addCats(root):
...    x = tk.Label(root, text="MOAR CATS")
...    x.pack()
>>> button = tk.Button(root, text="CATS", command=lambda:addCats(root))
>>> button.pack()
```

Woah! There is a lot going on here! `addCats` generates more labels. When we create a Button widget, we need to give it a function that will be called when the button gets clicked. However, you can't pass it any elements. HIGHER ORDER FUNCTIONS TO THE RESCUE! Since we want to pass in the root always, we can create a lambda function that will return a function with root applied to it. We could also use the partial module as well:

```python
from functools import partial

addCats_root = partial(addCats, root)
button = tk.Button(root, text="CATS", command=partial)
```

Okay, so we made quiet a mess here. I don't know about you, but this is what my GUI looks like:

<img src="/images/tk.png" style="width: 20%; height: 20%"/>​

Lets add a button that quits the GUI and destroys all the widgets properly!

```python
>>> button = tk.Button(text="QUIT", command=root.destroy)
>>> button.pack()
```
Now a QUIT button should appear, and when you press it, the window should close! Your root object is no longer available to play with though! You will need to create a new Tk object. 

But it was fun just playing around the Tkinter module in the interpreter. Whenever I got into a weird state, I would just destroy the root and start over.

## Unit testing in Tkinter
I am going through how the Python project runs their unit tests, and it is pretty impressive. They have test modules in Lib/test folder. For Tkinter, the test modules are test_ttk_guionly.py, test_ttk_textonly.py and test_tk.py. However, these modules call other test modules within the Lib/tkinter/test module. These modules test individual GUI objects by creating them and checking the hard values in the widget. 

However, [not all the Tkinter tests run successfully on Mac OS X][bug]. So I have to run them on Ubuntu, which is a bummer. 

I learned the hard way that once you close the window or call `root.destory()`, that object is gone forever and you need to instantiate the object again to get a new one. [I was trying to run the same set of tests for a GUI object with a different setting within the same module.][unittest] However, the testing suite uses the same root widget for all the test run from each module, then destroys the root widget. So when I tried to run the tests again from that module, I couldn't because the root widget was destroyed from the previous time it ran.

I had to make a completely separate testing module with that setting change, which seemed kind of bloated to me.

Anyway, I am still a beginner to Tkinter and Turtle modules. Turtle seems like a awesome module to play with. I will be telling you more about that next time!

[tk]: https://docs.python.org/3.4/library/tkinter.html
[id]: https://twitter.com/jessicamckellar
[bug]: http://bugs.python.org/issue17496
[unittest]: http://bugs.python.org/issue21585