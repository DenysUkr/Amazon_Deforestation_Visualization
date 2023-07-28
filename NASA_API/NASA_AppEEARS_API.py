import json
import requests
import geojson
import os
from multiprocessing import Pool

#LOGIN TO AppEEARS HERE
response = requests.post('https://appeears.earthdatacloud.nasa.gov/api/login', auth=('USERNAME', 'PASSWORD')) 
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
token_response = response.json()
token = token_response['token']

#ENTER TASK ID HERE
task_id = '57b0adce-8009-4d99-8e25-fc9fbe8376ce'
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

response = requests.get(
    'https://appeears.earthdatacloud.nasa.gov/api/bundle/{0}'.format(task_id),  
    headers={'Authorization': 'Bearer {0}'.format(token)}
)
bundle_response = response.json()

#ENTER DESTINATION DIRECTORY HERE
dest_dir = 'C:/Users/Connor/Desktop/Data/AppEARS_LST/'
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


    
def download(file):
        
    file_id = file["file_id"]
    filename = file["file_name"]
    response = requests.get( 
        'https://appeears.earthdatacloud.nasa.gov/api/bundle/{0}/{1}'.format(task_id,file_id),  
        headers={'Authorization': 'Bearer {0}'.format(token)},
