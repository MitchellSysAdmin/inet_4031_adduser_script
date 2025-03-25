#!/usr/bin/python3

# INET4031
# Matthew Mitchell
# Date Created: 03/24/25
# Date Last Modified: 03/24/25

#Imports os module to interact with the os.
#Imports re module to use regular expressions.
#Imports sys module to access system-specific parameters and functions like i/o.
import os
import re
import sys

#Begins he main function and reads from the input file.

def main():
    for line in sys.stdin:

        #Uses a regular expression to search for lines starting with a comment and stores them.
        match = re.match("^#",line

        #Splits the data fields separated by : and stores them in an array.
        fields = line.strip().split(':')

        #The IF statement checks to see if the line was a comment or if there are not 5 data fields.
        #If either is true, then it ignores that line and continues on to the next line of the input file.
        #This script must have exactly 5 data fields and comments are not needed for operation.
        if match or len(fields) != 5:
            continue

        #Stores the username, password, and account info to put in the passwd file when creating the account.
        username = fields[0]
        password = fields[1]
        gecos = "%s %s,,," % (fields[3],fields[2])

        #Splits the data field containing the groups into an array to add user to each group later.
        groups = fields[4].split(',')

        #Informs the user that it is now creating the account for transparency and to identify if there is an issue.
        print("==> Creating account for %s..." % (username))
        #Builds the command to create the user account with the user info and no password. Stores it to run later.
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

        #Command to add the user is commented out for testing the script.
        #If uncommented, the os.system(cmd) statement will attempt to create the user using the command above.
        #print cmd
        #os.system(cmd)

        #Informs user that the password is now being set for that username. Helps with transparency and debugging.
        print("==> Setting the password for %s..." % (username))
        #Builds the command to set the password for the username
	#Uses echo to output password twice without a new line after.
	#Pipes that output and uses sudo to set the password for the username, entering password twice to confirm.
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

        #Command to set the password for the username is commented out for testing the script.
	#If uncommented, the os.system(cmd) statement will attempt to set the password using the command above.
        #print cmd
        #os.system(cmd)

        for group in groups:
            #The IF statement looks at each group in the groups array to add the user to those groups.
            #If the name of the group is not a dash which indicates no group, then it will add the group.
	    #It will also inform the user it is adding the username to the group for transparency and debugging.
            if group != '-':
                print("==> Assigning %s to the %s group..." % (username,group))
                cmd = "/usr/sbin/adduser %s %s" % (username,group)
                #print cmd
                #os.system(cmd)

if __name__ == '__main__':
    main()
