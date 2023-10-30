import configparser
import requests
import modules.functions as functions
import json

####################
# Lecture fichier .ini
####################
parser = configparser.ConfigParser() 
parser.read('./conf/configuration.ini')

signalk_server = parser['signalk']['server']
signalk_port = parser['signalk']['port']
output_path = parser['output']['bronzepath']

####################
# Récupération fichier JSON Signalk
####################
api_url = "http://" + signalk_server + ":" + signalk_port + "/signalk/v1/api/"

try:
    response = requests.get(api_url)
    json_data = response.json()
    functions.JSONWriteFile(json_data,output_path)
except:
    pass

