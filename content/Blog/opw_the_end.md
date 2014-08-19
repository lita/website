Title: The End of my Internship!
Date: 2014-08-18 09:00
Tags: opw, internship, python
Slug: opw_the_end
Authors: Lita Cho
Summary: Reflections on my internship. I go into what I learned and give advice for future OPW interns.

I can't believe it. My internship is over! I feel like I learned a lot and have so much things to do in order to wrap up. There is so much left to do!

Here I am going to write about my experience during OPW and share what I learned. I also want to give advice to people who are considering doing this program.

#What I learned
### I can pick up a Python ticket and start working on it
I am fully comfortable picking up a ticket from bugs.python.org, submitting a patch, receiving feedback, and having it committed. I've submitted two big patches now. One is writing a shit ton of unit tests for the [turtle](https://docs.python.org/3.5/library/turtle.html) module, since none existed. The other was adding two big features in [turtledemo](https://docs.python.org/3/library/turtle.html#demo-scripts), a GUI which shows you some cool examples of what you can do with turtle. I made it so that you can adjust the separator between the canvas window and the text window. I also added a feature where you can adjust the font size of the text within the demo.

###I'm not afraid of navigating through big code bases and reading code.
I am surprised how much of a better programmer I've become just by reading the source code of Python's standard libraries. I learned about [Mixins](http://en.wikipedia.org/wiki/Mixin), a whole slew of modules I never knew existed before ([mock](https://docs.python.org/3/library/unittest.mock.html), [importlib](https://docs.python.org/3/library/importlib.html), [smtplib](https://docs.python.org/3/library/smtplib.html), [turtle](https://docs.python.org/3.5/library/turtle.html), [tkinter](https://docs.python.org/3/library/tkinter.html) just to name a few), and how to dynamically generate code using [exec](https://docs.python.org/3/library/functions.html#exec).

### Developing for other operating systems.
I learned to be aware of testing for different operating systems, like Windows or different flavors of Linux. Most of this came from adding new GUI features to the [IDLE](https://docs.python.org/3/library/idlelib.html). Mac OS X also has a lot of special case hacks for focusing on certain GUI windows when a program launches due to the nature of Cocoa.

### Open source code isn't perfect!!!
I thought you had to be this experience, hardcore, programmer to contribute to Python. I also thought that Python would be very elegant, and I wouldn't get anything committed.

I was so wrong.

I saw a lot of beautiful code, but I also saw some nasty code. Python also has tons of legacy code that needs to be cleaned up. Thus, I feel like anyone can contribute as long as they are willing to put in the time. Your code doesn't need to be perfect either. It is definitely an iterative processes. However, if you contribute, you will learn a lot from code reviews. The core contributors tries keep the bar high and to do what's right. But hacky code gets through sometimes due to practical reasons.

###Working remotely is not for me
I really missed having an office and talking with coworkers. Working at home is hard for me, as it is quite lonely. I also feel like I would get distracted a lot easier. I would also not be good about setting "work hours", as sometimes I would be working till 3am. Sometimes, it was good as I was on a roll with a feature/bug and got it done. Sometimes, I was working on the weekends because I ended up beige watching Orange is the New Black,  and I needed to make up the hours. However, being able to work while waiting in line for Comic-Con panels was pretty awesome. Thanks to the free wifi provided by Teen Wolf, I was surprisingly productive.

I have some tips about working remotely further down the blog post.

#What could have been better
###Communication
I feel like I could have been better communicating. I was expected to write daily emails of what I was doing, and that was hard to get in the routine. There were some weeks where I was super good about it, but some weeks I didn't write it at all. I should have built good habits early on.

###Maybe have more than one mentor
My mentor is a super busy person. She is preparing so many talks for different PyCons, working a full-time job, and volunteering as the director of the Software Python Foundation. Thus, there would be times where it would take awhile before she responded to me. I feel like I would be bothering her if I tried to talk to her outside our weekly meetings. This was probably all in my head.

It would have been super awesome if there were a group of people I was introduced to in the beginning where I can go to for questions. I totally found that once I started working on tickets. I quickly found out that the python-dev IRC channel is usually dead and mailing lists were the way to go. Python has a specific mailing list for beginners trying to contribute, called core-mentorship@python.org, that is super active. I found a lot of my answers there. But I can see some interns struggling to find out where they can ask questions, as every open source community is different.

##Advice for future OPW Interns
###Be picky when choosing your project
To make the most of your internship, you should be excited about the project. You are also trying to gain skills you currently don't have. There is SO MUCH to learn out there. Thus, even before applying, I would make a list of what skills I want to gain and what projects would fit that.

###When applying, talk to your potential mentor
Your mentor is going to be one of the biggest factors that affects your experience during the internship. Thus, you should make sure you get along! If I were to do it all over again, I would list out the top three projects I want to apply for, and contact the mentors. Ask them questions about what they look for when picking interns. I would also ask what their working styles are like and see if it matches yours. Do you need someone who is charismatic and contacts you every other day, or are you the proactive type? Maybe you are an experience developer and can get things done on your own. Then maybe a really chill mentor who meets with you once a week will be better suited for you.

###When submitting your first patch, see if the community is right for you!
As mentioned before, the Python IRC channel is not super active compared to other open source communities like Rust. Also, getting your patched reviewed takes awhile as there are a lot of patches to go through and not enough contributors. Most patches I submitted have been split out to be really small, incremental changes.

If you were to go to a younger project, you could work on huge changes! It also might be the wild west, where things are changing all the time. Also, documentation might be really bad or non-existent. So setting up you dev environment might be a challenge. A more mature project might have well written docs and tutorials to help you get started.

###During OPW, don't stay quiet when you get stuck!!
I know I was told this right before my internship, but I still think I could have been better about it. If you get stuck, allow yourself 20 minutes before seeking help. Sometimes, your mentor might take longer to respond, you can work on something else while you are waiting feedback.

Also the biggest thing I learned was representing a problem in an efficient way. If I am working on big project, I can make a [gist](https://gist.github.com/) of the problem area, rather than pointing to the whole huge file.

###You can find help from other core contributors
It was super useful trying to find the key contributor of a particular module and asking for advice. I feel like most of my code reviews have been completed by other contributors rather than my mentor. If your mentor is busy, try to find someone else within the community to guide you. Not question/patch review needs to go through your mentor.

###Don't apply for jobs during your internship.
I started to apply for jobs midway through my internship as I wanted to have something lined up right afterwards. However, I feel like this was a big mistake. Some companies wanted me to do homework, which was a big pain. Going on site to meet with companies is a huge time suck.  Once I started getting offers, companies wanted to decide right away. I feel like overall, job searching was a distraction, and I should have waited. If you have the ability to wait, do it! If you really need to start applying to jobs during your internship, manage your time and try not to get burnt out.

###Even though you are making small changes, you are learning a lot.
I really liked that I started off fixing bugs and doing documentation to learn the source code. During the first month, I thought I making any impact. But when I look back through my tickets, I closed out a lot. I was pairing with a friend, and we were debugging a small turtle bug together. He eventually got stuck, and I ended up taking the driver seat. I was shocked how quickly I was able to find the bug. It was because I spent so much time unit-testing and reading the turtle source code that I was able to find it so quickly.

###Tips on working remotely
I've learned some tips both from my experience and my Remote Support Group, which is Hacker School's Zulip stream, and I thought I share them with future OPW interns.

####Find a friend who is also working remotely, and work over their house!
I didn't realize how many friends I have that are working remotely in San Francisco. I took this advice from the Remote Support Group and worked out of a friends house, and it was super fun!

####Don't be afraid to ask for wifi information!
In San Mateo, I ended up working out of boba shops a lot, as there are tons of them. They didn't advertise they had free wifi. However, I did notice their network on my phone. I decided to ask if I could use their wifi and they were really nice about giving me their wifi information! Your mileage may vary, but it is worth a shot, especially if you don't like crowded places! Remember to always buy something if you are using their wifi!

####Public Libraries
Public libraries are also a great place to work. It is super quiet, and their wifi is truly free! No need to by coffee or anything! Some cities have better libraries than others. If you live in the Bay Area, Mountain View's library is SUPER nice.

####Ask your mentor, or other mentors from different projects in your area, for coworking places!
[Sumana Harihareswara](http://www.harihareswara.net/ces.shtml), the mentor for the Wikimedia project, gave me a [list of co-working places in San Francisco](http://wiki.coworking.org/w/page/16583935/SanFranciscoCoworking). She is really awesome, and I would highly recommend reading her blog! 

####Find other OPW interns in your area and work together!
I wish I had done this. There were 3 people in OPW that were based out of San Francisco. I would have loved to organize a co-working space somewhere and worked together.

####If you have to work at your house, talk a walk before starting your "work day"
[Maja Z. Frydrychowicz](http://www.majazf.ca/blog/) came up with this one. She recommended taking a walk for 10 minutes to reset your brain so that when you enter your room, you have the mindset of entering a working space rather than your room. Then when you are done for the day, take another walk so you can reset your brain and your desk becomes your home again. I haven't tried this as I kept going to different coffee shops, but I wanted to share to see if it would work for other people.

####Ask to work out of company's workspace.
I was lucky, and I got to work out of Dropbox once a week. I also have a lot of friends who work at tech companies, and they were able to let me work at an empty desk in their office once in awhile. So definitely ask around! Worse case, they will say no.

I definitely don't want to stop contributing to Python after this internship. OPW definitely gave me the foundation I need to contribute to Open Source.