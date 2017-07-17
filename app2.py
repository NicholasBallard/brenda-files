import os, shutil, pprint

WORKING_DIRECTORY = r'c:\users\nicholasericballard\desktop'
os.chdir(WORKING_DIRECTORY)
DIRECTORY = 'workThisDirectory'

temp = os.walk(DIRECTORY, topdown=False)
for dirpaths, directories, files in temp:
    print(dirpaths)