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
            # Extract file from server.
            serverZip.extract(name)
            # Try and chmod the file to be WRX for everybody. (If file is a directory, this will fail)
            os.chmod(name, 0777)
        except IOError:
            # Bit of code that might not be needed, but I'm not removing it because it might be important.
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
            # Deletes server directory and files inside.
            nukedir.nukedir(serverObjectToRun['zip-name'].strip('.zip'))
            print "Cleaned up."
            break
        else:
            print "Server data not deleted. Returning to server list."
            break
    return
