The FileSystem class is a simplified representation of a file system. It provides methods for creating directories (mkdir), changing the current directory (cd), listing the contents of the current directory (ls), creating files (touch), writing to files (echo), reading from files (cat), moving files or directories (mv), copying files (cp), and deleting files or directories (rm). Also, for saving the file , type "exit save file_name.json", here file_name.json is the file where your state will be saved. And, to load the file type "load_state file_name.json", here the file_name is the name of saved json file that will be loaded in the system.

Data Structures:
The FileSystem class uses a tree data structure to represent the file system hierarchy. Each node in the tree represents a file or a directory. The root of the tree is the root directory of the file system.

Each node in the tree is an instance of the Node class. The Node class has properties for the name of the file or directory, its parent node, its children nodes (if it's a directory), and its content (if it's a file).

The FileSystem class also maintains a reference to the current directory node, which is updated when the cd method is called.

Design Decisions
The decision to use a tree data structure was based on the hierarchical nature of file systems. A tree allows us to easily model the parent-child relationships between directories and files.

The Node class was designed to be flexible enough to represent both files and directories. This was achieved by giving each node a children property (which is used if the node is a directory) and a content property (which is used if the node is a file).



HOW TO RUN THE CODE:

a) You need to have Python on your system

To install Python on Windows, if you don't have it already:

Windows

1)Visit the official Python website's download page at https://www.python.org/downloads/.
2)Click on the button that says "Download Python" followed by the version number. As of writing, the latest version is Python 3.10.0.
3)Once the executable file is downloaded, run it. This will open the Python install wizard.
4)In the first screen of the installation wizard, check the box at the bottom that says "Add Python 3.x to PATH". This will allow you to use the python command directly in your terminal.
5)Click "Install Now" to start the installation process.
6)Once the installation is complete, you can verify the installation by opening a new terminal window and typing python --version. This should display the version of Python that you just installed.

b) Then Open the folder in any IDE, type command "python main.py"



HOW TO RUN THE UNIT TESTS:

1) To run the unit tests, type "python -m unittest test_file.py"



Steps to test the file:

1)To create a directory named "dir1" - mkdir dir1

2)To change the current directory to another directory to "dir1" - cd/dir1

3)To go to parent directory - cd ..

4)To go to root directory - cd /

5)To go to a inside a directory or relative path : dir1 -> dir2 - cd ../dir2

6)To create a new file - touch file.txt

7)To write a text to a file - echo "Hello World" file.txt

8)Move file(file.txt) from one directory(dir1) to another directory(dir2) - mv /dir1/file /dir2

9)Copy file(file.txt) from one directory(dir1) to another directory(dir2) - cp /dir1/file /dir2

10)Remove a file or directory - rm file1

11)To save a state to a json file (state.json) - exit save state.json

12)To load a state from json file (state.json) - load_state state.json




















