
import os

def renameFiles():
    
    #get files name
    
    fileList = os.listdir(r"C:\Bogdan's Folder\#INFO\UDACITY\Introduction to functions in Python\Image Sorter by Name\arranged")
    print(fileList)
    
    #cwd=current working directory
    
    savedPath=os.getcwd()
    #print("cwd is" + savedPath)
    os.chdir(r"C:\Bogdan's Folder\#INFO\UDACITY\Introduction to functions in Python\Image Sorter by Name\arranged")#programul lucra intr un folder superior ierarhic
    
    #for each file,rename it
    
    for fileName in fileList:
        os.rename(fileName,fileName.translate(None,"0123456789"))
    os.chdir(savedPath)#optional, ne intoarcem in folderul superior ierarhic initial

renameFiles()
