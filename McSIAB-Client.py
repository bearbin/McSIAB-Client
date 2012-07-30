#!/usr/bin/python

import os
import urllib
import zipfile
from sys import executable
import yaml
import platform
import getpass

server_url = "http://bearpi.no-ip.org"
authserver = "http://www.berboe.co.uk"

def main():
	print "Welcome to McSIAB, the Minecraft Server In A Box app."
	get_system_info()
	print "setup.py must be run before using this program"
	setupRan = ask_question(['yes', 'no'], "Has setup.py been run? (yes/no): ", "You must enter a yes or no answer.")
	if setupRan == 'no':
		print "setup.py must have been run. Exiting."
		return
	main_menu()
	print
	print "Exiting"
	return

def fetch_serverlist():
	yamlFileOnServer = urllib.urlopen(server_url+"/serverzips/list.yml")
	parsedFile = yaml.load(yamlFileOnServer)
	yamlFileOnServer.close()
	return parsedFile

def main_menu():
	while 1:
		print
		print "(1) Choose a Server to Use"
		print "(2) Test Authentication"
		print "(3) Exit"
		option = ask_question(['1', '2', '3'], "Choose an option: ", "Please enter a value in the range of options.")
		if option == "1":
			server_choice()
		elif option == "2":
			auth()
		elif option == "3":
			break
	return

def server_choice():
	print "This feature is under development. It does not do its final procedure yet."
	print
	serverListObject = fetch_serverlist()
	while 1 == 1:
		serverNumber = 0
		for currentServer in serverListObject:
			serverNumber += 1
			print "("+str(serverNumber)+"): "+currentServer['name']
		serverOptionToUse = raw_input("Please enter the server you wish to use: ")
		try:
			int(serverOptionToUse)
		except ValueError:
			raw_input("Please enter a valid integer. Press enter to try again.")
			continue
		adjustedServerOption = int(serverOptionToUse) -1
		if adjustedServerOption < len(serverListObject) and adjustedServerOption > -1:
			chosenServerInfo = serverListObject[adjustedServerOption]
			if str(chosenServerInfo['os']) not in [currentos, 'any']:
				print "This server is not compatible with your OS, it requires: "+str(chosenServerInfo['os'])
				raw_input("Press enter to continue.")
				continue
			if str(chosenServerInfo['processortype']) not in [currentprocessor, 'any']:
				print "This server is not compatible with your processor, it requires the "+str(chosenServerInfo['processortype'])+" architecture."
				continue
			print "Information on server: "+serverOptionToUse
			print "Server Name	: "+str(chosenServerInfo['name'])
			print "Server Type	: "+str(chosenServerInfo['server-type'])
			print "Requires Java	: "+str(chosenServerInfo['requires-java'])
			print "User-Update?	: "+str(chosenServerInfo['user-update'])
			runServerDecision = ask_question(['yes', 'no'], "Do you wish to run this server (yes/no): ", "You must answer a yes or no answer.")
			if runServerDecision == 'yes':
				print "Running Server."
				run_server(chosenServerInfo)
				print "Server running completed."
				raw_input("Press enter to continue. ")
				continue
			else:
				print "Returning to server list..."
				continue
	return
			
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
	keypass = getpass.getpass("Please enter your password: ")
	authhandle = urllib.urlopen(authserver+"/keyverify.php?keyid="+str(keyid)+"&keypass="+str(keypass))
	i = authhandle.readline()
	if i == "correct password":
		print "Correct ID/Pass Combination"
		return 1
	else:
		print "Something went wrong :("
		return -1

def get_system_info():
	global currentos
	global currentprocessor
	print "Getting system info:"
	print "Getting OS..."
	currentos = platform.system()
	print "OS is: "+currentos
	print "Getting processor type..."
	currentprocessor = platform.machine()
	print "Processsor type is: "+currentprocessor
	print "System info collected."
	return

def run_server(serverObjectToRun):
	print "Downloading server zip."
	download_zip(server_url+"/serverzips/"+serverObjectToRun['zip-name'], serverObjectToRun['zip-name'])
	print "Extracting server zip."
	serverZip = zipfile.ZipFile(serverObjectToRun['zip-name'])
	for name in serverZip.namelist():
		try:
			serverZip.extract(name)
			os.chmod(name, 0777)
		except IOError:
			serverZip.extract(name)
	print "Server zip extracted. Deleting now..."
	os.remove(serverObjectToRun['zip-name'])
	print "Server zip deleted. Running server."
	runCommand = serverObjectToRun['run-command']
	os.system(runCommand)
	print "Server running completed. Cleaning up."
	while 1:
		userChoiceServerCleanup = ask_question(['yes', 'no'], "Do you want to clean up (yes/no): ", "You must use a yes or no answer")
		ifif userChoiceServerCleanup == 'yes':
			print "Deleting server data..."
			nukedir(serverObjectToRun['zip-name'].strip('.zip'))
			print "Cleaned up."
			break
		else:
			print "Server data not deleted. Returning to server list."
			break
	return

def download_zip(url, saveLocation):
	print "Zip Download Started."
	zipToDownload = urllib.urlopen(url)
	localFile = open(saveLocation, 'wb')
	print "Downloading..."
	while 1:
		packet = zipToDownload.read()
		print "Downloading..."
		if not packet:
			break
		localFile.write(packet)
	print str(saveLocation)+" Downloaded."
	return

def nukedir(dir):
	if dir[-1] == os.sep: dir = dir[:-1]
	files = os.listdir(dir)
	for file in files:
		if file in ['.', '..']: continue
		path = dir + os.sep + file
		if os.path.isdir(path):
			nukedir(path)
		else:
			os.unlink(path)
	os.rmdir(dir)		

def ask_question(answers, questionText, errorText):
	while 1:
		userAnswerGiven = raw_input(questionText)
		if userAnswerGiven not in answers:
			print errorText
			raw_input("Press enter to continue.")
			continue
		else:
			return userAnswerGiven
	return -1

main()
