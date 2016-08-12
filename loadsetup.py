'''
Author: Michael J Friedman
Created: 08/10/2016

Description:
This script loads my setups defined in setups.py, prompts the user to select
one, and then applies that setup to the workspace number passed as argument.
'''
from sys 					import argv, stdin
from shutil 			import copy2			# copy2 preserves all file metadata as well
from subprocess32 import call
from i3 					import I3
import os.path
import setups as s

# Runs terminal command and then wastes time
def run(cmd):
	call(cmd)
	I3.waste_some_time()

# Copies the initial config file to config.on-startup so it can be restored when
# the user logs out
def copy_config():
	copy2(I3.CONFIG_FILE, I3.CONFIG_FILE_BACKUP)

# Renames the workspace of the provided number w to the given name. Assumes the
# convention that workspace names are defined in variables of the form:
# $WORKSPACE#
# Returns the full name of the workspace (as named in the i3 config file)
def rename_workspace(w, new_name):
	workspace_declaration = I3.workspace_declaration(w)
	replacement 					= "%s \"%d: %s\"" % (workspace_declaration, w, new_name)
	config 								= open(I3.CONFIG_FILE, "r")
	lines 								= []
	found 								= False
	for line in config:
		if workspace_declaration in line:
			line = replacement + "\n"
			found = True
		lines.append(line)
	config.close()
	if found:
		config = open(I3.CONFIG_FILE, "w")
		for line in lines:
			config.write(line)
		config.close()
	else:
		raise Exception("Query not found in file")

#-------------------
# Main script
#-------------------
workspace_num = int(argv[1])
print "--------------------------------"
print "  Load a setup on workspace %d  " % (workspace_num)
print "--------------------------------"

# Load in user-defined setups
setups = s.create_setups()

# Prompt user to select a setup
prompt_message = "Select a setup from the following options:\n"
for i in range(0, len(setups.names())):
	prompt_message += str(i+1) + ": " + setups.names()[i] + "\n"
print prompt_message
selection = 0
num_attempts = 1
MAX_ATTEMPTS = 5
while selection not in range(1, len(setups.names()) + 1):
	try:
		selection = int(stdin.readline())
	except ValueError:
		pass
	num_attempts += 1
	if num_attempts > MAX_ATTEMPTS:
		exit("Maxed out your " + str(MAX_ATTEMPTS) + " attempts")
selection_index = selection - 1

# Rename the workspace and restart i3 to apply that name
if not os.path.isfile(I3.CONFIG_FILE_BACKUP):
	copy_config()
rename_workspace(workspace_num, setups.names()[selection_index])
I3.run("restart")
I3.run("workspace " + str(workspace_num) + ": " + setups.names()[selection_index])

# Run the commands for the selected setup
for cmd in setups.cmds(selection_index):
	parts = cmd.split(" ")
	run(parts)