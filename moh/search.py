import json
import os

files = os.listdir("./ministryofhealing")

def search(chapter):
 filename = files[chapter-1]
 print("Filename: " + filename)

 f = open("./ministryofhealing/"+filename, "r")
 jsonData = json.loads(f.read())
 keyword = input("search: ")
 result = 0
 for x in range(0, len(jsonData)):
  if keyword in jsonData[x]:
    print("Found Index: " + str(x))
    print("Found Matching Paragraph: " + str(jsonData[x]))
    result = x
 return result
  
ministryofhealing = open("ministryofhealing3.json", "r")
jsonData = json.loads(ministryofhealing.read())
ministryofhealing.close()

ministryofhealing2 = open("ministryofhealing3.json", "r")
jsonData2 = json.loads(ministryofhealing2.read())
ministryofhealing2.close()

for x in range(0, len(jsonData["tableofContents"])):
  chapters = jsonData["tableofContents"][x]["chapters"]
  for c in range(0, len(chapters)):
    item = chapters[c]
    chapterNumber = int(item["chapterNumber"])
    subsections = jsonData["tableofContents"][x]["chapters"][c]["subsections"]
    for s in range(0, len(subsections)):
      subItem = subsections[s]
      key = list(subItem.keys())[0]

      if(subItem[key]==0):
       print("Chapter: " + str(chapterNumber))
       print("Subsection: " + key)
       index = search(chapterNumber)
       jsonData2["tableofContents"][x]["chapters"][c]["subsections"][s][key] = index
       with open("ministryofhealing3.json", "w") as outfile:
          json.dump(jsonData2, outfile, indent=4)