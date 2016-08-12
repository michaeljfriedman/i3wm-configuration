'''
Author: Michael J Friedman
Created: 08/12/2016

Description:
This is a static class that holds constants and functions related to i3. Replaces and improves the i3cmd module
'''
from subprocess32 import call


class I3(object):

	# Constants
	I3_DIRECTORY 						= "/home/michael/.config/i3/"
	CONFIG_FILENAME 				= "config"
	CONFIG_FILE 						= I3_DIRECTORY + CONFIG_FILENAME
	CONFIG_FILE_BACKUP 			= CONFIG_FILE + ".on-startup"
	DEFAULT_WORKSPACE_NAMES = [
		# Home
		"1: Home",						# Browsing, music, recreation
		
		# School
		"2: Psets",						# Psets
		"3: Study",						# Reviewing notes/readings
		"4: Writing",					# Papers/written work
		"5: Exams",						# Practice exams
		
		# Code
		"6: Sublime",					# Projects using ST editor
		"7: Android Dev",			# Developing Android apps
		"8: LaTeX",						# LaTeX docs

		# Music
		"9: Music Prod",			# Recording & editing music
		"10: Piano",					# Reading music, practicing w/ videos
		"11: Composing",			# Composing/arranging music
		"12: Music Player",		# Any music playing

		# Misc.
		"13: Messaging",			# Any messaging services
		"14: Games",					# Gaming

		# Un-purposed
		"15",
		"16",
		"17",
		"18",
		"19",
		"20"
	]

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