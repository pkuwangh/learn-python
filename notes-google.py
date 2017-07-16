# get help for a module and its built-in functions
>> import sys
>> dir(sys)
>> help(sys.exit)

# list
>> a = [1, 2, 'aa'] + [3, 4]
>> b = a        # b is a reference to list a
>> b = a[:]     # make a copy of list a
# keyword "in"
>> for num in a: print num
>> 2 in a
>> a.append(10)
>> x = a.pop(2)
# sort
>> a = ['ccc', 'aaaa', 'd', 'bb']
>> b = sorted(a)
>> b = sorted(a, key=len)
>> def Last(s): return s[-1]
>> b = sorted(a, key=Last)
# join & split
>> b = ':'.join(a)
>> b.split(':')

# tuple
>> a = (1, 2, 3)    # fixed size, immutable
>> (x, y) = (1, 2)  # simultaneous assignment

# dictionary, i.e. hash table
>> d = {'a':'alpha', 'b':'beta'}
>> d['g'] = 'gamma'
>> d.get('x')       # get() returns None if key not found
>> d.keys()         # no order specified
>> d.values()       # same 'random' order as keys()
>> for k in sorted(d.keys()): print 'key:', k, '->', d[k]
>> for t in d.items(): print t

# file
>> f = open(filename, 'rU')
>> for line in f: print line,
>> text = f.read()          # read entire file as a string
>> lines = f.readlines()    # read entire file in a list
>> f.close()

# regular expression
>> import re
>> match = re.search('ig', 'called piiig')  # search
>> if match: print match.group()
# . (dot) any char
# \w word char
# \d digit
# \s whitespace
# \S non-whitespace
# + 1 or more
# * 0 or more
>> re.findall(r'[\w.]+@[\w.]+', 'blah nick.p@gmail.com ya foo@bar')     # returns a list
>> re.findall(r'([\w.]+)@([\w.]+)', 'blah nick.p@gmail.com ya foo@bar') # a list of tuples

# system
# os module
>> os.listdir('.')                      # return list of strings
>> os.path.join(directory, filename)
>> os.path.abspath(filepath)
>> os.path.dirname(path)                # return the directory name
>> os.path.basename(path)               # return the file name
>> os.path.exists(filename)
>> os.mkdir(dir_path)
>> shutil.copy(src_path, dir_path)
# commands module
>> (status, output) = commands.getstatusoutput(cmd)

