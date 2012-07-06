#!/usr/bin/python

import os
import urllib

server_url = "http://bearpi.no-ip.org"
authserver = "http://www.berboe.co.uk"

def main():
	print "Welcome to McSIAB, the Alleyns Minecraft Server In A Box app."
	raw_input("Press enter to continue")
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
	print "Not implemented. Coming Soon."
	print
	return 1
	keyid = raw_input("Please enter your key id: ")
	keypass = raw_input("Please enter your password: ")
	
			
def test_page():
	filehandle = urllib.urlopen(server_url+"/bottombar.php")
	int1 = 0
	for i in filehandle.readlines():
		int1 = int1 + 1
		print "("+str(int1)+") "+i.rstrip()
	print
	return

def auth():
	print
	keyid = raw_input("Please enter your key id: ")
	keypass = raw_input("Please enter your password: ")
	authhandle = urllib.urlopen(authserver+"/keyverify.php?keyid="+str(keyid)+"&keypass="+str(keypass))
	i = authhandle.readline()
	if i == "correct password":
		print "Correct ID/Pass Combination"
		return 1
	else:
		print "Something went wrong :("
		return -1;

main()
