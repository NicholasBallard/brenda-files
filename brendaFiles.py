import os
import shutil
import pprint

# change current working directory to the Desktop
os.chdir(r'c:\users\nicholasericballard\Desktop\\')

# shutil.copy2(src, dst)
# Similar to shutil.copy(), but metadata is copied as well – in fact, this is just shutil.copy() followed by copystat(). This is similar to the Unix command cp -p.

# testFolder
directory = '2017'

# add each absolute path to a list
list_of_files = list()
for root, dirs, files in os.walk(directory):
    for name in files:
        list_of_files.append(os.path.join(root, name).split('\\'))

# make a new name for each file in the list_of_files, one shorter
shorter_file_names = list(list_of_files)

for absolute_file_path in range(len(shorter_file_names)):
    for part in range(1, len(shorter_file_names[absolute_file_path]) - 1):
        shorter_file_names[absolute_file_path][part] = shorter_file_names[absolute_file_path][part][:7].rstrip()

pprint.pprint(shorter_file_names)

# TODO: make folder for shorter file names 

new_folder = r'shortened_' + str( directory )

os.makedirs( new_folder , exist_ok=True)

for file in shorter_file_names:
    file[0] = str( new_folder )

newListOnTheBlock = list()
for i in range(len(shorter_file_names)):
    newListOnTheBlock.append('\\'.join(map(str, shorter_file_names[i])))

list_of_files_concatenated = list()
for i in range(len(list_of_files)):
    list_of_files_concatenated.append('\\'.join(map(str, list_of_files[i])))

print('{} files in list_of_files\n{} files in shortened list.\n{} files in newListOnTheBlock'.format(len(list_of_files),len(shorter_file_names), len(newListOnTheBlock)))

# for file in range(len(list_of_files)):
#     os.renames(list_of_files_concatenated[file], newListOnTheBlock[file])

print(id(list_of_files),id(list_of_files_concatenated),id(shorter_file_names),id(newListOnTheBlock),sep='\n')

pprint.pprint(list_of_files)

# TODO:
'''
os.renames(src, dest) will do the trick recursively
will shutil.move recursively move files?
'''
