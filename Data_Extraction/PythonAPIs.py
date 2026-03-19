import requests
import pandas as pd
from bs4 import BeautifulSoup

page_number = 2
url = f"https://anisuge.se/status/finished-airing?page={page_number}"


page = requests.get(url)
html_content = page.text.encode("utf=8")
soup = BeautifulSoup(html_content)
#flex grid = 
anime_titles = soup.find('div', class_ = "original anime main-card")
print(anime_titles.prettify())

# print(soup.prettify())