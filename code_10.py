import nltk
from nltk.corpus import stopwords
from yelpapi import YelpAPI
import pandas as pd

api_key = "ksoebnALf5ivymvDz1Q_p9SDUFZ2QL0_TBGw8709TW8ummNhjXkyUBRgo0Az-sIGhYxz7EFEuRHgjvv7FLg7Fq8E61OetYPwNhBM7hvlFsCgmFxe-sMYWY6bmGJMZXYx"

yelp_api_instance = YelpAPI(api_key)

search_term = 'coffee'
location_term = 'El Paso, TX'

search_results = yelp_api_instance.search_query(
    term=search_term, location=location_term,
    sort_by = 'rating', limit=5
)


id_for_reviews = ['proof-and-press-el-paso','frontera-churros-el-paso','café-con-leche-el-paso-6','viejo-coffee-el-paso-4','frontera-churros-coffee-and-beer-el-paso']

# for i in id_for_reviews:
#     review_response = yelp_api_instance.reviews_query(id=i)
#     for review in review_response['reviews']:
#         print("\n")
#         print(review)
       
    


# reviews_df =  pd.DataFrame.from_dict(search_results['reviews'])
# reviews_df.to_csv('api_result2.csv',index=False)
# print(reviews_df)


result_df = pd.DataFrame.from_dict(search_results['businesses'])
result_df.to_csv('api_result.csv',index=False)
print(result_df)


rev_df = pd.DataFrame.from_dict(search_results['reviews'])
rev_df.to_csv('api_reviews.csv',index=False)
print(result_df)





#######
# reviews = open('api_result.csv')
# stop_words = set(stopwords.words('english'))




# reviews_df =  pd.DataFrame.from_dict(search_results['reviews'])
# reviews_df.to_csv('api_result.csv',index=False)
# print(reviews_df)





# # /////
# ###
# for review in reviews:
#     print('')
#     # print(review)
#     tokens = nltk.word_tokenize(review)
#     #print(tokens)
#     pos_tags = nltk.pos_tag(tokens)
#     #print(pos_tags)
#     new_text = []
#     for tag in pos_tags:
#         # if tag[1] == 'NN' or tag[1] == 'NNP' or tag[1] == 'NNS':
#         #     print(tag)
#         if tag [0] not in stop_words:
#             new_text.append(tag[0])
#     print('\nOriginal')
#     print(review)
#     print('\nNew')
#     print(" ".join(new_text))
# ####