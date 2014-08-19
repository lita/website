Title: 2 weeks into internship. Mock Module and more!
Date: 2014-6-17 16:18
Tags: opw, python, tkinter
Slug: mock
Author: Lita Cho
Summary: Listing of the things I know and don't know!

I was inspired by [Julia Evan's blog][julia] post about listing what she knows and what she doesn't know, and how asking questions is a super power! I try to be good about asking questions when I don't know something, but I feel like my questions are too vague. I really want to get better at boiling my question down!

Thus, I thought I take some time to list out what I don't know, specifically about unit testing, since that is all I have been doing this week! I'm been tasked with writing unit tests for the entire Turtle module! Can you believe there isn't a single unit test for this module at all, even though it is a standard library?! It also surprises me that the Turtle module is all in one file, but that's a different story.

## What I don't know
#### GUI Testing
I am still not 100% sure how GUIs are run through unit testing. In Tkinter, it looks like the widget is initialized and test just the internal variables within the widget class. I thought they would compare pixel by pixel, checking if the GUI is the same or not. That might be because I often did that at Dreamworks for testing the renderer.

After talking with Ingrid, it looks like you can mock mouse-events by generating your own events through Tkinter. Then you pass in those events to Turtle to see how it reacts. The `mock` module would be perfect for this! More on the `mock` module later!

We are still learning as we develop our test coverage. In most cases, I create a GUI object and just test the internal state of Turtle rather than the Tkinter objects themselves. Everything seems to be coming together! As my tests run, all these GUI windows appear and disappear like I am being hacked. Soon, I can scare all my friends by running my tests on their computer! >:D

#### The test.support module
CPython has an internal module called `test.support`, which holds all the utility functions for its unit tests. It has useful features, such as `use_resource`, where you can pass along command-line flags to your unit tests. We use this a lot for Turtle/Tkinter testing, as we need to check if GUIs are enabled in our environment. Thus rather than running the check for every module, an outside program that checks if GUIs are enabled and passes a 'gui' flag to all the other GUI unit tests if it passes. If not, then a warning appears, and the GUI unit tests don't run.

However, the support module has a LOT of stuff in it that I don't know about. I really want to study it more so I know what is available to me when I write my tests.

#### The mock module
Another thing I don't know really well is the `mock` module. I definitely feel like my tests can be more robust and cleaner with this module. This module has so many features! My favorite so far is the `patch` decorator, where you can override the behavior of a function specifically for that test case. I have used it on programs that print to `stdout`. Before, I would have to override `sys.stdout` manually and make sure to set it back correctly, or my print function is borked.
```python
import unittest
import sys
from io import StringIO

def lets_print_something():
    print("Dude, I totally printed")

class TestPrinting(unittest.TestCase):
    def test_lets_print_something(self):
        sysout = sys.stdout
        sys.stdout = io = StringIO()
        lets_print_something()
        self.assertEquals(io.getvalue(), 
                          "Dude, I totally printed\n")
        sys.stdout = sysout
```
This totally felt ugly to me. It's like remembering to `close` your file objects. I never do that anymore due to the `with` statement. However, with the `patch` decorator, this test looks so much cleaner!
```python
import unittest
import sys
from io import StringIO
from unittest.mock import patch

def lets_print_something():
    print("Dude, I totally printed")

class TestPrintingMock(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_lets_print_something(self, mock_stdout):
        lets_print_something()
        self.assertEquals(mock_stdout.getvalue(),
                          "Dude, I totally printed\n")
```
The patch decorator passes a `MagicMock` object by default, but I've changed it to give me a `StringIO` object using the `new_callable` argument. The decorator will handle passing this argument in, so you don't need to pass it anything to make it run.

I just barely scratched the surface. Your unit tests don't need to create side affects! [Naftuli Tzvi Kay][rm_mock] has a great blog post about mocking in Python and how to test if your program called `rm` without generating any files!

[The Python documentation on mocking][py] is also very good. However, it is only available on 3.3 and up. You will need to `pip install mock` for earlier versions of python.

Alex Marandon also has a great blog post about [Python Mock Gotchas][gotcha]. I haven't gotten enough experience with the module where I have run into these, but I feel like it is a time saver!

This blog post has gotten way bigger than I expected. I really want to thank Amandine Lee, a fellow Hacker Schooler, about showing me the `mock` module, and her general insights regarding unit testing! Also, my fellow intern, Ingrid Cheung, for helping me with GUI testing! Together, Turtle will have better test coverage!!!

I need to write a blog post about the basics of Turtle. I hope to get to it soon!

[gotcha]: http://alexmarandon.com/articles/python_mock_gotchas/
[py]: https://docs.python.org/3.5/library/unittest.mock.html#module-unittest.mock
[rm_mock]: http://www.toptal.com/python/an-introduction-to-mocking-in-python
[julia]: http://jvns.ca/blog/2014/06/13/asking-questions-is-a-superpower/