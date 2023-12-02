import nltk
from nltk.corpus import stopwords

reviews = open('ice_cream_reviews.txt')
stop_words = set(stopwords.words('english'))

for review in reviews:
    print('')
    # print(review)
    tokens = nltk.word_tokenize(review)
    #print(tokens)
    pos_tags = nltk.pos_tag(tokens)
    #print(pos_tags)
    new_text = []
    for tag in pos_tags:
        # if tag[1] == 'NN' or tag[1] == 'NNP' or tag[1] == 'NNS':
        #     print(tag)
        if tag [0] not in stop_words:
            new_text.append(tag[0])
    print('\nOriginal')
    print(review)
    print('\nNew')
    print(" ".join(new_text))