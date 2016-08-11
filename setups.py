'''
Author: Michael J Friedman
Created: 08/10/2016

Description 1:
This class defines a container for a group of "setups". These are similar to
workspaces, but are not tied to any one workspace. They hold all the contents
of a workspace - the name of the workspace, the programs/commands to run - and
are applied to a workspace using the separate script load-setup.py.

This is more powerful than simply tying programs (via their classes or
instances, for example) to a workspace via the i3 config, as I can arrange to
have one or multiple programs on multiple workspaces, but still group related
programs so they can load together on a common workspace.


Description 2:
The static function following the Setups class defines all the setups in lists.
(This is where the user specifies what to name the setup, and which
programs/commands to run.)
'''

class Setups(object):

	# Constructs a group of setups from the parallel lists names and cmds
	#
	# @param names: list of names for each setup
	# @param cmds: list of lists of commands to run when loading each setup
	def __init__(self, names=[], cmds=[]):
		if len(names) != len(cmds):
			raise Exception("Different number of names and commands in the list of setups")

		self._names = []
		for name in names:
			self._names.append(name)

		self._cmds = []
		for i in range(0, len(cmds)):
			self._cmds.append([])
			setup_cmds = cmds[i]
			for cmd in setup_cmds:
				self._cmds[i].append(cmd)

	def names(self):
		return self._names
	
	def cmds(self, i):
		return self._cmds[i]


def create_setups():
	names = [
		"Sublime"
	]

	# To run i3 commands (for instance, to split horizontally/vertically), prefix
	# the command with "i3-msg" followed by the i3 command
	# 	e.g. To split horizontally: "i3-msg split h"
	cmds = [
		["subl -n", "gnome-terminal", "i3-msg split v", "gnome-terminal"]
	]

	return Setups(names, cmds)