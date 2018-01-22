import notify2
import requests
import traceback
from bs4 import BeautifulSoup
import time

sc = requests.get("https://www.enggwave.com/category/mumbai")
soup = BeautifulSoup(sc.text,'lxml')
arr = soup.select(".td_module_16")
for entry in arr:
	try:
		stri = ""
		anc = entry.find("a")
		sc = requests.get(anc["href"])
		soup = BeautifulSoup(sc.text,"lxml")
		title = soup.select("h1.entry-title")[0]
		print("Title "+title.text)
		p_tags = soup.select(".td-post-content")[0]
		for p in p_tags.find_all("p"):
			if "click here" in str(p.text).lower():
				print(p.text+" "+p.find("a")['href'])
				stri =stri + str(p.text)+" "+str(p.find("a")['href'])+"\n"
			else:
				print(p.text)
				stri = stri + p.text+"\n"
			print()
		notify2.init('foo') 
		notifier =notify2.Notification("Job Announcement" , title.text)
		notifier.show()
		
	except IndexError as e:
		continue