Title: Setting Up a Pelican Blog
Date: 2014-03-16 
Tags: blog, hacker school
Slug: blog-setup

Setting up a Pelican blog was a pain. But I actually learned a lot about CSS and HTML. Right now, I am going through The Modern Web, which is giving me a lot of great tips about how to organize my website. I now know that the structure of my website is a terrible mess and I need to refactor it ASAP.

I was going to write a tutorial about how to setup a Pelican blog, but this guy did a great job of it already.

[Slok's Blog: Creating a blog with Pelican][slok]

He uses Fabric, a Python library for automation, to push his blog posts to the website. He also uses git's branching in order to handle his dev-website and his deployment website. I made my own ghetto script using 'os' commands, but now going to use fabric to clean up my blog workspace. 

[slok]:http://blog.xlarrakoetxea.org/posts/2012/10/creating-a-blog-with-pelican/