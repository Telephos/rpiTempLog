#!/usr/bin/python

import subprocess, sys

#Use this if you want to run it with a command line argument.
#command = sys.argv[1:]
command = "vcgencmd measure_temp"

subprocess.run(command, shell = True, executable="/bin/bash")