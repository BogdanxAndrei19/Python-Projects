import urllib

def readText():
    quotes=open("C:\path\movie_quotes.txt")
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
