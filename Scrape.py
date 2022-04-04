import requests
from bs4 import BeautifulSoup
import datetime

class Scrape():

    def __init__(self, symbol, elements):
        
        url = "https://www.westmetall.com/en/markdaten.php"

        r = requests.get(url)
        if(r.url != url): # redirect occurred; likely symbol doesn't exist or cannot be found.
            raise requests.TooManyRedirects()

        r.raise_for_status()
        
        self.soup = BeautifulSoup(r.text, "html.parser")

        self.__summary = {}
        
        self.price_table = self.soup.find('table', class_ = 'marginalia extended-head')
        self.current_date = datetime.datetime.now()
        
        for prices in self.price_table.find_all('tbody'):
            rows = prices.find_all('tr')
            for row in rows:
                
                element = row.find_all('td')[0].text.strip()
                price = row.find_all('td')[1].text.strip()

                self.__summary[element] = price
                print(element + ' ' + price)

    def summary(self):
        return self.__summary