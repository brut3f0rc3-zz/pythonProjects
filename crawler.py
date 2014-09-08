from bs4 import BeautifulSoup
import urllib2
import re


def parse(linkWithTag):
    match = re.search(r'href=[\'"]?([^\'" >]+)', linkWithTag)
    if match:
        return match.group(1)

def getLinks(url, links):
    html = urllib2.urlopen(url)
    soup = BeautifulSoup(html)
    for link in soup.find_all(href=re.compile('[\S]*')):
        link = str(link)
        parsedUrl = parse(link)
        if re.search(r'^\/[^\/].*', parsedUrl):
            parsedUrl=url+parsedUrl
        if parsedUrl == '#' or parsedUrl == '/':
            continue
        if parsedUrl in links.keys():
            continue
        else:
            links[parsedUrl]=False
            print parsedUrl

    for newLink in links.keys():
        if links[newLink] == False:
            matches = re.search(r'^(\S*\.css)|(\S*\.js)|(\S*\.php)|(\S*\.html)|(\S*\.htm)|(\S*\.jsp)|(\S*\.png)|(\S*\.jpeg)|(\S*\.jpg)|(\S*\.gif)$', newLink)
            if matches == None:
                getLinks(newLink, links)
            else:
                continue
        else:
            continue

def main():
    url = "http://www.ticsealumni.com"
    links={}
    links[url]="true"
    getLinks(url, links)



if __name__ == '__main__':
    main()