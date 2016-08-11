'''
Author: Michael J Friedman
Created: 08/10/2016

Description:
This script loads my setups defined in setups.py, prompts the user to select
one, and then applies that setup to the workspace number passed as argument.
'''
from sys import argv, stdin
from shutil import copy2			# copy2 preserves all file metadata as well
from i3cmd import i3cmd
from os import system as run
import setups as s

# Returns the index of the string s in the array a
def index_of(item, a):
	for i in range(0, len(a)):
		if a[i] == item:
			return i
	return -1

# Returns the provided string with the ending newline character stripped off
def with_newline_stripped(s):
	NEWLINE = "\n"
	N = len(s)
	if N == 0:
		return s
	elif NEWLINE == s[N - 1]:
		return s[0:N - 1]
	return s

# Copies the initial config file to config.on-startup so it can be restored when
# the user logs out. Returns a reference to the copy of the file named "config"
# with rw permissions
def copy_config():
	copy2("config", "config.on-startup")
	f = open("config", "rw")
	return f

# Renames the workspace of the provided number w to the given name in the given
# config file. Assumes the convention that workspace names are defined in
# variables of the form $WORKSPACE#
def rename_workspace(w, new_name, config):
	workspace_declaration_phrase = "set $WORKSPACE" + str(w)
	for line in config:
		if workspace_declaration_phrase in line:
			line = workspace_declaration_phrase + str(w) + ": " + new_name
			# TODO: write this line to the config in place of the old line

#-------------------
# Main script
#-------------------
# Switch to the specified workspace
workspace_num = int(argv[1])
i3cmd("workspace " + str(workspace_num))

# Load in user-defined setups
setups = s.create_setups()

# Prompt user to select a setup
prompt_message = "Select a setup from the following options:\n"
for i in range(0, len(setups.names())):
	prompt_message += str(i+1) + ": " + setups.names()[i] + "\n"
print prompt_message
selection = ""
num_attempts = 1
MAX_ATTEMPTS = 5
while with_newline_stripped(selection) not in setups.names():
	selection = stdin.readline()
	num_attempts += 1
	if num_attempts > MAX_ATTEMPTS:
		exit("Maxed out your " + str(MAX_ATTEMPTS) + " attempts")
selection_index = index_of(selection, setups.names())

# Rename the workspace and restart i3 to apply that name
# rename_workspace(workspace_num, setups.names()[selection_index], copy_config())
# i3cmd("restart")

# Run the commands for the selected setup
for cmd in setups.cmds(selection_index):
	run(cmd)