#!/usr/bin/python

import os
import urllib
import sys
import zipfile
import nukedir

def main():
    print "Root required to run script - make sure to use."
    raw_input("Press enter to confirm continuing.")
    print "Installing PyYAML"
    install_yaml()
    print "Installing requests."
    install_requests()
    return

def install_yaml():
    yaml_zip_url = urllib.urlopen("http://pyyaml.org/download/pyyaml/PyYAML-3.10.zip")
    localFile = open("PyYAML.zip", "wb")
    print "Downloading ZipFile"
    while 1:
        packet = yaml_zip_url.read()
        print "Downloading..."
        if not packet:
            break
        localFile.write(packet)
    print "Downloaded."
    localFile.close()
    yaml_zip_url.close()
    yamlzip = zipfile.ZipFile("PyYAML.zip")
    print "Extracting PyYAML.zip"
    yamlzip.extractall()
    print "Installing"
    os.system("cd PyYAML-3.10 && "+sys.executable+" setup.py --without-libyaml install")
    print "Installed"
    print "Cleaning Up"
    print "Deleting Directories"
    nukedir.nukedir("PyYAML-3.10")
    print "Deleting ZipFile"
    yamlzip.close()
    os.remove("PyYAML.zip")
    print "Cleaned Up!"
    return

def install_requests():
    requests_url = urllib.urlopen("http://pi.berboe.co.uk/files/requests.zip")
    localFile = open("requests.zip", "wb")
    print "Downloading ZipFile"
    while 1:
        packet = requests_url.read()
        print "Downloading..."
        if not packet:
            break
        localFile.write(packet)
    print "Downloaded."
    localFile.close()
    requests_url.close()
    requestszip = zipfile.ZipFile("requests.zip")
    print "Extracting requests.zip"
    requestszip.extractall()
    print "Installing"
    os.system("cd requests && "+sys.executable+" setup.py install")
    print "Installed"
    print "Cleaning Up"
    print "Deleting Directories"
    nukedir.nukedir("requests")
    print "Deleting ZipFile"
    requestszip.close()
    os.remove("requests.zip")
    print "Cleaned Up!"
    return

main()
