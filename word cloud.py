from pywordcloud import pywordcloud,stopwords

import matplotlib.pyplot as plt

import pandas as pd

df=pd.read_csv("C:/Users/Yogesh Kumar Ahuja/Desktop/ppts/Youtube04-Eminem.csv")
comment_words=''
stopwrds=set(stopwords.stopwords)
for val in df.CONTENT:
    val=str(val)
    tokens=val.split()
    for i in range(len(tokens)):
        tokens[i]=tokens[i].lower()
    for words in tokens:
        comment_words=comment_words+words+' '

wc=pywordcloud.create(comment_words)
plt.imshow(wc)
plt.show()
