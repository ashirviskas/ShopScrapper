import requests
from bs4 import BeautifulSoup


class Shop:
    def extract_product_info(self,url):
        header =  {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        r = requests.get(url, headers=header);
        soup = BeautifulSoup(r.content, 'html.parser')
        soup =soup.find_all("table", class_="specification")
        soup= soup[0].find_all('tr')
        results={}
        for a in soup:
            results[a.next_element.text] = a.next_element.next_sibling.text
        print(results)










