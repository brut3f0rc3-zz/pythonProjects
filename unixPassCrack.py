#   Basic Unix Password Cracker
#   Currently just supports SHA-512 password cracking, that most Linux systems use as of now
#   Important checks regarding *,!, etc to be added

import sys
import crypt

def crackPass(hashedPass, dictName):
        algo = hashedPass.split('$')[1]
        salt = hashedPass.split('$')[2]
        print "[+] Salt in use is : "+salt

        salt = '$'+algo+'$'+salt+'$'
        unixPass = hashedPass.split('$')[3]
        dictFile = open(dictName,'r')

        if algo == '6':
            for line in dictFile.readlines():
                password = line.strip('\n')
                cryptedPass = crypt.crypt(password,salt)
                if(cryptedPass == hashedPass):
                    print "[+] Password found : "+password
                    return

            print "[-] Password couldn't be found."
        else:
            print "[-] We don't support the required algorithm as of now"



def main():
    if(len(sys.argv)!=3):
        print "Usage : python unixPassCrack.py <passwordFile> <dictionaryFile>"
        exit(0)
    else:
        passwordFile = open(sys.argv[1],'r')
        dictionaryFile = sys.argv[2]
        for line in passwordFile:
            if ':' in line:
                user = line.split(':')[0]
                hashedPass = line.split(':')[1].strip('')
                print "[*] Trying to crack password for user "+user
                crackPass(hashedPass, dictionaryFile)


if __name__=='__main__':
    main()