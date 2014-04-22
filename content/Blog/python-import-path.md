Title: Path Module
Date: 2014-04-13
Slug: path-and-import
Tags: python, hacker school, path module, previous life

In order to take a break from making Flask apps, my Bittorrent client, messing with various databases, and reading HTTP protocol documentation, I wanted to write about Python, something I know.

While working at Dreamworks Animation, my favorite module was the "path" module. This is a 3rd party module dealing with file paths. It makes paths as first class objects, allowing you to do some common operations on them.  We had our own version at Dreamworks, which hooks into our proprietary software. But path.py is still useful by itself. This is way better than using os.path. Hopefully, after this blog post, you will never use os.path... ever.

You might think module sounds boring. I mean, file directories... really? Well, when you are working with hundreds of thousands of images (30 frames in a second, 90 minutes in an animated film, so we are talking 30 x 60 x 90=162,000 images for an entire movie, not including composite layers that make up one image), this module is a godsend. We were constantly renaming, deleting, copying and moving files all over the place. Most of the marketing tasks were frankensteining some frames together in order to meet deadlines. 

But you can use this module in everyday tasks! Like cleaning up unnecessary data or making a script to rename some music files in Python! Here are some examples of using this module! If you are following along, please start in an empty directory.

First lets install this module.

```
pip install path.py
```

Okay, time to start playing with it!

```
from path import path

root = path('.')
```
This will create a path object that is pointed to your current directory! One of my favorite features is how easy and readable it is to append directories to the path. For example, you can do this!

```
In [18]: t = root / "test" / "a" / "long" / "directory" / "tree"
In [19]: print t
test/a/long/directory/tree 
```
How awesome is that?? You can even ask if the directory exists or not. 

```
In [20]: t.exists()
Out[20]: False
```
Lets go ahead and make this directory!
```
In [24]: t.makedirs()
In [25]: t.exists()
Out[25]: True
```
How easy was that?! You can also give it permissions with the `mode` flag! By default, permissions is set to 511.

Let's make a lot of directories!

```
import random

def make_fake_directories(root):
    for i in range(10):
        s = root / str(i)
        for i in range(random.randint(0,10)):
            s = s / str(i)
        s.makedirs()

make_fake_directories(root)
```
This function creates 10 directories with random directory depth, within a range from 0 to 10. Lets see if this worked

```
In [26]: root.dirs()
Out[26]: 
[path(u"./0"),
 path(u"./1"),
 path(u"./2"),
 path(u"./3"),
 path(u"./4"),
 path(u"./5"),
 path(u"./6"),
 path(u"./7"),
 path(u"./8"),
 path(u"./9"),
 path(u"./env"),
 path(u"./plugins"),
 path(u"./test")]
```
Lets create a file at the end of directory depth!
```
for dir in root.walkdirs():
    if not dir.dirs():
        file =  dir / "myfile"
        file.touch()
```
`walkdirs` returns a generator that iterates through your directory structure until you've looked at every folder. It is basically doing in-order traversal. 

We can use `walkfiles` to see if we created the necessary files!
```
In [117]: for files in root.walkfiles():
   .....:     print files
   .....:     
./3/myfile
./4/0/1/2/3/4/5/6/7/myfile
./5/0/1/2/3/4/myfile
./6/0/myfile
./7/0/1/myfile
./8/0/1/2/3/4/5/6/myfile
./9/0/1/2/3/4/5/6/7/8/myfile
./0/0/1/2/3/4/5/myfile
./1/0/1/myfile
./2/0/1/2/3/4/5/6/7/myfile
```
Okay, lets try to rename my numbered directories into letters! Just because we can. 

```
def renameDirs(root):
    for dir in root.dirs():
        if dir.name.isdigit():
            if dir.dirs():
                renameDirs(dir)
            parent, d = dir.splitpath()
            dir.rename(parent / chr(ord('a') + int(dir.name)))

renameDirs(root)
```
Woah! A lot of stuff going on here! I wrote a lot of these little recursive functions a lot, but you can do the same thing as `walkdirs`. Basically, I loop over all the directories in the current directory, and check to see if they have any directories. If so, I recurse. When the function returns, I rename the directory to the ASCII equivalent by using `ord`. The `rename` path is a little tricky, as it needs the full path from where your Python module is running from. That is why I call `splitpath` in order to get the parent directory. Now, we have folders like this!

```
a/       b/       c/       d/       e/       f/       g/       h/       i/       j/  
```

Now we have a directory structure like this! (Note: I shorten the results for brevity.)

```
./a
./a/a
./a/a/b
./a/a/b/c
./a/a/b/c/d
./a/a/b/c/d/e
./a/a/b/c/d/e/f
./b
./b/a
./b/a/b
./c
./c/a
./c/a/b
./c/a/b/c
./c/a/b/c/d
./c/a/b/c/d/e
./c/a/b/c/d/e/f
./c/a/b/c/d/e/f/g
./c/a/b/c/d/e/f/g/h
./d
./e
./e/a
...
```
So now that we are done testing, time to delete these useless directories! 

```
for dir in root.dirs():
    dir.rmtree()
```
This will delete the entire directory tree of the current folder. How cool is that? Don't run this if you have any import files or directories in your root folder!!!

Now that you know the basics, check out this blog about how to write a script a clean-up script for your website!

[Python 101: Writing a cleanup script][clean]

[clean]:http://freepythontips.wordpress.com/2014/01/23/python-101-writing-a-cleanup-script/

Happy scripting!


