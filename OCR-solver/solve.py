import requests
import re

url = "" #CTF Site
posturl = "" #site with post information ?answer=

r = requests.Session()
r1 = r.get(url)
test = r1.text


for i in range(100):
 if i > 99:
  print(test)                         #print flag once hit level 100


    #find both numbers
 scrapped = ""
 scrap = re.findall(r'quiz.+', test)  #change here
 for i in scrap:
  scrap1 = re.findall(r'>\d+<', i)  #change here
  if len(scrap1) != 0:
   scrapped += str(scrap1)

 scrappedfinal = re.findall(r"\d+", scrapped)    #change here


    # find operator 
 for i in scrap:
  if "operator" in i:
   operator1 = re.findall(">.<", i)    #change here
   operator1 = str(operator1)
   operator = (operator1[4])

 answer = str(eval(scrappedfinal[0]+operator+scrappedfinal[1]))  # eval(1111 + 2222)

 stage = re.findall(r"stage.+", test)  #change here
 print(stage)                          #check progress

 x = r.post(posturl+answer)
 test = x.text

