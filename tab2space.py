# Put this code inside the directory you want to fix tabs

import os, sys

spaces = "         "

DIR = "./"

file_list = [sys.argv[1]]

#for root, dirs, files in os.walk(DIR):
#  for name in files:
#    path = os.path.join(root, name)
#    if name != __file__:
#      file_list.append(path)

for file_path in file_list:
  file = open(file_path, 'r')
  content = file.read()
  content = content.replace("\t", spaces)
  file.close()
  file = open(file_path, 'w')
  file.write(content)

