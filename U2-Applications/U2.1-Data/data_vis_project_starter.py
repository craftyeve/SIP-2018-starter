'''
In this project, you will visualize the feelings and language used in a set of
Tweets. This starter code loads the appropriate libraries and the Twitter data you'll
need!
'''

import json
from textblob import TextBlob
import matplotlib.pyplot as plt

#Get the JSON data
tweetFile = open("TwitterData/tweets_small.json", "r")
tweetData = json.load(tweetFile)
tweetFile.close()

# Continue your program below! 
tweetstring = ""
for tweet in tweetData:
    tweetstring += tweet['text']

# print(tweetstring)

blob_string = TextBlob(tweetstring)

filteredWords = {}
for word in blob_string.words:
    filteredWords[word.lower()] = blob_string.word_counts[word.lower()]

# print(filteredWords)

tweet_text = []
for tweet in tweetData:
    tweet_text.append(tweet["text"])

# print(tweet_text)

tweets_tb = []
for tweet in tweet_text:
    tweets_tb.append(TextBlob(tweet))

# print(tweets_tb)

polarity = []
subjectivity = []
for tb in tweets_tb:
    polarity.append(tb.polarity)
    subjectivity.append(tb.subjectivity)

avg_polarity = sum(polarity) / len(polarity)
avg_subjectivity = sum(subjectivity) / len(subjectivity)

# print(avg_polarity)
# print(avg_subjectivity)

# plt.hist(polarity, bins=[-1, -.9, -.8, -.7, -.6, -.5, -.4, -.3, -.2, -.1, 0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
# plt.xlabel('Polarity')
# plt.ylabel('Number of occurances')
# plt.title('Histogram of Polarity of Tweets')
# plt.axis([-1, 1, 0, 50])
# plt.grid(False)
# plt.show()

# plt.hist(subjectivity, bins=[0, .1, .2, .3, .4, .5, .6, .7, .8, .9, 1])
# plt.xlabel('Subjectivity')
# plt.ylabel('Number of occurances')
# plt.title('Histogram of Subjectivity of Tweets')
# plt.axis([0, 1, 0, 50])
# plt.grid(False)
# plt.show()

# Textblob sample:
# tb = TextBlob("You are a brilliant computer scientist.")
# print(tb.sentiment)