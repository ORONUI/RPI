import json
import os
import time

def JSONWriteFile(json_data,output_path,filename=""):
    # Création folder output s'il n'existe pas
    if not os.path.exists(output_path): 
        os.makedirs(output_path) 
    
    # Nom de fichier
    if filename == "":
        output_filename = 'data-' + time.strftime("%Y%m%d-%H%M%S") + '.json'
    else:
        output_filename = filename

    #ecriture
    with open(output_path + '/' + output_filename, 'w') as f:
        json.dump(json_data, f)
