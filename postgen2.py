 import os;
from os import walk
from os.path import isfile, join

def getextension(a):
	strlist = a.split(".");
	return strlist
def getcmd(time = "00:00:01",path="",size="384x216",destPath=""):
		 return 'ffmpeg -ss '  + time + ' -i "' + path +'" -y -s ' + size + ' -vframes 1 -f image2 "' + destPath +'"'	;
def getcmd1(path,destPath):
		 return 'srt-to-vtt "'  +  path +'" > "'+destPath +'"'	;
def getbhj(a):
	strlist = a.split("\\");
	return strlist
f =[]
d=[]
i=1
for (dirpath , dirnames , filenames) in walk("posters") :
	f=filenames
	d=dirnames
	
	dirbreak = dirpath.split("\\")
	
	if len(dirbreak) == 2 :
		
#print (f);
#print(d)
#print (walk("."))	
	