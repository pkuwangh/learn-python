#!/usr/bin/python -tt

import sys

def Cat(filename):
  try:
    f = open(filename, 'rU')
    for line in f:
      print line,
  except IOError:
    print 'IO Error', filename

def main():
  Cat(sys.argv[1])

if __name__ == '__main__':
  main()

