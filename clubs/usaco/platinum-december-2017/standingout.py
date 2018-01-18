"""
ID: your_id_here
LANG: PYTHON2
TASK: standingout
"""

def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in xrange(length) for j in xrange(i,length)]

fin = open ('standingout.in', 'r')
fout = open ('standingout.out', 'w')
n = int(fin.readline()) 
names = []
for i in range(n):
    names.append(fin.readline().replace('\n',''))

subs = [set(get_all_substrings(i)) for i in names]
unique = [len(i) for i in subs]

for i in range(n):
    minus = len(subs[i].intersection(set.union(*(subs[:i]+subs[i+1:]))))
    unique[i] -= minus

for i in unique:
    fout.write (str(max(0, i)) + '\n')

fout.close()
