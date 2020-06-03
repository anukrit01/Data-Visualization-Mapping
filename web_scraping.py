import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.edureka.co/")
c = r.content

soup = BeautifulSoup(c, "html.parser")
#print(soup.prettify())      #it makes html code look pritty

'''
#Extracting all the links present in the webpage
links = []      #Empty array to store all the links
for web_links in soup.find_all('a'):
    links.append(web_links.get('href'))

print(links)
'''

#Comparison of prices in a E-commerce website
for price in soup.find_all('span', class_='after_discount'):
    print(price)