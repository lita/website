Title: Fun with Python and pip!
Date: 2014-03-22 
Tags: python, hacker school
Slug: pip-freeze

I have been programming in Python for quite awhile now. However, I am still
learning new things all the time about this language! I was able to download the
source code for CPython and learn a lot about the internals! I even committed
TWO patches to the CPython!

David, a fellow Hacker Schooler, showed me a cool way to list out all my
dependences in my Python project! This is very useful for people who what to run
my Python project.

`pip freeze > requirements.txt`

The command, pip freeze, prints out all the required modules that need to be
downloaded to run my project. I write that out to a text file
('requirements.txt') and save that to my project.

Then if someone wants to run my program, rather than me listing out my modules
in a README or them looking at my code for the modules, all they need to do is
run

`pip install -r requirements.txt`

and pip installs everything for you!!! How cool is that? Now all my friends who
are reviewing my code won't complain about how hard my projects are to setup!

I had no idea pip was so powerful! `pip list -e` lists all the out-dated
libraries you have in your project, `pip search <query>` searches the PyPi
libraries for modules! I need to learn more about the program!

I am working on this HUGE blog post about Databases. But it needs to be proof-
read and refined. Hopefully I get that out soon!

