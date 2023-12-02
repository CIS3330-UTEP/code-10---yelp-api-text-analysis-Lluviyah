from yelpapi import YelpAPI
import pandas as pd

api_key = "ksoebnALf5ivymvDz1Q_p9SDUFZ2QL0_TBGw8709TW8ummNhjXkyUBRgo0Az-sIGhYxz7EFEuRHgjvv7FLg7Fq8E61OetYPwNhBM7hvlFsCgmFxe-sMYWY6bmGJMZXYx"

yelp_api_instance = YelpAPI(api_key)
search_term = 'pizza'
location_term = 'El Paso, TX'

search_results = yelp_api_instance.search_query(
    term=search_term, location=location_term,
    sort_by = 'rating', limit=20 #, offset=20
)


#print(search_results)

# for business in search_results['businesses']:
#     print('\n')
#     print(business)

id_for_reviews = 'little-habana-el-paso'

reviews_response = yelp_api_instance.reviews_query(id=id_for_reviews)


# for review in reviews_response['reviews']:
#     print("\n")
#     print(review)

##Using pandas

result_df = pd.DataFrame.from_dict(search_results['businesses'])
result_df.to_csv('api_result.csv',index=False)
print(result_df)


reviews_df =  pd.DataFrame.from_dict(search_results['reviews'])
reviews_df.to_csv('api_result2.csv',index=False)
print(reviews_df)

