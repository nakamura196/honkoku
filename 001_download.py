import requests
import json
import os

url = "https://us-central1-honkoku2.cloudfunctions.net/api/projects/ishimoto/"

project = requests.get(url).json()

collections = project["collections"]

for collection_id in collections:
    collection_url = "https://us-central1-honkoku2.cloudfunctions.net/api/collections/"+collection_id

    collection = requests.get(collection_url).json()

    entries = collection["entries"]

    for entry_id in entries:
        entry_url = "https://us-central1-honkoku2.cloudfunctions.net/api/entries/"+entry_id

        opath = "data/"+entry_id+".json"

        entry = requests.get(entry_url).json()

        fw = open(opath, 'w')
        json.dump(entry, fw, ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': '))
        fw.close()

