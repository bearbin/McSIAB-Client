import urllib

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
