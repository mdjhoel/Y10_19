'''
myapi.py 
- simple program to demo using a web API with requests Python module
- also uses json Python module to demo how to access parts of received data
- secondary function to demo how to write out received data to an HTML file 
'''

import requests
import json

# Find APIs at - https://apilist.fun/
# some will require an API key

# cool geo example
# https://geo-info.co/?ref=apilist.fun
# example - https://geo-info.co/43.65,-79.40

# cool funny example
# https://funtranslations.com/api/chef
# https://api.funtranslations.com/translate/chef.json?text=I%20like%20upper%20canada%20college

def writeHTML(data):
	myfile = open("myapi.html","w")
	myfile.write("<h1>JSON file returned by API call</h1>")
	myfile.write("<p>Copy and paste to <a href='https://jsoneditoronline.org/'>JSON editor</a> for pretty format.</p>")
	myfile.write(data)
	myfile.close()

def main():
	# use API to get place info
	response = requests.get("https://geo-info.co/43.65,-79.40")

	# if API call is correct
	if (response.status_code == 200):
		data = response.content # response comes in as byte data type
		data = data.decode()	# decode to str
		writeHTML(data)		# call function to write str to HTML file ttc.html

		# load as a JSON to access specific data more easily
		data = json.loads(data) # load str to json dictionary
		print(data["city"])
		
	else:
		data = "Error has occured"
		writeHTML(data)

main()