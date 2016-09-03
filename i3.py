'''
Author: Michael J Friedman
Created: 08/12/2016

Description:
This is a static class that holds constants and functions related to i3. Replaces and improves the i3cmd module
'''
from subprocess32 import call
import workspacenames


class I3(object):

	# ----Set this to one of the lists you defined in workspacenames.py----
	WORKSPACE_NAMES_DEFAULT = workspacenames.workspace_names_desktop

	# Constants
	I3_DIRECTORY 						= "/home/michael/.config/i3/"
	CONFIG_FILENAME 				= "config"
	CONFIG_FILE 						= I3_DIRECTORY + CONFIG_FILENAME
	CONFIG_FILE_BACKUP 			= CONFIG_FILE + ".on-startup"

	# Returns the workspace declaration line for workspace i
	@staticmethod
	def workspace_declaration(i):
		return "set $WORKSPACE" + str(i)

	# Does a meaningless process to cause a slight delay
	@staticmethod
	def waste_some_time():
		for i in range(0, 10000000):
			a = 1

	# Runs an i3 command
	@staticmethod
	def msg(cmd):
		i3_command_runner = "i3-msg"
		parts = [i3_command_runner]
		for part in cmd.split(" "):
			parts.append(part)
		call(parts)
		I3.waste_some_time()

	# Shows an error bar at the top with the given message and (optionally)
	# a button with a corresponding shell command
	@staticmethod
	def nagbar(message, button_label="", button_cmd=""):
		i3_nagbar_runner = "i3-nagbar"
		parts = [i3_nagbar_runner, "-m", message]
		if button_label != "" and button_cmd != "":
			button_parts = ["-b", button_label, button_cmd]
			parts = parts + button_parts
		call(parts)