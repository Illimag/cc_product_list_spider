import requests
from bs4 import BeautifulSoup as soup

r = requests.get("https://www.centralcomputer.com/")
content = soup(r.content, "html.parser")

print (content)