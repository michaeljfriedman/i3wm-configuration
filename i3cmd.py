'''
Author: Michael J Friedman
Created: 08/10/2016

Description:
This module allows a client to pass in any i3 command and execute it.
'''
from os import system as run
from sys import argv

# Executes an i3 command
def i3cmd(cmd):
	i3_command_runner = "i3-msg"
	run(i3_command_runner + " " + cmd)


# Test client runs the i3 command given as argument
def main(cmd):
	i3cmd(cmd)

if argv[0] == "i3cmd.py":
	main(argv[1])