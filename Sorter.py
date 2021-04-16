import os
import shutil

#os.system("time")
#os.mkdir("D:/WHJ/Class99/TestFolderOf_C99")
#print(os.getcwd())

path=""
exist=os.path.exists(path)

#print(exist)

filePath="D:/AA_Unclassified_Items/"
bbc=os.path.splitext(filePath)

#print(bbc)

#print(os.listdir("D:/WHJ/Class99"))

src=input("Source path: ")
dest=input("Destination path: ")

#destination=shutil.move(src, dest)
#print(os.listdir("D:/WHJ/Class99"))

path2=input("Path Two (Same as Source path): ")
files=os.listdir(path2)
for i in files:
    name, ext=os.path.splitext(i)
    ext=ext[1:]
    if ext=="":
        continue
    if os.path.exists(path2+"/"+ext):
        shutil.move(path2+"/"+i,path2+"/"+ext+"/"+i)
    else:
        os.makedirs(path2+"/"+ext)
        shutil.move(path2+"/"+i,path2+"/"+ext+"/"+i)
