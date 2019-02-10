README:

This is a little script I did to scrape one of my favorite image collections on the internet and pull down all of the images. Big shout out to Sven Geier who made these incredible fractals that you will hopefully be downloading soon enough. I haven't made anything in python for quite some time so this was more a tool to refresh my memory. I'm a perl guy and I'll tell you, many of my perl shortcuts [that make things work yet unreadable] don't work in python.

Usage:

./main.py

Installation:
just run setup.sh on your favorite ubuntu machine.
otherwise, just look at it and figure out which dependencies that you need to install. This was made to work with python3 so you will need the package python3-pip to install the dependencies which are listed in requirements.txt

What this does:
Goes to the main index of all the fractals, and parses the page to make a list to download and downloads them to a folder that it creates in this directory called workdir.

How to set scrapes as your desktop background:
mkdir -p ~/Pictures/backgrounds && rsync -av workdir/ ~/Pictures/backgrounds/
then go into your display managers background settings and tell it to randomly cycle through that folder at your desired interval.

Extensibility:
this uses python requests to pull the page down and beautiful soup to parse it for links to images. There's an array of image types that it cycles through on that list to make it's download queue. The url that it extracts this from is in the file searchList.txt and you can add any site there that you want to scrape images from. Beautiful soup is nice because in my perl days, I would use a bunch of regex that would really be quite site specific. Now, I can work with any site with proper or broken html [everyone knows that nobody actually uses proper html anymore, eh?] and get the information that is desired.

Known issues:
I should do a check to make sure that the client receives a status 200 before it tries to go through all of the downloading logic. I'm sure you'll get a nice error otherwise.
