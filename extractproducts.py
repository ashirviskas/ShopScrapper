import requests
from bs4 import BeautifulSoup

class Item:
    def __init__(self,model,name,url,contents,price):
        self.model= model
        self.name = name
        self.url = url
        self.price = price
        self.contents=contents
        self.attributes={}




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

    def get_product_soup(self,url):
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        r = requests.get(url, headers=header);
        return BeautifulSoup(r.content, 'html.parser')

    def get_pages(self):
        nav = self.soup.find_all("td", class_="pagenav")
        return int((len(nav[0].contents) - 1) / 2)

    def extract_products(self):
        items =self.soup.find_all("tr",  {"class":["productListing"]})

        for a in items:
            if "group" in a["class"]:
                continue
            t= Item(a.contents[1].text,a.contents[5].text,'http://www.skytech.lt/'+a.contents[5].next['href'],a.contents[7].text,a.contents[9].text)
            self.items.append(t)

    def extract_product_info(self, url):
        soup = self.get_product_soup(url)
        soup = soup.find_all("table", class_="specification")
        print(url)
        results = {}
        try:
            soup = soup[0].find_all('tr')
        except IndexError:
            return results
        if soup ==[]:
            return results
        for a in soup:
            results[a.next_element.text] = a.next_element.next_sibling.text
        return results

    def extract_all_products(self):
        for self.currentpage in range(1,self.total_pages+1):
            self.soup = self.get_soup()
            self.extract_products();
        self.get_all_product_attributes()
        return self.items;

    def get_all_product_attributes(self):
        for item in self.items:
            item.attributes=self.extract_product_info(item.url)







