#!pip install requests

#!pip install beautifulsoup4

import requests
import pandas as pd

url="https://www.imdb.com/title/tt27995594/reviews/?ref_=tt_ov_rt"

page =requests.get(url)
page

page.content



from bs4 import BeautifulSoup

soup = BeautifulSoup(web.content,"html.parser") 

print(soup.prettify())

scrapped_reviews=soup.find_all('div', class_="text show-more__control")
scrapped_reviews

reviews=[]
for review in scrapped_reviews:
    review=review.get_text().replace('\n',"")
    review=review.strip(" ")
    reviews.append(review)
review

data =pd.DataFrame()
data['Reviews of movie'] = reviews
data.head()

from textblob import TextBlob

def textblob_sentiment_analysis (review): 
    sentiment = TextBlob (review).sentiment 
    if sentiment.polarity > 0.1 : 
        return 'Positive'
    elif sentiment.polarity<-0.1:
        return 'Neutral'
    else:
        return 'Negetive'

data['Sentiment']=data['Reviews of movie'].apply(textblob_sentiment_analysis)

data.sample(5)


sentiment_distribution=data['Sentiment'].value_counts()
sentiment_distribution

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize = (9,5))
sns.barplot(x = sentiment_distribution.index,
y = sentiment_distribution.values)
plt.title('Distribution of Sentiments')
plt.xlabel('Sentiment')
plt.ylabel('Count')

