#!/usr/bin/python

import os
import urllib
import zipfile
from sys import executable
import yaml

server_url = "http://bearpi.no-ip.org"
authserver = "http://www.berboe.co.uk"

def main():
	print "Welcome to McSIAB, the Minecraft Server In A Box app."
	print "setup.py must be run before using this program"
	main_menu()
	print
	print "Exiting"

def main_menu():
	while 1 == 1:
		print
		print "(1) Choose a Server to Use"
		print "(2) Load Test Page"
		print "(3) Exit"
		print "(4) Test Auth"
		option = raw_input("Choose an option: ")
		if option == "1":
			server_choice()
		elif option == "2":
			test_page()
		elif option == "3":
			return
		elif option == "4":
			auth()
		else:
			print "Invalid option chosen. Please try again"

def server_choice():
	serverNumber = 0
	print "Not implemented. Coming Soon."
	print
	listYAMLserver = urllib.urlopen(server_url+"/serverzips/list.yml")
	FileForParsing = yaml.load(listYAMLserver)
	for currentServer in FileForParsing:
		serverNumber += 1
		print serverNumber
		print currentServer
	print FileForParsing
	listYAMLserver.close()
			
def test_page():
	filehandle = urllib.urlopen("http://yaml.org")
	int1 = 0
	for i in filehandle.readlines():
		int1 = int1 + 1
		print "("+str(int1)+") "+i.rstrip()
	print
	return

def auth():
	print
	keyid = raw_input("Please enter your key id: ")
	keypass = getpass("Please enter your password: ")
	authhandle = urllib.urlopen(authserver+"/keyverify.php?keyid="+str(keyid)+"&keypass="+str(keypass))
	i = authhandle.readline()
	if i == "correct password":
		print "Correct ID/Pass Combination"
		return 1
	else:
		print "Something went wrong :("
		return -1

main()
