import requests
from lxml import html
import lxml
import json
import re

def getVerse(reference, version):
	url = 'https://www.biblegateway.com/passage/?search='+reference+'&version='+version
	page = requests.get(url)
	tree = html.fromstring(page.content)
	#classname = tree.xpath('/html/body/div[2]/div/section/div[3]/div/div[2]/section/div[1]/div[1]/div[2]/div[2]/div[2]/div/div[1]/p/span[last()]/@class')[0]
	#word = tree.xpath('/html/body/div[2]/div/section/div[3]/div/div[2]/section/div[1]/div[1]/div[2]/div[2]/div[2]/div/div[1]/p/span[@class="'+classname+'"]/text()')
	
	word = tree.xpath('/html/head/meta[14][@property="og:description"]/@content')
	print("version: " + version)    
	print(word)
	if len(word)>0:
	   return word[0].strip()
	else:
	   return "verse doesn't exist in this bible version"   

"""
reference = "Ecclesiastes 1:100"
version = "JLB"

word = getVerse(reference, version)
print(word)
"""

def saveToJson(filename, word):
  with open(filename, "w") as outfile:
     json.dump(word, outfile, indent=4)
  
def getChapter(jsonFilename, url):
	page = requests.get(url)
	tree = html.fromstring(page.content)
	#classname = tree.xpath('/html/body/div[2]/div/section/div[3]/div/div[2]/section/div[1]/div[1]/div[2]/div[2]/div[2]/div/div[1]/p/span[last()]/@class')[0]
	#word = tree.xpath('/html/body/div[2]/div/section/div[3]/div/div[2]/section/div[1]/div[1]/div[2]/div[2]/div[2]/div/div[1]/p/span[@class="'+classname+'"]/text()')

	word = tree.xpath("//p[contains(@class, 'Centered')]/b/text()")  
	print(word)
    
	result = []
	exclude = ["Find out more today how to purchase a", "or", "copy of", ".", "...", "Illustration \u00a9", "AdventWeb", "Illustration —"]    
	for item in word:
	  print(len(item.strip()))
	  if len(item.strip())>0:
	   if item.strip() not in exclude:
	     text = item.rstrip()        
	     text2 = re.sub(r'\r\n', ' ', text)
	     text2 = text2.strip()
	     jsonObj = {text2: 0}
         
	     result.append(jsonObj)
	     print(text2)
         
	saveToJson(jsonFilename, result)


f = open("ministryofhealing.json", "r")
jsonData = json.loads(f.read())
for x in range(0, len(jsonData["tableofContents"])):
  sectionTitle = jsonData["tableofContents"][x]
  print(sectionTitle)
  chapters = jsonData["tableofContents"][x]["chapters"]
  for c in range(0, len(chapters)):
    url = chapters[c]["url"]
    print(url)
    jsonFilename = url.split("/")[4].split(".")[0] + "_subsections.json"
    print(jsonFilename)
    getChapter(jsonFilename, url)
