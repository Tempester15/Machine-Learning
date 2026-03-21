import pandas as pd
import requests
from bs4 import BeautifulSoup
import os

class quote_scrape:
    def __init__(self):
        self.folder_path = "Scraped Content"
        self.files = []
        self.results = []

    #Run this function at 1st position to download html pages for quotes data 
    #Function to save the HTML files from the URL
    def fetch_quote_pages(self):

        page_number = 1

        while True:
            url = f"https://quotes.toscrape.com/page/{page_number}"
            response = requests.get(url)
            # response = response.text.encode("utf=8")
            soup = BeautifulSoup(response.text, "lxml")
            quote_elements = soup.select("div.quote") 
            
            if not quote_elements:
                print("No more quotes present")
                break
            
            with open(f"Scraped Content/quote_content_{page_number}.html", "w" , encoding="utf-8") as f:
                f.write(response.text)
                print(f"Scraped page {page_number} contents !!")

            page_number += 1
    
    #Function to extract the contents of the quotes with life tag
    def extract_life_quotes(self, file_path):

        with open(file_path, "r", encoding="utf-8") as f:
            html_content = f.read()

        html_content = BeautifulSoup(html_content, 'lxml')

        quotes = html_content.select("div.quote")

        life_quote = []
        count = 0

        for quote in quotes:
            all_quote_tags = []

            for element in quote.select(".tags .tag"):
                all_quote_tags.append(element.get_text())


            if 'life' in all_quote_tags:
                author = quote.select_one("small.author").get_text(strip = True)
                # print(author)
                content = quote.select_one(".text").get_text()
                # print(content)
                count += 1
                life_quote.append({"Quote" : content, "Author" : author})

        print(f"No. of life tagged Quotes : {count}")
        return life_quote
    
    #Optional - Run this function at 2end postion to fetch the file path to all html files
    #Function to create the file paths of the downloaded HTML files
    def fetch_file_path(self):
        file_count = 0

        for file_path in os.listdir(self.folder_path):
            if(file_path.endswith(".html")):
                full_path = self.folder_path + "/" + file_path
                self.files.append(full_path)
                file_count += 1

        print(f"Total file fetched : {file_count}")

        self.view_files()

    #Function to view file paths
    def view_files(self):
        for file in self.files:
            print(file)


    #Optional - Run this function at the 3rd position to extract all the quotes with life tags
    #Function to extract quotes from all the saved HTML pages 
    def get_all_life_quotes(self):
        self.fetch_file_path()
        for file_path in self.files:
            if(file_path.endswith(".html")):
                print(file_path)
                result = self.extract_life_quotes(file_path)
                self.results.extend(result)

    #Finally Run this function at 4th position to get the dataframe of the extracted data
    #Function to get the dataframe of the extracted life quotes 
    def get_life_quotes_dataframe(self):
        self.get_all_life_quotes()
        return pd.DataFrame(self.results)



scraper = quote_scrape()
scraper.fetch_quote_pages()
print(scraper.get_life_quotes_dataframe())