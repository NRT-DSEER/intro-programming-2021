# Introduction to Scientific Computing 2021 Bootcamp Materials
This repo houses data and notebooks for the 2021 DSEER "Introduction to Scientific Computing" bootcamp.

## Instructions:
0) Follow the setup instructions on [this page](https://carpentries.github.io/workshop-template/#setup) titled "The Bash Shell", "Git" and "Python". Basically, everything under "Setup" not including "R." 
      - For python, install Anaconda.
      - The videos may be helpful. 
      - These additional tutorials may also be helpful to skim:
            _Unix shell/command line:_ http://swcarpentry.github.io/shell-novice/
            _Version control with git:_ http://swcarpentry.github.io/git-novice/
1) Open Terminal or other application for the bash or zsh command line (for Windows its the git bash introduced in the instructions above, for Mac and Linux its the Terminal)
2) `cd` into a directory that you want all of your bootcamp materials to live.
3) Type `git clone https://github.com/NRT-DSEER/intro-programming-2021.git`
4) Type `cd intro-programming-2021`
5) You're all set up! To start using notebooks, type `cd notebooks` and then type `jupyter notebook` 
6) This should open a new tab in your default browser and print a bunch of stuff in your terminal.
7) In the new tab that was just opened in your browser, click the notebook for the day of the course that you are on. For the first day, open "Day1_Setup.ipynb" and follow the instructions in that notebook to make sure you followed all the steps correctly.
8) Each day, start class by going into your bootcamp repo directory (`cd intro-programming-2021`) and typing `git pull`. Then follow steps 5-7

## Directory Structure:
`data` holds data

`notebooks` holds notebooks

`output` is where you will save your own files

Don't change the structure!


# Syllabus

### Instructors:
All the instructors are also on Slack, we prefer that you send us a slack message if you have any questions over sending an email. Slack is only available for students taking the live version of the course. Please check your email for information on how to join slack.

- Amanda Farah (she/her or they/them), 3nd year graduate student, Astrophysics
- Katie Dixon (she/her), 5th year graduate student, Ecology and Evolution
- Maria D Hernandez Limon (she/her), 3nd year graduate student, Geophysical Sciences

### Teaching Assistants:
Contact over slack or attend [office hours](#office-hours) at this link:

Office Hours Zoom: 
https://uchicago.zoom.us/j/97235120674?pwd=RUlqUUNMY25SL2h2a2JvMFhMdis1Zz09
Meeting ID: 972 3512 0674   Passcode: 965225

### Class Time:
- Aug 30-Sept 17
- 10:00am-12:30pm CT 
- We will not have class on Labor Day 9/6.

### Structure:
- Instructors will go over pre-written code and discuss the mechanics of what is going on
- We will stop intermittently for skill practice and breaks 
- Any code not covered should be completed outside of class with help from TAs
- Occasional, short skill practice problems as homework 

### How to ask for help:
- Go to the office hours of any of the TAs
- If you need help outside of class time or office hours, contact one of the TAs via slack. They will respond during their office hours.
- During class, post to your slack channel and your TA will respond in real time

### Recordings:
Info on where to find the recordings.

## Week 1: Foundation 
### 1. General instruction and go over syllabus (8/30)
- Goals for the workshop/syllabus 
- Motivation
- How this course works
- How to ask for help
- Expectations
- Rules
- Growth-mindset  
- What is programming? Why python and not R?
- Directories and file structure
- Installation- Run JN
- Introduction to jupyter notebooks-the structure 30m
- Import libraries 
- Interface, running a cell
- Markdown- comments
- Error messages-learn from mistakes
- Google
- Stack overflow
- 12:00 SET-UP and installation 

### 2. Introduction to data types and storage (8/31)
- Variables
- Booleans (side note on how bits work -transistor in 0 or 1)
- Ints 
- Floats
- Lists-indexing 
- dictionary
- Strings, and string manipulation

### 3. Automation (9/1)
- Loops- for/while
- if/else (computation example 4 motivation)

### 4. Numpy (9/2)
- Array Wise operations and math
- 2D arrays, linear algebra
- (mention that all numpy knowledge we learned here is enough for basic data manipulation)

### 5. Numpy Continued (9/3)

## Week 2:  Functions and Pandas

### 1. Functions (9/7)
- User-defined functions
- docstrings!!!
- List python built-in functions
- Make connection to functions in libraries

### 2. Introduction to Plotting (9/8)
- plotting with matplot
- using functions for automating plots

### 3. Introduction to pandas (9/9)
- Create a dataframe from scratch
- Read in tabular data into a dataframe
- View and access data in the dataframe
- Save and export a dataframe

### 4. Introduction to pandas (9/10)
- Modify dataframe
- Modify values
- Clean data and make a function to import data
- Merge, concat, append
- Automation (functions, for loops)

## Week 3: Applied

### 1. Pandas applications (9/13)
- Intro to Math/Stats  
- Intro to pivot, groupby
 
### 2. Intermediate Plotting (9/14)
- Seaborn
- Intro to SciPy

### 3. Maps (9/15)
- Maps + gif
- .py/.sh scripts

### 4. Classes and Conlusion (9/16)
- Classes
- Computing at scale and the RCC
- Best practices

### 5. NO CLASS (9/17)
-We didn't need the buffer day we had originally scheduled.


# Office Hours
Office Hours Zoom: 
https://uchicago.zoom.us/j/97235120674?pwd=RUlqUUNMY25SL2h2a2JvMFhMdis1Zz09
Meeting ID: 972 3512 0674   Passcode: 965225


## Week One:
### August 30, 2021 (Monday)
Slot 1: 1:00pm

Slot 2: 2:00pm 

Slot 3: 4:00pm

### August 31, 2021 (Tuesday)
Slot 1: 1:00pm

### September 1, 2021 (Wednesday)
Slot 1: 3:00pm

### September 2, 2021 (Thursday)
Slot 1: 4:00 pm

### September 3, 2021 (Friday)
Slot 1: 8:30am

## Week Two:

### September 7, 2021 (Tuesday)
Slot 1: 11:00 am

Slot 2: 1:00pm

### September 8, 2021 (Wednesday)
Slot 1: 11:00 am

### September 9, 2021 (Thursday)
Slot 1: 4:00 pm

### September 10, 2021 (Friday)
Slot 1: 8:30am

## Week Three:
### September 13, 2021 (Monday)

Slot 1: 4:00 pm

Slot 2: 11:00 am

### September 14, 2021 (Tuesday)
Slot 1: 8:30am

### September 15, 2021 (Wednesday)
Slot 1: 11:00 am

### September 16, 2021 (Thursday)
Slot 1: 4:00 pm

