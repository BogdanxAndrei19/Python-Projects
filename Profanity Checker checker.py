import urllib

def readText():
    quotes=open("C:\Bogdan's Folder\#INFO\UDACITY\Introduction to functions in Python\ProfanityChecker\movie_quotes.txt")
    contentFile=quotes.read()
    print(contentFile)
    quotes.close()
    checkProfanity(contentFile)

def checkProfanity(textToCheck):
    connection= urllib.urlopen("http://www.wdylike.appspot.com/?q=QUERY"+textToCheck)
    output=connection.read()
    print(output)
    connection.close()

readText()
