'''
Author: Michael J Friedman
Created: 08/10/2016

Description:
This module allows a client to pass in any i3 command and execute it.
'''
from subprocess32 import call as run
from sys import argv

def waste_some_time():
	for i in range(0, 10000000):
		a = 1

# Executes an i3 command
def i3cmd(cmd):
	i3_command_runner = "i3-msg"
	parts = [i3_command_runner]
	for part in cmd.split(" "):
		parts.append(part)
	run(parts)
	waste_some_time()


# Test client runs the i3 command given as argument
def main(cmd):
	i3cmd(cmd)

if argv[0] == "i3cmd.py":
	main(argv[1])