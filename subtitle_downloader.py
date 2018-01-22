import requests
from bs4 import BeautifulSoup
import sys
#!/usr/bin/python
import urllib.request
from zipfile import ZipFile
import zipfile
import io

for index in range(1,len(sys.argv)):
	argument = sys.argv[index]
	arga = argument.split("~")
	com = ""
	arg = ""
	if len(arga) == 2:
		com = arga[1]
	arg = arga[0]
	sc = 	requests.get("https://subscene.com/subtitles/release?q=" + arg)
	soup = BeautifulSoup(sc.text , 'lxml')
	rows = soup.find_all("tr")
	for row in rows:
		if "English" in str(row.find("span").text).replace(" ",""):
			url = "https://subscene.com" + row.find("a")['href']
			sc = requests.get(url)
			soup = BeautifulSoup(sc.text , 'lxml')
			release = soup.select(".release")[0].find_all("div")
			fallback = True
			for divs in release:
				if com in divs.text:
					fallback = False
					break
			if fallback:
				continue
			dwnld = soup.select("#downloadButton")[0]
			url = "https://subscene.com" + dwnld['href']
			name = str(soup.select(".release")[0].find_all("div")[0].text).replace(" ","").rstrip() + ".srt"
			r = requests.get(url)
			z = zipfile.ZipFile(io.BytesIO(r.content))
			z.extractall()
			break