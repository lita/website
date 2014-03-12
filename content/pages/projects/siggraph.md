Title: SIGGRAPH

Interactive Simulation of Surgical Needle Insertion and Steering
=====

I co-wrote a real-time renderer for a graduate student, who was developing a software that simulates how tissue deforms when a needle is inserted (also in real-time). I ended up using Ogre API, which is an open-sourced game engine, to develop the renderer. My work got me an authorship on a SIGGRAPH paper in 2009, which is the highest publication for computer graphics.

The renderer couldn't use very much CPU power, since all the CPU resources were going to the simulator. We had to use the GPU as much as possible in order for the program to run in real-time.

[SIGGRAPH Paper through UC Berkeley's Graphics Group][sig] 

You can watch the renderer in action in the video below! 

<iframe style='width: 450px; height: 300px;' src="//www.youtube.com/embed/y0Fq0bmEmc4?wmode=opaque" frameborder="0" allowfullscreen=""></iframe>

<br></br>

<iframe style='width: 450px; height: 300px;' src="//www.youtube.com/embed/WiGVieW2tk8?wmode=opaque" frameborder="0" allowfullscreen=""></iframe>

<br></br>

[sig]: http://graphics.berkeley.edu/papers/Chentanez-ISN-2009-08/

