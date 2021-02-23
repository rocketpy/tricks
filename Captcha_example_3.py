from urllib import urlopen,urlretrieve
from PIL import Image,ImageOps
from bs4 import BeautifulSoup
import requests
import subprocess


def cleanImage(imagePath):
    image = Image.open(imagePath)
    image = image.point(lambda x:0 if x<143 else 255)
    borederImage = ImageOps.expand(image,border=20, fill="white")
    borederImage.save(imagePath)
    
html = urlopen("http://www...")
soup = BeautifulSoup(html,'html.parser')
imageLocation = soup.find('img',{'title':'Image CAPTCHA'})['src']
formBuildID = soup.find('input',{'name':'form_build_id'})['value']
captchaSID = soup.find('input',{'name':'captcha_sid'})['value']
captchaToken = soup.find('input',{'name':'captcha_token'})['value']
captchaURL = "http://pythonscraping.com" + imageLocation
urlretrieve(captchaURL,"captcha.jpg")
cleanImage("captcha.jpg")
p = subprocess.Popen(['tesseract','captcha.jpg',"captcha"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.wait()
f = open('captcha.txt','r')
captchaResponce = f.read().replace(" ","").replace("\n","")
print("captcha responce attempt "+ captchaResponce+"\n\n")
try:
    print(captchaResponce)
    print(len(captchaResponce))
    print(type(captchaResponce))
except:
    print("No way")
