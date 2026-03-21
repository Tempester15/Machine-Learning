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

    """
    URL for scraping Anisuge site anime data 
    page_number = 2
    url = f"https://anisuge.se/status/finished-airing?page={page_number}"
    """
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

  def scrape_countries_data(self):

    """ url for scraping countries  
    url = "https://www.scrapethissite.com/pages/simple/"
    """ 
    countries_data = {}

    #Scraping countries name
    countries_heading_element = self.soup.find_all('h3', class_ = "country-name")
    countries_names = [countries_name.text.strip() for countries_name in countries_heading_element]
    countries_data.update({"Name": countries_names})

    #Scraping countries capitals
    countries_capitals_element = self.soup.find_all('span', class_ = "country-capital") 
    countries_capitals = [countries_capital.text.strip() for countries_capital in countries_capitals_element]
    countries_data.update({"Capital" : countries_capitals})

    #Scraping countries population
    countries_population_element = self.soup.find_all('span', class_ = "country-population") 
    countries_populations = [int(countries_population.text.strip()) for countries_population in countries_population_element]
    countries_data.update({"Population" : countries_populations})
    countries_populations

    #Scraping countries Area
    countries_area_element = self.soup.find_all('span', class_ = "country-area")
    countries_areas = [float(countries_area.text.strip()) for countries_area in countries_area_element]
    countries_data.update({"Area (sq. Km)" : countries_areas})

    return pd.DataFrame(countries_data)
