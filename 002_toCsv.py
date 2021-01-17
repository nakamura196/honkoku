import requests
import json
import os
import glob

files = glob.glob("data/*.json")

rows = []
rows.append(["uuid", "url", "title", "page", "status", "text", "canvas"])

for file in files:

    json_open = open(file, 'r')
    entry = json.load(json_open)

    transcriptions = entry["transcriptions"]

    label = entry["label"]

    url = "https://honkoku.org/app/#/transcription/"+entry["id"]+"/1/"

    for i in range(len(transcriptions)):
        transcription = transcriptions[i]

        text = transcription["text"]
        status = transcription["status"]

        canvas = transcription["canvasUrl"]

        uuid = canvas.split("/iiif/")[1].split("/canvas/")[0]

        row = [uuid, url, label, i+1, status, text, canvas]

        rows.append(row)

import csv

with open('data.csv', 'w') as f:
    writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
    writer.writerows(rows)

