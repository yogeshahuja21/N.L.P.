import nltk
import urllib.request
import urllib.response
import re
from nltk.corpus import stopwords

# nltk.download('stopwords')

x=urllib.request.urlopen("https://en.wikipedia.org/wiki/Box_plot")
r=x.read()
# print(r)

from bs4 import BeautifulSoup
soup=BeautifulSoup(r,'html5lib')
text=soup.get_text(strip=True)

print(soup.find_all('a'))
print(soup.find_all('img'))
links=soup.find_all('td')
for link in links:
    print(link.get("href"))
print(links[:10])
print(str(links[:10]))

list_rows=[]
# clean2=[]
for row in links:
    cells=row.find_all('td')
    str_cells=str(cells)
    clean=re.compile('<.*?>')
    # print(clean)
    clean2=(re.sub(clean,'',str_cells))
    list_rows.append(clean2)
    print(clean2)
print(list_rows)
type(list_rows)
