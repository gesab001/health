import json
import os


files = os.listdir("ministryofhealing_text")
result = []
for f in files:
  print(f)
  fopen =  open("./ministryofhealing_text/"+f, "r")
  jsonarray = json.loads(fopen.read())
  for x in range(0, len(jsonarray)):
      print(x)
      jsonObj = {"filename": f, "paragraphIndex": x, "text": jsonarray[x]}
      print(jsonObj)  
      result.append(jsonObj)

with open("ministryofhealing_allParagraphs.json", "w") as outfile:
  json.dump(result, outfile, indent=4)      