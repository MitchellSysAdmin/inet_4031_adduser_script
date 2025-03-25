---
# **INET4031 Add Users Script and User List**
---
## Program Description
Detailed and helpful description paragraph goes here. Describe how the program will help the user. It should talk about how the program is an automated way for the user to accomplish the manual task of adding users. Also include a description of what commands a user would normally use to add a user and then describe how those SAME COMMANDS are used by the script and automated.
This program is designed to automate the process of adding users to a Linux system. Doing so will save time and prevent accidental errors that could occur when doing it manually. 

Normally a user would need to run:
1. `sudo adduser <username>` to add a user then imput in the user's information manually.
2. `grep <username> /etc/passwd` to verify user was added
3. `sudo addgroup <groupname>` to create a new group if one is needed.
4. `sudo adduser <username> <groupname>` to add the user to a group.
5. `grep <groupname> /etc/group` or `groups <username>` to verify that the user is in the group.
---
## Program User Operation
---
To use this program, it must have a separate input file. 
This input file will be redirected into the script which will then process it line by line.
The following sections describe what is needed for the input file and the program's execution.
---
### Input File Format
---
The input file consists of a list of users with each user on their line.
Each line lists the fields for that user separated by colons ":".
If the user has multiple groups, they will be listed next to each other in the same field and separated by a comma ",".
Each user line should be in the following format:
- username:password:lastname:firstname:groups

Each of these fields correspond to what is needed to be added into the passwd file.
If the user wants to skip a line, then they must edit the input file and put a # at the beginning of the line to skip.
If the user does not want a user added to any group, then they must edit the input file and put a - in the groups field.
---
### Command Excuction
The Python file may need the permission to execute by the user with `chmod +x create-users.py`
The script can be run by using the following command:
`sudo ./create-users.py < create-users.input`
---
### "Dry Run"
---
If the user does a dry run, the program's logic will execute but will not make any changes to the system.
Users should do a dry run to test the script out first and make sure it works as expected.
To do this, the program can be modified with:
1. Running the command `sudo nano create-users.py` or `sudo vi create-users.py`
2. Commenting out the os.system(cmd) lines with a #.
3. Removing the # fom the lines with test print statements.
4. Exiting the editor and running the command `sudo ./create-users.py < create-users.input`
---
