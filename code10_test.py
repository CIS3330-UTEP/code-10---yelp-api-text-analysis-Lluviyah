from yelpapi import YelpAPI
import pandas as pd

api_key = "ksoebnALf5ivymvDz1Q_p9SDUFZ2QL0_TBGw8709TW8ummNhjXkyUBRgo0Az-sIGhYxz7EFEuRHgjvv7FLg7Fq8E61OetYPwNhBM7hvlFsCgmFxe-sMYWY6bmGJMZXYx"

yelp_api = YelpAPI(api_key)
search_term = 'coffee'
location_term = 'El Paso, TX'

#gather the top 5 coffee shops
search_results = yelp_api.search_query(
    term=search_term, location=location_term,
    sort_by = 'rating', limit=5
)

#create csv file with top 5 coffee shops
result_df = pd.DataFrame.from_dict(search_results['businesses'])
result_df.to_csv("api_result.csv")

#create csv file with all 15 reviews, 3 per each of the coffee shops. 
all_reviews_df = pd.DataFrame()

for index, row in result_df.iterrows():
    business_alias = row['alias']
    review = yelp_api.reviews_query(id=business_alias)

    business_reviews_df = pd.DataFrame.from_dict(review['reviews'])
    business_reviews_df['business_alias'] = business_alias
    all_reviews_df = pd.concat([all_reviews_df, business_reviews_df], ignore_index=True)

all_reviews_df.to_csv("reviews_results.csv")

### Extract only the reviews and business alias
#Using vector to separate the columns i want to use
def get_reviews_alias(row):
    review = row['text']
    alias = row['business_alias']
    new_row = {"Review":review , "Alias": alias}
    return pd.Series(new_row)

#read the csv file with the info needed
df = pd.read_csv('reviews_results.csv')
#create an empty df
only_reviews_df = pd.DataFrame()

##print(df.apply(get_reviews_alias,axis=1))

##Iterate through data frame to catch every row with the selected columns in the get_reviews_alias function. 
for index, row in all_reviews_df.iterrows(): 
    x = df.apply(get_reviews_alias,axis=1)
    only_reviews_df = pd.concat([x],ignore_index=True)
   
only_reviews_df.to_csv("only_reviews.txt")


#We now begin our text analysis based on the reviews_results

reviews = open('only_reviews.txt')

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
for i in reviews:
    sentiment_score = analyzer.polarity_scores(i)
#     print(i)
    print(sentiment_score)
    


import nltk
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

for review in reviews:
    print('')
    # print(review)
    tokens = nltk.word_tokenize(review)
    print(tokens)
    pos_tags = nltk.pos_tag(tokens)
    #print(pos_tags)
    new_text = []
    for tag in pos_tags:
        if tag[1] == 'JJ' or tag[1] == 'JJR' or tag[1] == 'JJS':
            print(tag)
        elif tag [0] not in stop_words:
            new_text.append(tag[0])
    print('\nOriginal')
    print(review)
    print('\nNew')
    print(" ".join(new_text))

from nltk import FreqDist
count = 0
for review in reviews:
    if review == 0:  
        continue
    count += 1
    tokens = nltk.word_tokenize(review)
    filtered_tokens = [token for token in tokens if len(token) > 3]
    freq_dist = FreqDist(filtered_tokens)
    print("Most common words:", freq_dist.most_common())
    print('\n')


   

