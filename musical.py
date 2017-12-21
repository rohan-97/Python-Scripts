import requests
from bs4 import BeautifulSoup
import os

search = input('Enter the name of the song: ')
sc = requests.get('https://www.youtube.com/results?search_query=' + search)
soup = BeautifulSoup(sc.text, 'lxml')
title = soup.findAll('h3', {'class': 'yt-lockup-title '})
link = []
for i in range(min(10, len(title))):
    link.append(title[i].find('a')['href'])
for i in range(min(10, len(title))):
    print(str(i + 1) + '. ' + title[i].find('a').text)

while True:
    try:
        user_input = int(input('Enter the song no. to download: '))
        if user_input not in range(1, 11):
            print('Enter correct input')
            continue
        break
    except NameError:
        print('Enter correct input')
        continue

print('Download hotay... jara vel thamba....')
os.system("youtube-dl --extract-audio --audio-format mp3 " + 'https://www.youtube.com' + link[user_input - 1])