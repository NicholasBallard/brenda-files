import os, shutil, pprint

WORKING_DIRECTORY                                   = r'c:\users\nicholasericballard\desktop'
NAME_OF_FOLDER_WE_ARE_WORKING_ON                    = '2017'
DIRECTORY_NAME_OF_COPY                              = 'workThisDirectory'
NUMBER_OF_CHARACTERS_TO_KEEP_IN_EACH_FOLDER_NAME    = 5

os.chdir( WORKING_DIRECTORY )

# copy directory to working directory
try:
    shutil.copytree(NAME_OF_FOLDER_WE_ARE_WORKING_ON, DIRECTORY_NAME_OF_COPY)
except FileExistsError:
    print("The folder already exists.")

original_folder_names = list()
shortened_folder_names = list()
absolute_file_paths = list()
shortened_file_paths = list()

# THE ORIGINAL DIRPATH
for dirpath, directories, files in os.walk(DIRECTORY_NAME_OF_COPY):
    for file in files:
        original_folder_names.append( dirpath )

# THE SHORTENED DIRPATH
shortened_folder_names = list(original_folder_names)
for dirpath in range(len(shortened_folder_names)):
    shortened_folder_names[dirpath] = shortened_folder_names[dirpath].split('\\')
# shorten the folder names but leave the root alone
for dirpath in range(len(shortened_folder_names)):
    # change root
    shortened_folder_names[dirpath][0] = DIRECTORY_NAME_OF_COPY
    for folder in range(1, len(shortened_folder_names[dirpath])):
        # the number of characters to remain in the shortened folder names
        shortened_folder_names[dirpath][folder] = shortened_folder_names[dirpath][folder][:NUMBER_OF_CHARACTERS_TO_KEEP_IN_EACH_FOLDER_NAME].rstrip()
# stitch the dirpaths back together
for dirpath in range(len(shortened_folder_names)):
    shortened_folder_names[dirpath] = '\\'.join(map(str, shortened_folder_names[dirpath]))

# THE ORIGINAL FULL FILEPATH
for dirpath, directories, files in os.walk(DIRECTORY_NAME_OF_COPY):
    for file in files:
        absolute_file_paths.append(os.path.join(dirpath, file))

# THE SHORTENED FILEPATH
shortened_file_paths = list(absolute_file_paths)
for x in range(len(shortened_file_paths)):
    shortened_file_paths[x] = shortened_file_paths[x].replace(original_folder_names[x] , shortened_folder_names[x])

# MAKE SHORTENED DIRPATH
for folder in range(len(shortened_folder_names)):
    os.makedirs(shortened_folder_names[folder], exist_ok=True)

# COPY FILES INTO SHORTENED DIRPATH
for file in range(len(absolute_file_paths)):
    shutil.copy2( absolute_file_paths[file] , shortened_file_paths[file] )

# counts original folder's longest absolute path
old_longest_file = 0
for file in absolute_file_paths:
    if len(file) > old_longest_file:
        old_longest_file = len(file)

# counts longest absolute path
new_longest_file = 0
for file in shortened_file_paths:
    if len(file) > new_longest_file:
        new_longest_file = len(file)

print('The longest file is a total of {} characters in length.\nBefore, the longest file path (in the original folder) is {} characters in length.'.format(len(WORKING_DIRECTORY) + new_longest_file , len(WORKING_DIRECTORY) + old_longest_file))