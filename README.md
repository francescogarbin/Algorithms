### A Journey across fundamental algorithms

In September 2020 I decided I had enough with the usual web-centric stuff and dediced to create some space for new and refreshing coding opportunities.

It did not take too long for me to start browsing the Amazon catalog for good 
quality books on non-UX oriented programming, having decided to make a step back 
from the day-to-day coding of Javascript and Ruby stuff and to get back into
programming fundamentals. When I think "fundamentals" I mean a place where
writing software has - almost - nothing to do with reusing code from libraries
and pre-built components or data structures. And this means getting back
to basic programming logic, data scructures and - alas! - getting as close 
as possible to the CPU.

I therefore brushed off my old K&R's ANSI C book and started writing basic linked
lists and manipulating arrays. Fun. Lots of it. But I was not learning much:
at the end of the day, good old ANSI C did not change much from thirty-five years ago (yep, I did program in C on a Commodore Amiga 500 in my teens!) and, although interesting, I was sorta feeling I could mix my personal research with some novelty factors such as, for instance, a programming language I sorta-knew about but have not much of a chance to use in my day job.

I picked Python. And love every bit of it.

It's kind of unstructured and works well in both structured as well as
object-oriented programming. I requires a lot of discipline to write good code
because it's far too easy to make a mess out of it. But when you apply some
basic common sense or even a real clean-code approach while writing Python code,
the result are generally beautiful.

A level of clarity that is way higher than, say, C (and BTW I love C and, to an
extent, C++).

I therefore started converting my first basic algorithms originally written in C
to Python and created a small GUi, the TkTestHarness, with the Python Tk/Tcl library, TkInter. Honestly, I'd have gone with GTK+ 3.0 but the GTK+ Python library is not available for the Linux distribution I'm using for my experiments. A shame, the GTK+ widgets are quite beautiful on a GNOME desktop and TkInter does not match that level of polished appearance. It only kinda comes close.

Anyway, this repo collects my journey on fundamental algorithms written in Python
on a basic testharness GUI application.

And it's a fun journey, for sure.

## How to run the code

The code is hosted in the <code>src</code> folder with an entry point in <code>main.py</code> which assumes Python 3.

Algorithms are encapsulated in a small class library in the src/classes folder, nothing too fancy, every algorithm is launched via the run() method of its own class, everything is pretty much self-describing and in fact you'll notice that there's not much commenting around. Critical operations are better explaned through the occasional log.debug() statement. My code generally does not need comments other than for stating some code-agnostic instructions.

The code imports standard Python libraries such as:
* logging for emitting a log file in the current directory via logging.info, logging.debug, etc.
* os for some nice platform-independent helpers such as linesep for line termination. 
* tkinter and its themed wrapper ttk for the implementation of the UI

At the date of this writing I have not yet written a requirements.txt file but plan
 to do so in the future.

When you download the code, a good idea is to run it in its own virtualenv, which of
course is not part of the repo, GitHub has some nice intelligence when it comes to
automatically exclude files and folders given the project's type set in its repos. 
  
Anyway, clone or download the repo, create a virtualenv on your machine, open a terminal
and run it with:

<code>$ python3 main.py</code>

Enjoy.

Francesco, 26th September 2020
