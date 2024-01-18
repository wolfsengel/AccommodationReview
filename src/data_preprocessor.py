from ast import literal_eval

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer


def impute(column):
    column = column[0]
    if not isinstance(column, list):
        return "".join(literal_eval(column))
    else:
        return column


def process_text(text):
    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

    # Stem the tokens
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

    # Join the stemmed tokens back into a single string
    processed_text = ' '.join(stemmed_tokens)

    return processed_text


def preprocess_data(data):
    # Split country from hotel address so we can easily work with it
    data["countries"] = data.Hotel_Address.apply(lambda x: x.split(' ')[-1])

    # String 'list' of tags to an actual list
    data["Tags"] = data[["Tags"]].apply(impute, axis=1)

    # Lowercase countries and tags
    data['countries'] = data['countries'].str.lower()
    data['Tags'] = data['Tags'].str.lower()
    return data
