import random
from itertools import chain

# This code is terrible

header = '''---
layout: default
title: Groups
---

# 1pm Groups
'''

groups = open("index.md", "r")
    
ta = ''
img = ''
number = -1
students = {}
tas = []
currgroup = 0

cgo = 0

# This is super ugle and hacky, but gets a data structure I can work with.
for line in groups:
  if line[0] == '|':
    cgo = -1
    tokens = line.split('<br>')
    for i in range(len(tokens)):
      token = tokens[i]
      print('I: ' + str(i) + ' --- ' + token)
      if i == 0:
        ta = token[1:]
        students[ta] = []
      elif token[0] == '|':
        currgroup = token[2:-2]
        if currgroup != '':
          currgroup = int(currgroup.strip('*'))
          students[ta].append([])
          cgo += 1
      elif token[0] == '<':
        currgroup = token[-5:-2]
        if currgroup != '':
          currgroup = int(currgroup.strip('*'))
          print(currgroup)
          students[ta].append([])
          cgo += 1
      else:
        students[ta][cgo].append(token)

# Create new file
new_index = open('newindex.md', 'w')
new_index.write(header + '\n')

# Do the shuffling
group_num = 1
index = 0

tas = list(students.keys())
random.shuffle(tas)

for ta in tas:
  groups = students[ta]

  newgroups = [[], [], [], [], []]
  for i in range(len(groups)):
    for j in range(len(groups[i])):
      newi = (i+j)%5
      newgroups[newi].append(groups[i][j])

  # Confirm that we did not lose any students in the process
  fo = list(chain.from_iterable(groups))
  fn = list(chain.from_iterable(newgroups))
  fo.sort()
  fn.sort()
  if fn != fo:
    print('BADDDDD LOST A STUDENT')
  else:
    print('SUCCESSFULL SHUFFLE')

  new_index.write('|' + ta + '<br><img src="../../images/?.png" class="taimg" />|')
  for i in range(len(newgroups)):
    new_index.write('**' + str(group_num) + '**<br>')
    group_num += 1
    for j in range(len(newgroups[i])):
      new_index.write(newgroups[i][j] + '<br>')
    new_index.write('|')
  new_index.write('\n')
      

