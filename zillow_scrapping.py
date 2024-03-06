import requests
from bs4 import BeautifulSoup

class ZillowScrapping:

    def __init__(self, URL):
        self.URL = URL

    @staticmethod
    def modified_prices(s):

        index_plus = s.find('+')
        index_slash = s.find('/')
        index = min(index_plus if index_plus != -1 else len(s), index_slash if index_slash != -1 else len(s))

        return s[:index]

    @staticmethod
    def clean_address(address):

        cleaned_address = ' '.join(part.strip() for part in address.split('|'))

        return cleaned_address


    def rent_details_scrapping(self):

        response = requests.get(self.URL)
        zillow_web_page = response.text

        soup = BeautifulSoup(zillow_web_page, "html.parser")

        lists = soup.find_all(class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

        prices = []
        addresses = []
        listing_links = []

        for i in range(len(lists)):
            prices.append(lists[i].find(class_="PropertyCardWrapper__StyledPriceLine").text.strip())
            addresses.append(lists[i].find(class_="StyledPropertyCardDataArea-anchor").text.strip())
            listing_links.append(lists[i].find(name="a").get("href").strip())

        return prices, addresses, listing_links



