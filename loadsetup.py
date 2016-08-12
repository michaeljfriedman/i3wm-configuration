'''
Author: Michael J Friedman
Created: 08/10/2016

Description:
This script loads my setups defined in setups.py, prompts the user to select
one, and then applies that setup to the workspace number passed as argument.
'''
from sys 					import argv, stdin
from subprocess32 import call
from i3 					import I3
import setups as s

# Runs terminal command and then wastes time
def run(cmd):
	call(cmd)
	I3.waste_some_time()

# Stips the newline character off the end of a line
def with_newline_stripped(text):
	NEWLINE = "\n"
	N = len(text)
	if NEWLINE == text[N-1]:
		return text[0:N-1]
	else:
		return text

# Renames the workspace of the provided number w to the given name
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
prompt_select_setup_msg = "Select a setup from the following options:\n"
for i in range(0, len(setups.names())):
	prompt_select_setup_msg += str(i+1) + ": " + setups.names()[i] + "\n"
print prompt_select_setup_msg
selection = 0
num_attempts = 1
MAX_ATTEMPTS = 5
while selection not in range(1, len(setups.names()) + 1):
	if num_attempts > MAX_ATTEMPTS:
		I3.nagbar("Maxed out your " + str(MAX_ATTEMPTS) + " attempts")
		exit()
	try:
		selection = int(stdin.readline())
	except ValueError:
		pass
	num_attempts += 1
selection_index = selection - 1

# Rename the workspace and restart i3 to apply that name
prompt_rename_workspace_msg = "Enter a name for the workspace (or leave it blank to use the setup name)"
print prompt_rename_workspace_msg
workspace_name = with_newline_stripped(stdin.readline())
if workspace_name == "":
	workspace_name = setups.names()[selection_index]
rename_workspace(workspace_num, workspace_name)
I3.msg("reload")
I3.msg("workspace " + str(workspace_num) + ": " + workspace_name)

# Run the commands for the selected setup
for cmd in setups.cmds(selection_index):
	parts = cmd.split(" ")
	run(parts)