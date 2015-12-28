import requests
import argparse

coolurl = ""

parser = argparse.ArgumentParser(description="Scanner de tipo de servidor")
parser.add_argument('-u', '--url', dest="coolurl", help="Especifica la URL a scanear", required=True)

arguments = parser.parse_args()

if arguments.coolurl:
	request = requests.get(url=arguments.coolurl, verify=False)
	headers = dict(request.headers)


	if headers["Server"]:
		print "El server es: {}".format(headers["Server"])
	else:
		print "No se ha detectado el tipo de servidor"