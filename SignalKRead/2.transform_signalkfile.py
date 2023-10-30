import json
import os
import time
import configparser
import modules.functions as functions
import shutil
import datetime

####################
# Lecture fichier .ini
####################
parser = configparser.ConfigParser() 
parser.read('./conf/configuration.ini')

trash_path = parser['output']['trashpath']
bronze_path = parser['output']['bronzepath']
silver_path = parser['output']['silverpath']

if not os.path.exists(trash_path + '/' + bronze_path): 
  os.makedirs(trash_path + '/' + bronze_path) 

####################
# Lecture configuration noeud SignalK
####################
with open('./conf/configuration_signalk_key.json') as user_file:
  file_contents = user_file.read()
dict_signalk = json.loads(file_contents)

####################
# boucle sur les fichiers
####################

contenu = os.listdir(bronze_path)
fichiers_json = [fichier for fichier in contenu if fichier.endswith(".json")]
for filename in fichiers_json:
  print ("Traitement du fichier : " + filename)

  with open('./' + bronze_path + '/' + filename) as user_file:
    file_contents = user_file.read()
  parsed_json = json.loads(file_contents)

  # Recupération des données présentes dans le JSON
  firstNode = list(parsed_json["vessels"].keys())[0]
  data_json = parsed_json["vessels"][firstNode]

  # Parcours liste de clé & création contenu JSON de sortie
  output_data_json = {}

  # Heure de génération du fichier source
  hms = datetime.datetime.fromtimestamp(os.path.getctime(bronze_path + '/' + filename))
  output_data_json['DataTimestamp'] = hms.strftime("%Y-%m-%dT%H:%M:%S.%f")
  output_data_json['GenerationTimestamp'] = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")
  for key in dict_signalk:
      strg = "try:output_data_json['" + key + "'] = data_json" + dict_signalk[key] + "\nexcept:output_data_json['" + key + "'] =''"
      exec(strg)
  
  #Ecriture du JSON
  functions.JSONWriteFile(output_data_json,silver_path)

  # deplacement fichier source
  shutil.move(bronze_path + '/' + filename, trash_path + '/' + bronze_path + '/' + filename)

  time.sleep(2)

####################
# FIN BOUCLE FICHIER
####################