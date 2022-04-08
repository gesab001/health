import os
import json

files = os.listdir("./subsections")

ministryofhealing = open("ministryofhealing.json", "r")
jsonData = json.loads(ministryofhealing.read())
ministryofhealing.close()

ministryofhealing2 = open("ministryofhealing.json", "r")
jsonData2 = json.loads(ministryofhealing2.read())
ministryofhealing2.close()

for x in range(0, len(jsonData["tableofContents"])):
  print(x+1)
  chapters = jsonData["tableofContents"][x]["chapters"]
  print(chapters)
  for c in range(0, len(chapters)):
    item = chapters[c]
    chapterNumber = int(item["chapterNumber"])-1
    fileName = files[chapterNumber]
    print(fileName)
    fopen = open("./subsections/"+fileName, "r")
    jsonObj = json.loads(fopen.read())
    jsonData2["tableofContents"][x]["chapters"][c]["subsections"] = jsonObj
    print(jsonData2["tableofContents"][x]["chapters"][c]["subsections"])  

with open("ministryofhealing2.json", "w") as outfile:
  json.dump(jsonData2, outfile, indent=4)
""" 
for x in range(0,len(files)):
  fileName = files[x]
  fopen = open("./subsections/"+fileName, "r")
  jsonObj = json.loads(fopen.read())
  print(jsonObj)  
  """