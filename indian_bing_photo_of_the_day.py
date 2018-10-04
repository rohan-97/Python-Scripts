#!/usr/bin/python3.5
import urllib.request
import requests
from bs4 import BeautifulSoup
import os
import os.path
import datetime
now = datetime.datetime.now()
nm = "/home/rohan/Downloads/Bing_Photo_Of_the_day_indian/" + str(now).replace("-","")[:8]+".jpg"
# print(nm)

if os.path.exists(nm):
	print("gsettings set org.gnome.desktop.background picture-uri file:" + nm)
	os.system("gsettings set org.gnome.desktop.background picture-uri file:" + nm)
	exit(0)
	
# Get BingXML file which contains the URL of the Bing Photo of the day
# idx = Number days previous the present day. 0 means current day, 1 means       yesterday, etc
# n = Number of images previous the day given by idx
# mkt denotes your location. e.g. en-US means United States. Put in your  country code
BingXML_URL = "http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=en-IN"
# print(BingXML_URL)
page = requests.get(BingXML_URL)
BingXML = BeautifulSoup(page.text, "lxml")
Images = BingXML.find_all('image')
ImageName = ""
for pics in reversed(Images):
    ImageURL = "https://www.bing.com" + pics.url.text[:-12] + "1920x1080.jpg"
    ImageName = "/home/rohan/Downloads/Bing_Photo_Of_the_day_indian/" +pics.startdate.text + ".jpg"
    urllib.request.urlretrieve(ImageURL, ImageName)
change_background = 'gsettings set org.gnome.desktop.background picture-uri file:' + ImageName
# print(change_background)
# os.system("sudo chmod 777 " + ImageName)
os.system(change_background)
