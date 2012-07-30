#!/usr/bin/python

import os
import urllib
import sys
import zipfile

def main():
	print "Root required to run script - make sure to use."
	raw_input("Press enter to confirm continuing.")
	print "Installing PyYAML"
	install_yaml()
	return

def install_yaml():
	yaml_zip_url = urllib.urlopen("http://pyyaml.org/download/pyyaml/PyYAML-3.10.zip")
	localFile = open("PyYAML.zip", "wb")
	print "Downloading ZipFile"
	while 1:
		packet = yaml_zip_url.read()
		print "Downloading..."
		if not packet:
			break
		localFile.write(packet)
	print "Downloaded."
	localFile.close()
	yaml_zip_url.close()
	yamlzip = zipfile.ZipFile("PyYAML.zip")
	print "Extracting PyYAML.zip"
	yamlzip.extractall()
	print "Installing"
	os.system("cd PyYAML-3.10 && "+sys.executable+" setup.py --without-libyaml install")
	print "Installed"
	print "Cleaning Up"
	print "Deleting Directories"
	nukedir("PyYAML-3.10")
	print "Deleting ZipFile"
	yamlzip.close()
	os.remove("PyYAML.zip")
	print "Cleaned Up!"
	import yaml
	return

def nukedir(dir):
	if dir[-1] == os.sep: dir = dir[:-1]
	files = os.listdir(dir)
	for file in files:
		if file in ['..', '.']: continue
		path = dir + os.sep + file
		if os.path.isdir(path):
			nukedir(path)
		else:
			os.unlink(path)
	os.rmdir(dir)

main()
