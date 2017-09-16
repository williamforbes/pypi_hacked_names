import subprocess
import time
import platform

# "We are checking for malicious libraries that may have been inserted onto your computer through a PyPi mislabeling technique"
#"Note, this program was written to support python version 2.7.x"

print "You are using python verison: " + platform.python_version()

pip_version = subprocess.check_output(['pip', '--version'])
print "You are using  pip (the PyPi installer) version: " + pip_version

full_output = raw_input("Do you want to see the full output? (Y or N)").lower()
is_verbose = False
if full_output == "y" or full_output=="yes":
	is_verbose = True
print ""

array_bad_names  = ["acqusition","apidev-coop","bzip","crypt","django-server","pwd","setup-tools","telnet","urlib3","urllib","requests"]
your_bad_libraries = []

pip_listing = subprocess.check_output(['pip', 'list','--format=legacy']).splitlines()

for name in pip_listing:
	was_name_hacked = False
	for hack in array_bad_names:
		if hack in name:
			was_name_hacked = True
	
	if was_name_hacked == True:		
		your_bad_libraries.append(name)
		print name + "\t"+ '\x1b[0;30;41m' + 'bad' + '\x1b[0m'
		time.sleep(.4)

	elif is_verbose:
		print name + "\t"+ '\x1b[6;30;42m' + 'good' + '\x1b[0m'
		time.sleep(.1)
	
print ""

print ("Done reviewing libraries...")

if len(your_bad_libraries) > 0:
	for item in your_bad_libraries:
		print "potential hack: "+ item + " to remove this, type in the following command: "
		print "pip uninstall " + item.split(" ")[0]
		print "Then, install the proper library"
		
	print ("\n")


print ("We would love to have ou contribute to the project if you are interested in doing more") 
