#   Basic zip password cracker using dictionaries.
#   Usage : python zipCracker.py -f <zipFileName> -d <dictionary>
#   Uses python2.7

import optparse
import zipfile


def openZip(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print "[+] Password found : " + password
        exit(0)
    except:
        pass

def Main():
    parser =optparse.OptionParser("usage : -f <fileName> -d <dictionary>")
    parser.add_option('-f', dest="fileName", help="Please specify the file name")
    parser.add_option('-d', dest="dictFile", help="Please specify the dictionary to use")
    (options,arg) = parser.parse_args()
    if (options.fileName == None or options.dictFile == None) :
        print parser.usage
        exit(0)
    else:
        try:
            zFile = zipfile.ZipFile(options.fileName)
        except:
            print "The zip file was not found or was unable to be read"
            exit(0)

        try:
            dictFile = open(options.dictFile,'r')
        except:
            print "The dictionary file was not found or was unable to be read"
            exit(0)

        for line in dictFile.readlines():
            word = line.strip('\n')
            openZip(zFile, word)

        print "[-] The password couldn't be found"

if __name__=="__main__":
    Main()
