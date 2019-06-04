#!/usr/bin/python -tt

import sys
import os
import commands

def List(directory):
  filenames = os.listdir(directory)
  for filename in filenames:
    filepath = os.path.join(directory, filename)
    print filepath
    print os.path.abspath(filepath)

def LL(directory):
  cmd = 'ls -l ' + directory
  (status, output) = commands.getstatusoutput(cmd)
  if status:
    sys.stderr.write('there was an error:' + output + '\n')
    sys.exit(1)
  print output

if __name__ == '__main__':
  LL(sys.argv[1])
  List(sys.argv[1])
