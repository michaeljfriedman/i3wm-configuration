'''
Author: Michael J Friedman
Created: 08/12/2016

Description:
This script, to be executed upon logging out of i3, resets all the workspace
names to their defaults (as specified in the list "DEFAULT_NAMES").
'''

from i3 import I3

config = open(I3.CONFIG_FILE, "r")
lines = []
current_workspace = 1
for line in config:
	if I3.workspace_declaration(current_workspace) in line:
		line = "%s \"%s\"\n" % (I3.workspace_declaration(current_workspace),
														I3.WORKSPACE_NAMES_DEFAULT[current_workspace - 1])
		current_workspace += 1
	lines.append(line)
config.close()
config = open(I3.CONFIG_FILE, "w")
for line in lines:
	config.write(line)
