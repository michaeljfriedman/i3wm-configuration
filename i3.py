'''
Author: Michael J Friedman
Created: 08/12/2016

Description:
This is a static class that holds constants and functions related to i3. Replaces and improves the i3cmd module
'''
from subprocess32 import call


class I3(object):

	# Constants
	I3_DIRECTORY 					= "/home/michael/.config/i3/"
	CONFIG_FILENAME 			= "config"
	CONFIG_FILE 					= I3_DIRECTORY + CONFIG_FILENAME
	CONFIG_FILE_BACKUP 		= CONFIG_FILE + ".on-startup"
	WORKSPACE_DECLARATION = "set $WORKSPACE"

	# Returns the workspace declaration line for workspace i
	@staticmethod
	def workspace_declaration(i):
		return I3.WORKSPACE_DECLARATION + str(i)

	# Does a meaningless process to cause a slight delay
	@staticmethod
	def waste_some_time():
		for i in range(0, 10000000):
			a = 1

	# Runs an i3 command
	@staticmethod
	def run(cmd):
		i3_command_runner = "i3-msg"
		parts = [i3_command_runner]
		for part in cmd.split(" "):
			parts.append(part)
		call(parts)
		I3.waste_some_time()