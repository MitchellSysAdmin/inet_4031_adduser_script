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
	#Forces the code to read directly from terminal first to check for user input before reading the file.
	#After the user inputs their choice, it checks to see if input is a terminal (hence atty() function)
	#If not at terminal, it reads the redirected file and stores it in a variable to read from instead.
	with open("/dev/tty", "r") as tty:
		print("Do a dry run? y/n: ", end="", flush=True)
		test = tty.readline().strip()
	if not sys.stdin.isatty():
		redirected_file_contents = sys.stdin.read()
		for line in redirected_file_contents.splitlines():

			#Uses a regular expression to search for lines starting with a comment and stores them.
			match = re.match("^#",line)
			#The IF statement checks to see if the line was a comment and skips if so.
			if match:
				if test == 'y':
					print("\nUser entry marked to be skipped.")
				continue

			#Splits the data fields separated by : and stores them in an array.
			fields = line.strip().split(':')
			#IF statement checks if there are not 5 data fields.
			if len(fields) != 5:
				if test == 'y':
					print('\nError: Number of fields for user entry is not 5. Skipping user')
				continue

			#Stores the username, password, and account info to put in the passwd file when creating the account.
			username = fields[0]
			password = fields[1]
			gecos = "%s %s,,," % (fields[3],fields[2])

			#Splits the data field containing the groups into an array to add user to each group later.
			groups = fields[4].split(',')

			#Informs the user that it is now creating the account for transparency and to identify if there is an issue.
			print("\n==> Creating account for %s..." % (username))
			#Builds the command to create the user account with the user info and no password. Stores it to run later.
			cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (gecos,username)

			#Command to add the user is commented out for testing the script.
			#If uncommented, the os.system(cmd) statement will attempt to create the user using the command above.
			if test == 'y':
				print('Command to be run: ', cmd)
			if test == 'n':
				os.system(cmd)

			#Informs user that the password is now being set for that username. Helps with transparency and debugging.
			print("\n==> Setting the password for %s..." % (username))

			#Builds the command to set the password for the username
			#Uses echo to output password twice without a new line after.
			#Pipes that output and uses sudo to set the password for the username, entering password twice to confirm.
			cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (password,password,username)

			#Command to set the password for the username is commented out for testing the script.
			#If uncommented, the os.system(cmd) statement will attempt to set the password using the command above.
			if test == 'y':
				print('Command to be run', cmd)
			if test == 'n':
				os.system(cmd)

			#If test mode enabled, states the groups user is in
			if test == 'y':
				print('\nUser is in these groups: ', groups)

			for group in groups:
				#The IF statement looks at each group in the groups array to add the user to those groups.
				#If the name of the group is not a dash which indicates no group, then it will add the group.
				#It will also inform the user it is adding the username to the group for transparency and debugging.
				if group != '-':
					print("\n==> Assigning %s to the %s group..." % (username,group))
					cmd = "/usr/sbin/adduser %s %s" % (username,group)
				if test == 'y':
					print('Command to be run: ', cmd)
				if test == 'n':
					os.system(cmd)

if __name__ == '__main__':
    main()
