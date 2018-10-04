from bs4 import BeautifulSoup
import requests

def message():
	sc = requests.get("http://site21.way2sms.com/content/index.html")
	soup = BeautifulSoup(sc.text,'lxml')
	print(soup)
	nam = soup.select("#username")[0]
	print(nam)



if __name__ == '__main__':
	message()