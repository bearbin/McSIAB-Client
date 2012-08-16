import urllib
import yaml

def fetch_serverlist(serverURL):
	yamlFileOnServer = urllib.urlopen(serverURL+"/serverzips/list.yml")
	parsedFile = yaml.load(yamlFileOnServer)
	yamlFileOnServer.close()
	return parsedFile
