import nltk
import urllib.request
import urllib.response
from nltk.corpus import stopwords

# nltk.download('stopwords')

x=urllib.request.urlopen("https://en.wikipedia.org/wiki/Box_plot")
r=x.read()
# print(r)

from bs4 import BeautifulSoup
soup=BeautifulSoup(r,'html5lib')
text=soup.get_text(strip=True)
# to clean the data
tokens=[t for t in text.split()]
# print(tokens)
# print(text)
sr=stopwords.words('english')
# print(sr)
ct=tokens[:]
print(ct)

for token in tokens:
    if token in stopwords.words('english'):
        ct.remove(token)
print(ct)

freq=nltk.FreqDist(ct)
for key,val in freq.items():
    print(str(key)+':'+str(val))

freq.plot(20)