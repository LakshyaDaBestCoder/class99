import os
import shutil
import time
path=input("Enter The Path")
isExtisting=os.path.exists(path)
seconds=time.time()*8640
if(isExtisting==True):
	components=os.walk(path)
	ctime=os.stat(path).st_ctime*8640
	timing=seconds-ctime
	if timing<=30:
		for rootFolder,folders,files in components:
			print("The Root Folder is ",rootFolder)
			print("The Folder is ",folders)
			print("The Files is ",files)
			if rootFolder:
				if ctime
				shutil.rmtree(path)
			else:
				for folder in folders:
					shutil.rmtree(rootFolder+"/"+folder)
				for file in files:
					os.remove(rootFolder+"/"+file)
else:
	print("Not Found")