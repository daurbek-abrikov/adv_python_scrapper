from bs4 import BeautifulSoup
import requests


class Web_Scrapper():       #Creating class
    URL = 'https://coinmarketcap.com/currencies/'    #defining URL Attribute
    def set_coin(self):      #method to set cryptocurrency
        print("Please type the name of cryptocurrency, of which you need information:")
        self.crypto = input()

    def get_p(self):         #method to get all resulting paragraphs
        page = requests.get(self.URL + self.crypto)
        soup = BeautifulSoup(page.text, 'html.parser')
        paragraphs = soup.find_all('p') 
        return paragraphs

    def print_p(self):       #method to print those results(just for convenience)
        for item in self.get_p():
            print(item.get_text())  
            print()
        print("-"*64)      
