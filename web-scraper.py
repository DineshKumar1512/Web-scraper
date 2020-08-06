import requests
from bs4 import BeautifulSoup

URL="https://webscraper.io/test-sites/e-commerce/allinone/computers"

page = requests.get(URL)

soup = BeautifulSoup(page.text, "html.parser")

items = soup.find_all('div', attrs={'class':'caption'})
for x in items:
    name=x.find('a',attrs={'class':'title'})
    description=x.find('p',attrs={'class':'description'})
    price=x.find('h4',attrs={'class':'price'})
    print(name.text.strip())
    print(description.text.strip())
    print(price.text.strip())
    

    print()
    
                              

