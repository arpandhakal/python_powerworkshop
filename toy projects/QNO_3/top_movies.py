import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.boxofficemojo.com/')
soup = BeautifulSoup(page.content, 'html.parser')

# div = soup.findAll('div')
# for a in div:
#     if (a.text=='Worldwide 2019'):

print(soup.find_all('div', class_='hp_tab'))
start = soup.find_all('div', class_='hp_tab')
for a in start:
    if (a.text=='Worldwide 2019'):		#selected the div with Worldwide 2019, what after this?
        print(soup.a)								
