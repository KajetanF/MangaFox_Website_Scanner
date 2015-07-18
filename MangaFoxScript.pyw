from urllib import urlopen, urlretrieve
import re
import webbrowser

def MangaListAdjuster():
    with open("C:\Users\Kajetan\Documents\TodayMangaList.html","w") as MangaWipe:        #Wipes previous Manga List
        MangaWipe.write("")
        MangaWipe.close()

    with open("C:\Users\Kajetan\Documents\myMangaList.txt","r") as MangaInfo:           #Generates a new manga list to search from Manga List Document
        MangaStr = MangaInfo.read()
        print "Your novels are the following:\n %s" %(MangaStr)

    with open("C:\Users\Kajetan\Documents\myMangaList.txt", 'r') as myManga:
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

    with open("C:\Users\Kajetan\Documents\TodayMangaList.html", "a") as myManga:
        myManga.write('<a href="http://mangafox.com>MANGAFOX HOMEPAGE"</a><br><br>')

    try:
        for i in range(1,len(findPatTitle)+1):
            if findPatSeries[i] in MangaList:
                with open("C:\Users\Kajetan\Documents\TodayMangaList.html", "a") as myManga:
                    myManga.write(findPatLink[i]+'">' + findPatTitle[i] + "</a><br>")
    except IndexError:
        pass
    
    
def MultipleChapters():
    patFinderSecondTitle = re.compile('                        <dl><dt><em>.*</em><span class="chapter nowrap"><a href=".*class="chapter">(.*)</a></span></dt><dt><em>.*</em><span class="chapter nowrap"><a href=".*" class="chapter">')
    patFinderSecondLink = re.compile('                        <dl><dt><em>.*</em><span class="chapter nowrap"><a href=".*" class="chapter">.*</a></span></dt><dt><em>.*</em><span class="chapter nowrap"><a href="(.*)" class="chapter">(.*)</a>')

def main():
    Manga = MangaListAdjuster()                   #Creates the Manga List file
    MangaFoxChecker("http://mangafox.me/releases/",Manga)       #scans first page   
    MangaFoxChecker("http://mangafox.me/releases/2.htm",Manga)
    new = 2
    webbrowser.open("file:///C:/Users/Kajetan/Documents/TodayMangaList.html",new=new)
if __name__ == '__main__' : main()
