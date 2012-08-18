import urllib
import yaml

def fetch_serverlist(serverURL):
    #
    # Fetches the information YAML file, parses it and returns a python opject with the data inside.
    #
    # serverURL : The URL of the server hosting the server list.
    #

    yamlFileOnServer = urllib.urlopen(serverURL+"/serverzips/list.yml")
    parsedFile = yaml.load(yamlFileOnServer)
    yamlFileOnServer.close()
    return parsedFile
