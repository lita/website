Title: 2 Weeks into Hacker School! Progress on my Bittorrent Client
Date: 2014-02-24 02:56
Tags: bittorrent, hacker school
Slug: 2-weeks-into-hacker-school-progress-on-my-bittorrent-client

Wow! I can't believe two weeks has gone by! I feel like I am learning a
lot, but not learning enough. At the end of the day, I always want to
code more. It is so hard to focus on your projects while at Hacker
School though. There is SO much to do! So many interesting workshops and
so many people to do [pair-programming][pair-programming] with! In order to make time
for this project, I ended up staying late or coding over the weekend. I
actually like this schedule, but we'll see how long I can keep it up.

Bittorrent Client {.wsite-content-title style="text-align: left;"}
-----------------

GREAT NEWS! I am now able to download files from Bittorrent network
using a tracker file. Unfortunately, all the data lives in RAM until I
download all the pieces, so it is limited. I also can't upload files to
other peers. I have been mostly testing my client on music files with no
peers, only seeds. But hey! It's a start.   
  
I couldn't have done it without Kristen Widman's blog posts, who is also
a former Hacker Schooler!  
  
[How to Write a Bittorrent Client: Part 1][bt1]  
[How to Write a Bittorrent Client: Part 2][bt2]
  
Thank you SO much Kristen for writing this tutorial! Without it, it
would have taken me forever to get to where I am now.  
  
What I Learned:  
  
1. Refactoring code is hard.   
The Bittorrent Client is great for having small goals. However, at some
point, you reach a step and you realize you need to rewrite and organize
your code in order to move on. Adding more abstractions, get rid of
duplicate code, making it more object-orientated... it's a part of
life!   
  
2. Designing and structuring code can be a time suck.   
Many times, I would just sit at my desk, wondering how I should go about
organizing my code when I really had no idea what the Bittorrent
specification was talking about. Then I would read someone else's
implementation and get confused even more. Should I make a Piece class
because someone else did? Should I make a Message class for each Message
code? This was getting in the way of me learning. In the end, I ended up
hard coding the bytes and sending it to a Peer to see what happened.
This helped me tremendously to figure out how the protocol works, and
then designed around that. How are you suppose to design something if
you don't understand the specifications?  
  
3. Wireshark is awesome, especially for learning and debugging.  
I never really used Wireshark till this project, and IT IS F\*CKING
AWESOME. Many thanks to Alan, a Hacker School Facilitator, for showing
me how it works!  
  
4. Don't look at other people's code too early on.  
I feel like I got really scared of this project by looking at BitTorando
and other Hacker Schooler's Bittorrent implementations. But I am glad it
didn't deter me. I ended up writing it my own way.  
  
Future Steps:  

-   Make it so that my program can upload files as well as download.
-   Make it handle multiple peers, either with Twisted or writing my own
    event loop. (If I go with writing my own event loop, I should
    probably make it multi-threaded. But that is another beast)
-   Make it so that all the pieces don't live in RAM, but stored on disk
    if the file is too big. (Can't download 8GB files at the moment...)

Even after my skepticism, I have to say that this project was really
cool. You have these small little goals that build up to a big software
project. Try connecting to the tracker server, and getting ip address
back. Then try to connect to one peer and send a handshake and so
forth.  
  
I was running around when I was able to download an album and play it on
my computer. I can't believe I wrote software to do that!   
  
MANY THANKS TO ALAN AND TOM, my two WONDERFUL facilitators at Hacker
School! This couldn't have happened without your enthusiasm for writing
Bittorrent Clients!  
  
Even though this project was great, I want to try making a full stack
web app. Lets see how that goes!
    
[bt1]: http://www.kristenwidman.com/blog/how-to-write-a-bittorrent-client-part-1/
[bt2]: http://www.kristenwidman.com/blog/how-to-write-a-bittorrent-client-part-2/
[pair-programming]: https://www.hackerschool.com/manual#sec-pairing
