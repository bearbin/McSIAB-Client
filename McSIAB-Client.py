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

main()
