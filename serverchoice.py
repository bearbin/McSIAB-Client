import askquestion
import fetchserverlist
import runserver

def server_choice(platformInfo, serverURL):
    print "This feature is under development. It does not do its final procedure yet."
    print
    serverListObject = fetchserverlist.fetch_serverlist(serverURL)
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
        if str(chosenServerInfo['os']) not in [platformInfo['currentos'], 'any']:
            print "This server is not compatible with your OS, it requires: "+str(chosenServerInfo['os'])
            raw_input("Press enter to continue.")
            continue
        if str(chosenServerInfo['processortype']) not in [platformInfo['currentprocessor'], 'any']:
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
            runserver.run_server(chosenServerInfo, serverURL)
            print "Server running completed."
            raw_input("Press enter to continue. ")
            continue
        else:
            print "Returning to server list..."
            continue
    return
