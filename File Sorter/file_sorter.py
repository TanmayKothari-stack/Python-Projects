import os,shutil

folders = {"Text":['.txt'],"Python":['.py'],"Audio":['.wav','.mp3'], "Image":['.png','.jpg','.jpeg'],"Video":['.mp4']}

directory = "E:\\Program Files"

counter = {"Text":0,"Python":0,"Audio":0,"Image":0,"Video":0}

def counting():
	files = os.listdir(os.path.join(directory,folder))
	for file in files:
		if file.endswith(".txt"):
			counter["Text"]+=1

		if file.endswith(".py"):
			counter["Python"]+=1
		
		if file.endswith(".mp3"):
			counter["Audio"]+=1
		
		if file.endswith(".png"):
			counter["Image"]+=1
		
		if file.endswith(".mp4"):
			counter["Video"]+=1
	print("There are",counter['Text'],"Text files")
		




for folder in folders:
	files = os.listdir(directory)
	for ext in folders[folder]:
		for file in files:
			if file.split(".")[-1] == ext.split(".")[-1]:
				if os.path.exists(os.path.join(directory,folder)):
					pass

				else:
					os.mkdir(os.path.join(directory,folder))
					shutil.copy(os.path.join(directory,file),os.path.join(directory,folder))
