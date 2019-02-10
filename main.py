#!/usr/bin/env python3
#start up the program
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import os
#set up our variables
sources_file = "searchList.txt"
file_types = ['jpg','JPG','jpeg','JPEG','png','PNG','gif','GIF','bmp','BMP']
sources = []
workdir = "workdir"
object_count = 0
#set up our workdir
if not os.path.exists(workdir):
	os.mkdir(workdir, mode=0o700)
#read sources from list to determine which site to scrape
source_fd = open(sources_file, mode='r')
for source in source_fd:
	#add current lines source to the sources array
	sources.append(source.strip("\n"))
source_fd.close()
#load each source and parse it for desired objects and download them
print("downloading")
for source in sources:
	page = requests.get(source)
	soup = BeautifulSoup(page.text, 'html.parser')
	for link in soup.find_all('a'):
		this_object = link.get('href')
		for filetype in file_types:
			if this_object.endswith(filetype):
				print('.',end='',flush=True)
				image = requests.get(urljoin(source,this_object))
				filename=str(this_object)
				with open(workdir+"/"+filename.split('/')[-1], 'wb') as fd:
					for chunk in image.iter_content(chunk_size=512):
						fd.write(chunk)
				#print(urljoin(source,this_object))
				object_count+=1
#report stats
print("\n"+str(object_count) + " objects have been processed")
print("best action to do next:\nmkdir ~/Pictures/backgrounds/ && rsync -av workdir/ ~/Pictures/backgrounds/\nHope you anjoy!")
#close out
