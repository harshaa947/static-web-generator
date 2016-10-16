import os;
from os import walk
from os.path import isfile, join
list = os.listdir("..")
list.remove("public server")
print (list)
for x in list :
	temp = os.listdir("../"+x)
	if isfile("../"+x):
		
	for y in temp:
		temp1 = os.listdir("../"+x+"/"+y)
		print(temp1)
	print(temp)
	
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
def correcthyphen(a):
	return a.replace("\\","/");	
f =[]
d=[]
i=1
for (dirpath , dirnames , filenames) in walk("posters") :
	f=filenames
	d=dirnames
	for x in f:
		strlist = getextension(x);
		if strlist[1] == "mp4":
			cdirpath = dirpath.replace(" Videos","")
			newpath = "posters/" +cdirpath[3:]
			if not os.path.exists(newpath):
				os.makedirs(newpath)
			newfpath = newpath +"/" + strlist[0] +".png"
			cmd = getcmd("00:00:08",dirpath+"/"+x,"1280x740",newfpath)
			os.system(cmd);
			print(cmd)
		if strlist[1] == "srt":
			cdirpath = dirpath.replace(" Subtitles","")
			newpath = "srt/" +cdirpath[3:]
			if not os.path.exists(newpath):
				os.makedirs(newpath)
			newfpath = newpath +"/" + strlist[0] +".vtt"
			cmd = getcmd1(dirpath+"/"+x,newfpath)
			os.system(cmd);
			print(cmd)
	
	dirbreak = dirpath.split("\\")
	if len(dirbreak) == 1 :
		str ="""<!DOCTYPE html>
				<html lang="en">
				<head>
					<meta charset="UTF-8">
					<title>My videos</title>
					<link rel="stylesheet" href="style.css">
					<script src="script.js"></script>
				</head>
				<body>
				<div id="courses" >
						""";
		for y in d :		
			str +="""<div class="course thumbnail">
							<h4>""" + y +'</h4>'+"""
							<a href=\"""" + y +"/index.html"+"""\">
							<img src="posters/"""+y+'.png"> </a>'+"""
						</div>
				   """;
			if not os.path.exists('html/'+y):
				os.makedirs('html/'+y)	   
		str +="""</div>
				</body>
				</html>""";
		if not os.path.exists('html'):
				os.makedirs('html')		
		file=open('html/index.html','a')
		file.close()		
		file = open('html\index.html','w');
		file.write(str);
		file.close();
	if len(dirbreak) == 2 :
		
		str ="""<!DOCTYPE html>
				<html lang="en">
				<head>
					<meta charset="UTF-8">
					<title>"""+dirpath[8:]+""" </title>
					<link rel="stylesheet" href="../style.css">
					<script src="../script.js"></script>
				</head>
				<body>
				<div id="course playlists" >
				<h1> """+dirpath[8:]+'</h1>'+"""
						""";
		for y in d :
			relpath = dirpath[8:];
			relpath += "/"+y
			
			str +="""<div class="playlist thumbnail">
							<h4>""" + y +'</h4>'+"""
							<a href=\"""" + y +"/index.html"+"""\">
							<img src="posters/"""+relpath+'.png"> </a>'+"""
						</div>
				   """;
			if not os.path.exists('html/'+relpath):
				os.makedirs('html/'+relpath)	   
		str +="""</div>
				</body>
				</html>""";
		file=open('html/'+dirpath[8:]+"/"+'index.html','a')
		file.close()		
		file = open('html/'+dirpath[8:]+"/"+'index.html','w');
		file.write(str);
		file.close();	
	if len(dirbreak) == 3 :
		courlist = getbhj(dirpath[8:]);
		filenamedf = getextension(f[0])[0]
		str = """
						<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<title> """+courlist[0]+""" </title>
			<link rel="stylesheet" href="../../style.css">
			<script src="../../script.js"></script>
		</head>
		<body>
			<h1>WELCOME TO THE PLAYLIST
			Course 	: """+courlist[0]+"""
			Chapter : """+courlist[1]+"""
			</h1>
		    		

				<div id="video_container">
					 <h2 id="name">"""+filenamedf+"""</h2>
					 <div class="invisible overlay1" id="videolay">
             <h3 > Video Changing</h3>
             <h3> Current VIdeo :</h3>
             <h3>Next Video</h3>
             <h1>Timer</h1>
            </div>
					<video id="player" height="432" width="768" controls>
						<source id="videosrc" src="../../../videos/"""+correcthyphen(dirpath[8:])+"/"+filenamedf+'.mp4"type="video/mp4">'+"""
					
					<track label="English" kind="subtitles" srclang="en" src="../../../srt/""" + correcthyphen(dirpath[8:]) +"/"+ filenamedf +'.vtt"'+""" default>

					</video>
					<div id ="controls">
         <button class="control" onclick="playprev()">PREV</button>
          <button class="control" onclick="playnext()">NEXT</button>
         </div>
				</div>
				<div id ="playlist">
					<div id="inner">
					 <div id="overlay" class="invisible">
					  <h4></h4>
					  <img src="../../img/play.png" width="104" height="102">
					 </div>""";
		for z in f :
			extlist = getextension(z);
			str +='<a href="../../../videos/'+correcthyphen(dirpath[8:])+"/"+ extlist[0] +'.mp4"><img width="384" height="216" src="../../../posters/'+correcthyphen(dirpath[8:])+"/"+extlist[0]+'.png" alt="'+extlist[0]+'"></a>';
		str += """</div>
				</div>
			<div id="test">
			 <h4></h4>
			</div>
		<script>
		 var video_player = document.getElementById("inner"),
				 links = video_player.getElementsByTagName('a');
		 for (var i=0; i<links.length; i++) {
		  links[i].onclick = handler;
		  links[i].onmouseenter = handler1;
		  links[i].onmouseleave = handler2;

		 }
		 var video = document.getElementById("player");
 video.addEventListener("ended",startnew,false);
		</script>
		</body>
		</html>""";	 
		file=open('html/'+dirpath[8:]+"/"+'index.html','a')
		file.close()		
		file = open('html/'+dirpath[8:]+"/"+'index.html','w');
		file.write(str);
		file.close();
#print (f);
#print(d)
#print (walk("."))	
	
