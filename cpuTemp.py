#!/usr/bin/python

import subprocess, sys

#Use this if you want to run it with a command line argument. Add
#command = sys.argv[1:]

#1st cut extracts tempt number with unit, second cut gets only first 4 bytes.
command = r'vcgencmd measure_temp | cut -d= -f2 | cut -b 1-4'

subprocess.run(command, shell = True, executable="/bin/bash")