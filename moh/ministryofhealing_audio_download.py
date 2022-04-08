import requests
import json


f = open("ministryofhealing_audio.json", "r")
jsonData = json.loads(f.read())
print(jsonData)
for x in range(0, len(jsonData)):
  jsonObj = jsonData[x]
  chapter = jsonObj["chapter"]
  title = jsonObj["title"]
  url = jsonObj["url"]
  filename = chapter + ".mp3"
  doc = requests.get(url)
  with open("ministryofhealing_audio_files/"+filename, 'wb') as f:
    f.write(doc.content)