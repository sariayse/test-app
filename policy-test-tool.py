#!/usr/bin/python
import sys
from modules.database import *
from modules.probe import probe, probeshell

def parseargs():
    strargs=''.join(sys.argv)
    if strargs.find('--symyname'):
        print 'ayse'
def main():
    global probe
    parseargs()
    print "INFO: Application started"
    node=probe()
    node.get()

if __name__ == '__main__':
    main()