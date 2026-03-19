import requests
import pandas as pd
from bs4 import BeautifulSoup

class scrape:
  def __init__(self, url):
    self.url = url
    self.page = requests.get(self.url)
    self.html_content = self.page.text.encode("utf=8")
    self.soup = BeautifulSoup(self.html_content)


  def Scraping_aniSuge_anime_data(self):
    
    anime_data = {}
    #Scraping all anime containers on page
    anime_containers = self.soup.find('div', class_ = "original anime main-card")

    #Scraping anime names from anime containers
    anime_names = anime_containers.find_all('div', class_ = "name")
    anime_names_list = [anime_name.text.strip() for anime_name in anime_names]
    anime_data.update({"Name" : anime_names_list })

    #Scraping anime types from anime containers on page
    anime_types = anime_containers.find_all("span", class_ = "type")
    anime_types_list = [anime_type.text.strip() for anime_type in anime_types]
    anime_data.update({"Type": anime_types_list})

    return pd.DataFrame(anime_data)
