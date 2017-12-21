import urllib.request
import requests
from bs4 import BeautifulSoup

# Get BingXML file which contains the URL of the Bing Photo of the day
# idx = Number days previous the present day. 0 means current day, 1 means       yesterday, etc
# n = Number of images previous the day given by idx
# mkt denotes your location. e.g. en-US means United States. Put in your  country code

BingXML_URL = "http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=en-US"
page = requests.get(BingXML_URL)
BingXML = BeautifulSoup(page.text, "lxml")
Images = BingXML.find_all('image')
for pics in Images:
    ImageURL = "https://www.bing.com" + pics.url.text[:-12] + "1920x1080.jpg"
    ImageName = "/home/rohan/Downloads/Bing_Photo_Of_the_day/" + pics.startdate.text + ".jpg"
    urllib.request.urlretrieve(ImageURL, ImageName)
