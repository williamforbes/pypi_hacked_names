#!/usr/bin/env python2

import subprocess
import time
import platform
import json

# "We are checking for malicious libraries that may have been inserted onto your computer
#  through a PyPi mislabeling technique"

# Extra context for you as you.
print "python version: " + platform.python_version()
print "pip version: " + subprocess.check_output(['pip', '--version'])

# Visual interface because.
full_output = raw_input("Do you want to see the full output? (Y or N) : ").lower()
is_verbose = False
if full_output == "y" or full_output=="yes":
	is_verbose = True

print ""

with open('malicious_names.json') as malicious_file:
	malicious_names = json.load(malicious_file)

# Storing malicious libraries for the end.
your_bad_libraries = []
pip_listing = subprocess.check_output(['pip', 'list','--format=columns']).splitlines()

for name in pip_listing:
	was_name_hacked = False
	for hack in malicious_names:
		if hack["malicious_name"] in name:
			print hack["malicious_name"] + " was found in " + name
			was_name_hacked = True
	
	if was_name_hacked == True:		
		your_bad_libraries.append(name)
		print name + "\t"+ '\x1b[0;30;41m' + 'bad' + '\x1b[0m'
		time.sleep(.1)

	elif is_verbose:
		print name + "\t"+ '\x1b[6;30;42m' + 'good' + '\x1b[0m'
		time.sleep(.05)
	
print ""
print ("Done reviewing libraries...")

if len(your_bad_libraries) > 0:
	print "potential hacks: "
	for item in your_bad_libraries:
		print "pip uninstall " + item.split(" ")[0]
	print ("\n")

else:
	print "No malicious libaries found!"
