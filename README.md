# Our Vision 
### For educators, teachers, and game developers who need a more hands-on and interactive experience, LightMap is a robust image projection framework which allows one to be part of the image. Unlike current frameworks which rely on static objects, LightMap responds and interacts with moving subjects in real-time.

[LightMap Test #2](https://www.youtube.com/watch?v=L9hnyjyehlU)

[LightMap Test #1](https://www.youtube.com/watch?v=ZFFU9Q9EpU8)

[LightMap Product Backlogs](https://docs.google.com/spreadsheets/d/1KzVy8__O7hYm5OYdYDgpwn8v_2NLT_NFqykj1n62cC0/edit?usp=sharing) (note: subsequent sheets contain sprint backlogs)

[LightMap Burndown Chart](https://docs.google.com/spreadsheets/d/1Ahi36pMBZp_S9xYot1CPSjrou3HqOCyGpo3ACNAwtpA/edit?usp=sharing) (note: subsequent sheets show previous burndown charts)

[LightMap UML Diagrams](https://github.com/imlasky/LightMap/tree/master/Documentation/UML)
-----------------------------------------------------

To build from source
-----------------------------------------------------
You will need to have your computer hooked up to a projector first to properly use LightMap.
You should also be using an object thats at least the size of a basketball and is round. LightMap may not detect objects that are too small or round enough.
-----------------------------------------------------
Download project from github
	https://github.com/imlasky/LightMap.git
You will need to have python3 installed next

You will need the following packages to run LightMap

pygame
	sudo apt-get install python-pygame
opencv3
	this can sometimes be pretty tedious depending on your machine
	but here is a link http://tinyurl.com/pqp3sqk
Wand
	sudo apt-get install libmagickwand-dev

------------------------------------------------------
run LightMap.py from the command line.

A window will pop up and allow to choose the image that you want to project.

Once an image is selected, you will see a white circle slowly go from the 
top left of the pygame screen to the bottom right corner. This means that 
LightMap is calibrating the space to be used and may take a moment. You should
also keep this area clear of any people/objects.

As soon as it finishes, the screen may flash and go completely black.
It is now ready to project onto round objects such as a clock or ball.

The projection will stay on the ball as long as it is in range of the camera and
the object is not obscured.

