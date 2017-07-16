import os
import shutil
import sys
import pprint

# change current working directory to the Desktop
os.chdir(r'c:\users\nicholasericballard\Desktop\\')

# shutil.copy2(src, dst)
# Similar to shutil.copy(), but metadata is copied as well – in fact, this is just shutil.copy() followed by copystat(). This is similar to the Unix command cp -p.

# testFolder
directory = '2017\\'

# make sure I'm getting the absolute file path
for root, dirs, files in os.walk(directory):
    for name in files:
        print(os.path.join(root, name))

# add each absolute path to a list
list_of_files = list()
for root, dirs, files in os.walk(directory):
    for name in files:
        list_of_files.append(os.path.join(root, name).split('\\'))

# make a new name for each file in the list_of_files, one shorter
shorter_file_names = list(list_of_files)

for absolute_file_path in range(len(shorter_file_names)):
    for part in range(1, len(shorter_file_names[absolute_file_path]) - 1):
        shorter_file_names[absolute_file_path][part] = shorter_file_names[absolute_file_path][part][:7].rsplit()

pprint.pprint(shorter_file_names)
