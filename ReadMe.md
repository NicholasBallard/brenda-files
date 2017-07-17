Brenda-Files

Description: This project takes an existing directory of any number of files and shortens the "tree." The root directory - the folder every other folder and file is in - stays the same, as does the file name and extension.

Example:

"Z:\main_folder\another folder\Russian nesting doll\yadda yadda\investment board report.xlsx"

Becomes:

"Z:\main_\anoth\Russi\yadda\investment board report.xlsx"

In the terminal output when done, the program prints the new longest directory length versus the longest directory length of the original folder.

'''
Terminal:
The longest file is a total of 57 characters in length.
Before, the longest file path (in the original folder) is 90 characters in length.
'''

If the copy of the directory is already made by running this script before, the try loop will print a message saying the directory already exists and will skip re-creating the folder, and continue running the rest of the script.

'''
Terminal:
The fodler already exists.
'''

Steps:

**The script file "app.py" in "brenda-files" can be opened by any text editor. Right-click the file >> Open With >> [Sublime Text 3, Notepad, IDLE, Visual Studio Code, etc.]

1 ==>> Make sure to work on a copy of the folder, not the original! Just in case...

2 ==>> Set the working directory for Brenda's computer. Copy the Z:\\ ("the Z Drive") to the desktop. The program will make yet another copy of this folder just in case, and work off that.

3 ==>> Determine how many characters in each subfolder's name to keep. Set to 5, ".\Russian nesting doll\" becomes ".\Russi\". The root folder and file name remain the same.

4 ==>> Save the script file and run.

NOTE: To run a script file, in this case in the programming language called Python, (1) the program Python needs to be installed on your computer. (2) The dependencies need to be available in your environment. For example, this script "brenda-files/app.py" uses three "modules" - programs created by others to get the work done. In this case, "os", which allows Python to manipulate the file system of its running environment; "shutil", a library for doing high level file manipulation (think copying files and folders); "pprint", used in testing, which "pretty prints" output in the terminal window. Helpful when printing nested lists.

If Python is saved in the computer's PATH (hit Windows key, type "environment variables" and hit enter on the choice to change environment variables), the you can run the script using the RUN command.

WINDOWS KEY + R (hold the Windows key, then press R once)
In the little text box on the bottom left, type this:
python3 app.py

But! This might take too much troubleshooting. Would be more useful if Brenda-Files was made in a virtual environment or a container. Will have to do some debugging. So best to right-click the file "app.py" in the folder "brenda-files", open with IDLE which is the editor that comes with the Python distribution already downloaded to your computer, and then run the script by pressing F5, or in the menu bar, Run >> Run Module.

Then when done, drag the folder the program created to your cloud backed up directory. In English, this means copy this shortened folder to the "Blue Cloud" - Microsoft OneDrive, where it says "OneDrive - Kerrville Independent School District".

Good luck! :)