"""
Simple Program to help you get started with Google's APIs
"""
import urllib.request, json
import csv

#Google MapsDdirections API endpoint
endpoint = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
api_key = ''  # add your API keys
#Asks the user to input Where they are and where they want to go.
origin=''
destination=''
ctr=0
with open('D://addresses.csv', 'r') as csvfile:  # refer to file containing 1 row of all addresses you want to generate a distance matrix for
    spamreader = csv.reader(csvfile, delimiter=' ')
    for row in spamreader:
            ctr+=1
            if ctr<8:
                origin += (str(row)[2:-2]).replace(' ','+') + '|'
            else:
                destination += (str(row)[2:-2]).replace(' ','+') + '|'
#origin = ('1939 J. Abad Santos Ave. Tondo, 229, Manila, 1012 Metro Manila|1680 Blumentritt Streetsanta Cruz, Metro Manila, Santa Cruz, Manila, Metro Manila').replace(' ','+')
#destination = ('1939 J. Abad Santos Ave. Tondo, 229, Manila, 1012 Metro Manila|1680 Blumentritt Streetsanta Cruz, Metro Manila, Santa Cruz, Manila, Metro Manila').replace(' ','+')
#Building the URL for the request
nav_request = 'origins={}&destinations={}&mode=driving&language=fr-EN&key={}'.format(destination[:-1],destination[:-1],api_key)
request = endpoint + nav_request 
#Sends the request and reads the response.
response = urllib.request.urlopen(request).read()
#Loads response as JSON
directions = json.loads(response)
print(directions)
print(request)


