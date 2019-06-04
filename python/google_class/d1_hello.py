#!/usr/bin/python -tt

import sys


def Cat(filename):
  f = open(filename, 'rU')  # 'U' ignores dos/unix issues
  for line in f:
    print line,   # trailing comma absorb the new line
  
def Hello(name):
  if name == 'Alice' or name == 'Nick':
    name = name + '??'
  else:
    name = name + '!!!!'
  print 'Hello', name     # comma adds a space in between

def stringDemo():
  print 'a = %d, b = %4.1f' % (3, 4.1)
  a = 'abcdefg'
  print a[2:4]
  print a[2:]
  print a[:-3]

def main():
  Hello(sys.argv[1])
  stringDemo()
  Cat(sys.argv[1])

if __name__ == '__main__':
  main()
