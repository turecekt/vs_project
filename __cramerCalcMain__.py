#import file with methodss for matri operation
from __cramerLib__ import *
#import sys for handling of arguments
import sys

#main method doing the calculation
def main():


    if(len(sys.argv) != 2):
        if(len(sys.argv) < 2):
            print("too few argumetns specified")
            sys.exit(1)
        else:
            print("too many arguments specified")
            sys.exit(1)

    if(sys.argv[1] == 'help'):
        print("help me")
        sys.exit(0)

    #open file and 
    try:
        open("hulahula.toptop")
    except IOError:
        print("File "+sys.argv[1]+' not found on this machine')
        sys.exit(1)



main()
