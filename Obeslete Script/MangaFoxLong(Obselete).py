from class_MangaFoxGUI import *
from urllib import urlopen, urlretrieve
import re
import webbrowser

def MangaListAdjuster(Address):
    with open("C:\Users\Kajetan\Documents\TodayMangaList.html","w") as MangaWipe:        #Wipes previous Manga List
        MangaWipe.write("")
        MangaWipe.close()

    with open(Address,"r") as MangaInfo:           #Generates a new manga list to search from Manga List Document
        MangaStr = MangaInfo.read()
        print "Your novels are the following:\n %s" %(MangaStr)

    if (MangaStr == "") or (raw_input("Type yes to add a manga, if not type anything else").lower()=="yes"):    #writes old manga list as well as added manga list to file
        with open("C:\Users\Kajetan\Documents\myMangaList","w") as MangaEdit:           
            MangaEdit.write(MangaStr+"\n")
            while True:
                AddedManga = (raw_input("Enter full anime name one at a time, type '0' once finished"))
                if (AddedManga != "0"):
                    MangaEdit.write(AddedManga+"\n")
                else:                      
                    break

    with open(Address, 'r') as myManga:
        ListOfManga = myManga.read()
    MangaList = filter(None,ListOfManga.split("\n"))        #Creates List with added manga, while filtering out dead spaces
    print MangaList
    return MangaList

def MangaFoxChecker(url,MangaList):                    
    webpage = urlopen(url).read()

    patFinderSeries = re.compile('                        <dl><dt><em>.*</em><span class="chapter nowrap"><a href=".*" class="chapter">(.*)\s\d+</a>')
    patFinderTitle = re.compile('                        <dl><dt><em>.*</em><span class="chapter nowrap"><a href=".*" class="chapter">(.*\s\d+)</a>')
    patFinderLink = re.compile('                        <dl><dt><em>.*</em><span class="chapter nowrap">(<a href=".*)" class="chapter">.*\s\d+</a>')


    findPatTitle = re.findall(patFinderTitle,webpage)
    findPatLink = re.findall(patFinderLink,webpage)
    findPatSeries = re.findall(patFinderSeries,webpage)

    try:
        for i in range(1,len(findPatTitle)+1):
            if findPatSeries[i] in MangaList:
                with open("C:\Users\Kajetan\Documents\TodayMangaList.html", "a") as myManga:
                    myManga.write(findPatLink[i]+'">' + findPatTitle[i] + "</a><br>")
                    myManga.close()
    except IndexError:
        pass
    
    
def MultipleChapters():
    patFinderSecondTitle = re.compile('                        <dl><dt><em>.*</em><span class="chapter nowrap"><a href=".*class="chapter">(.*)</a></span></dt><dt><em>.*</em><span class="chapter nowrap"><a href=".*" class="chapter">')
    patFinderSecondLink = re.compile('                        <dl><dt><em>.*</em><span class="chapter nowrap"><a href=".*" class="chapter">.*</a></span></dt><dt><em>.*</em><span class="chapter nowrap"><a href="(.*)" class="chapter">(.*)</a>')

def PageChecker(Manga):
    while True:
        try:
            pages = int(raw_input("Please type the number of pages you would like to scan through"))    #user decides the amount of pages to be scanned through
            break
        except ValueError,TypeError:
            print "Please Enter a Number!"

    print "LOADING PAGES"
    MangaFoxChecker("http://mangafox.me/releases/",Manga)       #scans first page   
    URL = "http://mangafox.me/releases/2.htm"
    for page in reversed(xrange(2,pages+1)):
            MangaFoxChecker(URL.replace("2",str(page)),Manga)   #scans second page onwards
           
    print "Pages %s have been scanned. Results have been added to document" %(pages)

def main():
    app = MangaGUI(None)
    app.mainloop()
    Manga = MangaListAdjuster(app.Address)                   #Creates the Manga List file
    PageChecker(Manga)   
    new = 2
    webbrowser.open("file:///C:/Users/Kajetan/Documents/TodayMangaList.html",new=new)


if __name__ == '__main__' : main()
