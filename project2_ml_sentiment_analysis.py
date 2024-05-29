# App Review Sentiment Snalysis
#app review sentiments analysis mean evaulating and understanding the sentiment expressed in user reviews of mobile application

import numpy  as np
import pandas as pd

df=pd.read_csv("C:\\Users\\PARUL\\Downloads\\linkedin-reviews.csv")

df.head(10)

import matplotlib.pyplot  as plt
import seaborn as sns

df.info()

# EDA

# plotting the distribution of ratings

sns.set(style='whitegrid')
plt.figure(figsize=(9,5))
sns.countplot(data=df,x='Rating')
plt.title('Distribution of Rating')
plt.xlabel('Rating')
plt.ylabel('Count')
plt.show()

# Adding Sentiment Label in the data
#We will use Textblob library. Textblob provides a polarity scores raning from-1(very negative) to 1(very positive) for a given text. We can use this score to classify each review's sentiment as positive, negative or neutral

#pip install textblob

from textblob import TextBlob

def textblob_sentiment_analysis(review):
    sentiment=TextBlob(review).sentiment
    if sentiment.polarity>0.1:
        return 'Positive'
    elif sentiment.polarity< -0.1:
        return 'Negative'
    else:
        return 'Neutral'

df['Sentiment']=df['Review'].apply(textblob_sentiment_analysis)

df.sample(5)

# Analyzing App review sentiments

sentiment_distribution=df['Sentiment'].value_counts()
sentiment_distribution

plt.figure(figsize=(9,5))
sns.barplot(x= sentiment_distribution.index,
           y=sentiment_distribution.values)
plt.title('Distribution of sentiments')
plt.xlabel('sentiment')
plt.ylabel('count')
plt.show()

# So, we can see althrough the app has low ratings, still the reviewers don't use many negative words in the reviews for the app.
 #Next, we'll explore the relationship between the sentiments and the ratings. This analysis can help us understand whether there is a correlation between the sentiment of the text and numerical ratings.

plt.figure(figsize=(10,5))
sns.countplot(data=df,
             x='Rating',
              hue='Sentiment')
plt.xlabel('Rating')
plt.ylabel('count')
plt.legend(title='Sentiment')
plt.show()

