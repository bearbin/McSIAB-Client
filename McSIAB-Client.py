#!/usr/bin/python

# import os
import urllib
import zipfile
from sys import executable
import platform
import getpass
# import nukedir
import askquestion
import serverchoice

server_url = "http://bearpi.no-ip.org"
authserver = "http://www.berboe.co.uk"

def main():
    print "Welcome to McSIAB, the Minecraft Server In A Box app."
    # Sets processor type and OS to globals 'currentos' and 'currentprocessor'
    get_system_info()
    print "setup.py must be run before using this program"
    # Asks if setup.py has been run.
    setupRan = askquestion.ask_question("Has setup.py been run? (yes/no): ", 4, badAnswerText = "Please enter a yes or no answer. ")
    if setupRan == False:
        print "setup.py must have been run. Exiting."
        return
    # Load the main menu, gateway to all the functions.
    main_menu()
    print
    print "Exiting"
    return

"""
def fetch_serverlist():
    yamlFileOnServer = urllib.urlopen(server_url+"/serverzips/list.yml")
    parsedFile = yaml.load(yamlFileOnServer)
    yamlFileOnServer.close()
    return parsedFile
"""

def main_menu():
    while 1:
        print
        print "(1) Choose a Server to Use"
        print "(2) Test Authentication"
        print "(3) Exit"
        # Asks the user what to do.
        option = askquestion.ask_question("Choose an option: ", 2, [1, 2, 3])
        if option == 1:
            serverchoice.server_choice({'currentos':currentos, 'currentprocessor':currentprocessor}, server_url)
        elif option == 2:
            # Runs default auth.
            auth()
        elif option == 3:
            break
    return

"""
def server_choice():
    serverListObject = fetch_serverlist()
    while 1 == 1:
        serverNumber = 0
        for currentServer in serverListObject:
            serverNumber += 1
            print "("+str(serverNumber)+"): "+currentServer['name']
        serverOptionToUse = askquestion.ask_question("Please enter the server you wish to use (or 0 to quit): ", 2, range(len(serverListObject)+1))
        adjustedServerOption = serverOptionToUse -1
        if adjustedServerOption == -1:
            print "Returning to main menu..."
            break
        chosenServerInfo = serverListObject[adjustedServerOption]
        if str(chosenServerInfo['os']) not in [currentos, 'any']:
            print "This server is not compatible with your OS, it requires: "+str(chosenServerInfo['os'])
            raw_input("Press enter to continue.")
            continue
        if str(chosenServerInfo['processortype']) not in [currentprocessor, 'any']:
            print "This server is not compatible with your processor, it requires the "+str(chosenServerInfo['processortype'])+" architecture."
            continue
        print "Information on server: "+str(serverOptionToUse)
        print "Server Name	: "+str(chosenServerInfo['name'])
        print "Server Type	: "+str(chosenServerInfo['server-type'])
        print "Requires Java	: "+str(chosenServerInfo['requires-java'])
        print "User-Update?	: "+str(chosenServerInfo['user-update'])
        runServerDecision = askquestion.ask_question("Do you wish to run this server (yes/no): ", 4)
        if runServerDecision == True:
            print "Running Server."
            run_server(chosenServerInfo)
            print "Server running completed."
            raw_input("Press enter to continue. ")
            continue
        else:
            print "Returning to server list..."
            continue
    return
"""		

def auth():
    print
    keyid = raw_input("Please enter your key id: ")
    keypass = getpass.getpass("Please enter your password: ")
    # Verifies user using the authserver global as server.
    authhandle = urllib.urlopen(authserver+"/keyverify.php?keyid="+str(keyid)+"&keypass="+str(keypass))
    i = authhandle.readline()
    if i == "correct password":
        print "Correct ID/Pass Combination"
        return 1
    else:
        print "Something went wrong :("
        return -1

def get_system_info():
    # Defines globals to put system information in.
    global currentos
    global currentprocessor
    print "Getting system info:"
    print "Getting OS..."
    # Gets current OS type.
    currentos = platform.system()
    print "OS is: "+currentos
    print "Getting processor type..."
    # Gets processor architecture.
    currentprocessor = platform.machine()
    print "Processsor type is: "+currentprocessor
    print "System info collected."
    return

"""
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
"""

"""
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
"""

main()
