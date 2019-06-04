#!/usr/bin/python -tt

import re

def find(pattern, text):
  match = re.search(pattern, text)
  if match:
    print match.group()
  else:
    print 'not found'

if __name__ == '__main__':
  find('ig', 'called piiig')
  find('...g', 'called piiig')                      # . dot
  find(r'c\..ll', 'c.alled piiig')                  # leading r indicates raw string
  find(r':\w\w\w', 'blah :c7t blah')                # word char (including digit)
  find(r':\d\d\d', 'blah :123xxx')                  # digit
  find(r'\d\s\d\s\d', '1 2 3')                      # whitespace
  find(r'\d\s+\d\s+\d', '1   2      3')             # 1 or more
  find(r'\d\s*\d\s+\d', '12      3')                # 0 or more
  find(r'\S+', 'x12      3')                        # 0 or more
  find(r':\w+', 'blah :kitten123 blah')
  find(r'\w+@\w+', 'blah nick.p@gmail.com yatta')
  find(r'[\w.]+@[\w.]+', 'blah nick.p@gmail.com yatta') # [] a set of characters
  find(r'\w[\w.]*@[\w.]+', 'blah .nick.p@gmail.com yatta')

  m = re.search(r'([\w.]+)@([\w.]+)', 'blah nick.p@gmail.com yatta @')
  print 'group 1:', m.group(1)
  print 'group 2:', m.group(2)

