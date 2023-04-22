import requests
import xbmcgui
import xbmcplugin
from bs4 import BeautifulSoup

site_url = "https://streamblasters.pro/movies"

def list_movies():
    response = requests.get(site_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    movies = soup.find_all('div', class_='movie')

    for movie in movies:
        title = movie.find('h2').text
        url = movie.find('a')['href']
        print(title, url)