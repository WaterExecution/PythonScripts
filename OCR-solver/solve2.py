#due to tesseract unstability use this script multiple time to get it to work every 1/30 may fail to recognise image

import requests
import re
import hashlib
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import requests

def ocr_core(filename):

    magic = pytesseract.image_to_string(Image.open(filename))
    return magic

def md5Checksum(filePath):
    with open(filePath, 'rb') as fh:
        m = hashlib.md5()
        while True:
            data = fh.read()
            if not data:
                break
            m.update(data)
        return m.hexdigest()

url = ""                                    # add url
post = ""                                   # add url + ?answer=
plus = "e8f0a7b183094b14fe2ac4ed70bf110b"
minus = "5476d4bbb706d34838cd361e16e78f76"
divide = "5ae1d65e868e21e3e13038cd304b3d1d"
asterisk = "c9b90bd0385b6174eff6b4ffd5ad71fb"

r = requests.Session()
r1 = r.get(url)
test = r1.text

for i in range(100):
 if i > 40:
  print(test)  #get flag after 40 attempts
  
 scrapped = []
 
 scrap = re.findall(r'img.+', test)                                                 #change here
 for i in scrap:                                                                    #
  scrap1 = re.findall(r'\.\/.+"', i)                                                #
  scrapped.append(scrap1)                                                           #

 link1 = str(scrapped[0])[4:-3]                                                     #
 link2 = str(scrapped[1])[4:-3]                                                     #
 link3 = str(scrapped[2])[4:-3]                                                     #
 #gets all 3 link to images

 pic1 = r.get(url+link1)
 open('pic1.png', 'wb').write(pic1.content)
 text1 = ocr_core("pic1.png")
 print(text1)

 pic2 = r.get(url+link2)                    #tesseract didnt recognise image so i used hash to compare instead, + more accurate
 open('pic2.png', 'wb').write(pic2.content)
 hash = md5Checksum("pic2.png")
 if hash == plus:
  text2 = "+"
 elif hash == divide:
  text2 = "/"
 elif hash == asterisk:
  text2 = "*"
 else:
  text2 = "-"
 print(hash)
 print(text2) 

 pic3 = r.get(url+link3)
 open('pic3.png', 'wb').write(pic3.content)
 text3 = ocr_core("pic3.png")
 print(text3)

 answer = str(eval(str(int(text1))+text2+str(int(text3))))
 print(answer)
 stage = re.findall(r"stage.+", test)
 print(stage)

 x = r.post(posturl+answer)
 test = x.text

