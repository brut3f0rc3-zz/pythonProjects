from bs4 import BeautifulSoup
import urllib
import argparse
import re
import sys

linksList={}

def extractAllLinks(url, domain):

    #   URL has been visited
    linksList[url]=True

    try:
        page = urllib.urlopen(url)
    except IOError:
        print "The connection to "+url+" couldn't be made"
        return

    if page.code == 200:

        bs = BeautifulSoup(page.read(), "lxml")

        #   Store all the anchors on the page
        links = bs.findAll('a')

        if len(links):
            #   Check if href is present. If present display the url
            for link in links:

                if link.has_attr('href'):

                    if link['href']!='#' and link['href']!='/':

                        #   If the webpage belongs to the same domain
                        if (domain in link['href']) or (link['href'][0]=='/') or (('http://' not in  link['href']) and ('https://' not in link['href'])) :

                            #   If the webpage has not already been listed
                            if link['href'] not in linksList.keys():

                                #   List the webpage and mark it False
                                linksList[link['href']] = False
                                print link['href']+" : Completed"

    else:
        print "URL : "+url+" returned a "+page.code

def main():
    if len(sys.argv) == 1:
        print "Usage : "+sys.argv[0]+" [-u <baseURL>] [-l]"
        sys.exit(0)
    parser = argparse.ArgumentParser(description="Tries to find all the links for a given website", usage='%(prog)s [-u <baseURL>] [-l]')
    parser.add_argument('-u', '--url', dest='domain', help='The base URL for the website', default="localhost")
    parser.add_argument('-l', '--log', dest='log', help='Log the results', action="store_true", default="False")
    args = parser.parse_args()

    #   Set the domain
    domain = args.domain

    linksList[args.domain]=False

    print "Connecting to "+domain+"...\n"

    #   Iterate until all the pages in the linksList have been visited
    for key in linksList.keys():
        if linksList[key]==False:
            extractAllLinks(key, domain)


    #   Log the results if asked to do so
    if args.log:
        fileName = re.match(r'^[\w]+\:\/\/([\S]*)$', domain)
        logFile = open(fileName.group(1), "w+")


        #   Write to file
        for key in sorted(linksList.keys()):
            logFile.write(key+"\n")
        logFile.close()

        print "\nLog file created. Name : "+fileName.group(1)+"\n"

    print "Thank you for using!"


if __name__=='__main__':
    main()


