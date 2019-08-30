import requests # import requests module
response = requests.get("https://geo-info.co/43.65,-79.40") # send API request for Toronto

# convert response from binary to a JSON so it can be used in Python program
# pretty view (swiched single quotes to double, True surrounded with quotes so it would work
# https://raw.githubusercontent.com/mdjhoel/Y10_19/master/toronto.json
datajson = response.json() 

# grab all nearby city data in the JSON and place in a Python list (collection data type)
# lists have elements, indexes (start at 0) and bounds/range
nearbyList = datajson['nearbyCities']
numnearby = len(nearbyList) # determine number of elements in list
print("This is the number of nearby cities in the list")
print("-------------------------------------")
print(numnearby)
print("Here are all nearby cities")
print("---------------------")
print(nearbyList) # print entire list
print("Here is the first nearby city")
print("-----------------------")
print(nearbyList[0]) # print first element using index number, remember starts at 0
print("Here is the state of the first nearby city")
print("--------------------------------")
print(nearbyList[0]['state'])
print("You can loop through all elements in a list, and access parts of each as well")
print("--------------------------------------------------------------")
for nb in nearbyList:
    print(nb['city']) # notice the indent, denoting that this line of code is nested/belongs to the loop block
print("This is what happens when you give an index outside the bounds of the list")
print("---------------------------------------------------------------")
print(nearbyList[5])

