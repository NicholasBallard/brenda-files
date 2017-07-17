import os, shutil, pprint

os.chdir(r'c:\users\nicholasericballard\desktop')

# copy directory to working directory
try:
    shutil.copytree('2017', 'workThisDirectory')
except FileExistsError:
    print("The folder already exists.")

original_folder_names = list()
shortened_folder_names = list()
absolute_file_paths = list()
shortened_file_paths = list()

# THE ORIGINAL DIRPATH
# TODO: refactor 'workThisDirectory' to be a constant
for dirpath, directories, files in os.walk('workThisDirectory'):
    for file in files:
        original_folder_names.append( dirpath )

# THE SHORTENED DIRPATH
shortened_folder_names = list(original_folder_names)
for dirpath in range(len(shortened_folder_names)):
    shortened_folder_names[dirpath] = shortened_folder_names[dirpath].split('\\')
# shorten the folder names but leave the root alone
for dirpath in range(len(shortened_folder_names)):
    # change root
    shortened_folder_names[dirpath][0] = 'newWorkThisDirectory'
    for folder in range(1, len(shortened_folder_names[dirpath])):
        # TODO: replace [:5] with a constant at the top
        shortened_folder_names[dirpath][folder] = shortened_folder_names[dirpath][folder][:5].rstrip()
# stitch the dirpaths back together
for dirpath in range(len(shortened_folder_names)):
    shortened_folder_names[dirpath] = '\\'.join(map(str, shortened_folder_names[dirpath]))

# THE ORIGINAL FULL FILEPATH
for dirpath, directories, files in os.walk('workThisDirectory'):
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