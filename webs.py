import requests
from bs4 import BeautifulSoup
import csv

url="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
page=requests.get(url)

soup=BeautifulSoup(page.content,"html.parser")

'''img1=[]
image=soup.findAll('div',class_="imageWrapper")
for i in image:
    j=i.img['src']
    img1.append(j)
   print(img1)

link=soup.findAll('div',class_="col-sm-4 col-lg-4 col-md-4")
'''

names=soup.find_all("a",class_="title")

for i in names:
    print(i.text)

price=soup.find_all("h4",class_="pull-right price")
# print(price)