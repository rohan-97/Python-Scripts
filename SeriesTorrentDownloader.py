import requests
import os
from bs4 import BeautifulSoup
from prettytable import PrettyTable

isHighQuality=True
directory = 'C:\\Users\\rohan.yadav\\Downloads\\Movies'

def download_series(url,directory):
    if(url[0:24]!='https://ytstv.com/series'):
        print('cannot download from this link, please select anothe link\nquitting...')
        return
    sc = requests.get(url)
    soup = BeautifulSoup(sc.text,'lxml')
    seasons = soup.select('.tvseason')
    index = 1
    series_name = soup.select('#mv-info > div.mvi-content > div.mvic-desc > h3')[0].text
    series_root_directory = directory+'\\'+series_name
    safeMkdir(series_root_directory)
    qual = input("enter y for high quality torrents else enter n\n")
    if qual =="n":
        global isHighQuality
        isHighQuality = False
    options = {}
    for each_season in seasons:
        title = each_season.find('div',{'class' : 'les-title'})
        print("Enter "+str(index)+" for : "+trim(title.text))
        options[index] = (trim(title.text),each_season.select('.les-content > a'))
        print('------------------------------------')
        index+=1
    option = int(input())
    try:
        downloadSeason(options[option],series_root_directory)
    except KeyError as e:
        print('Bro select a valid option')

def downloadSeason(season_data,root_directory):
    season_directory = root_directory +'\\'+ season_data[0]
    safeMkdir(season_directory)
    episodes = season_data[1]
    for episode in episodes:
        name = trim(episode.text)
        downloadEpisode(name,episode['href'],season_directory)

def downloadEpisode(episode_name,episode_url,directory):
    try:
        sc = requests.get(episode_url)
        soup = BeautifulSoup(sc.text,'lxml')
        table = soup.find(id = 'lnk list-downloads')
        links = table.select('.lnk-lnk')
        torrent_url = links[-1]['href']
        print('downloading '+ episode_name)
        resp = requests.get(torrent_url)
        with open(directory+'\\'+episode_name+'.torrent','wb') as f:
            f.write(resp.content)
            f.close()
    except Exception as e:
        print('failed to download '+ episode_name +' you can download the torrent at '+ episode_url)


def search_series():
    pass

def show_list():
    sc = requests.get('https://ytstv.com/series/')
    soup = BeautifulSoup(sc.text,'lxml')
    pages = int(len(soup.select('#pagination > nav > ul > li'))/2)
    list = []
    list.extend(get_list(soup))
    for i in range(2,pages+1):
        sc =requests.get('https://ytstv.com/series/page/'+str(i)+'/')
        soup = BeautifulSoup(sc.text,'lxml')
        list.extend(get_list(soup))
    table = PrettyTable(['index','Name', 'Ratings'])
    index = 1
    selected_option = {}
    for movies in list:
        table.add_row([index,movies[0],movies[1]])
        selected_option[index] = movies[2]
        index+=1
    print(table)
    global directory
    option = int(input('Enter the index no. of the movie\n'))
    try:
        download_series(selected_option[option],directory)
    except KeyError as e:
        print('Bro select a valid option...')

def get_list(soup):
    list = soup.select('#main > div > div.main-content.main-category > div > div.movies-list.movies-list-full > div')
    arr = []
    for least in list:
        try:
            demo = []
            demo.append(least.select('.qtip-title')[0].text)
            demo.append(least.select('.jt-imdb')[0].text)
            demo.append(least.select('.ml-mask')[0]['href'])
            arr.append(demo)
        except Exception as e:
            i
    return arr

def trim(unstripped_string):
    return unstripped_string.replace('\n','').strip()

def safeMkdir(path):
    if not os.path.exists(path):
        os.makedirs(path)

def main():
    # resp = int(input('enter 1 for displaying list of available tv series\nenter 2 for searching specific series\n'))
    # if(resp == 2):
    #     search_series()
    # else:
    #     show_list()
    show_list()

if __name__ == '__main__':
    main()
