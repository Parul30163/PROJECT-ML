# install all the requirnment
#pip install requests
# pip install bs4
# pip install html5lib

import  requests
from bs4 import BeautifulSoup
url="https://www.imdb.com/title/tt27995594/"

# get the html
r = requests.get(url)
htmlContent= r.content

#parse the html
soup=BeautifulSoup(htmlContent ,'html.parser')
res =soup.title
print(soup.prettify())
#html tree traversal

print(soup.get_text())

