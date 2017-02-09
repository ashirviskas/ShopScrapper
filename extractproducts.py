import requests
from bs4 import BeautifulSoup

class Item:
    def __init__(self,model,name,amount,price):
        self.model= model
        self.name = name
        self.amount = amount
        self.price = price




class Shopv:
    def __init__(self,url):
        self.items=[]
        self.url=url
        self.currentpage=1
        self.soup = self.get_soup()
        self.total_pages=self.get_pages()


    def get_soup(self):
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        payload = {'page': str(self.currentpage)}
        r = requests.get(self.url, headers=header,params=payload);
        return BeautifulSoup(r.content, 'html.parser')
    def get_pages(self):
        nav = self.soup.find_all("td", class_="pagenav")
        return int((len(nav[0].contents) - 1) / 2)

    def extract_products(self):
        items =self.soup.find_all("tr",  {"class":["productListing"]})

        for a in items:
            if "group" in a["class"]:
                continue
            t= Item(a.contents[1].text,a.contents[5].text,'http://www.skytech.lt/'+a.contents[5].next['href'],a.contents[9].text)
            self.items.append(t)

    def extract_all_products(self):
        for self.currentpage in range(1,self.total_pages+1):
            self.soup = self.get_soup()
            self.extract_products();
        return self.items






