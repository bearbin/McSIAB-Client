import urllib

def download_zip(url, saveLocation):
    
    #
    # Downloads a zip fron the specified URL and saves it to the specified location.
    #
    # url          : The URL of the zip file to be downloaded.
    # saveLocation : Where the downloaded zip is to be saved.
    #

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
