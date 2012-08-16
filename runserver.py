import os
import zipfile
import askquestion
import downloadzip
import nukedir

def run_server(serverObjectToRun, serverURL):
	print "Downloading server zip."
	downloadzip.download_zip(serverURL+"/serverzips/"+serverObjectToRun['zip-name'], serverObjectToRun['zip-name'])
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
		userChoiceServerCleanup = askquestion.ask_question("Do you want to clean up (yes/no): ", 4)
		if userChoiceServerCleanup == True:
			print "Deleting server data..."
			nukedir.nukedir(serverObjectToRun['zip-name'].strip('.zip'))
			print "Cleaned up."
			break
		else:
			print "Server data not deleted. Returning to server list."
			break
	return
