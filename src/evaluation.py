import pandas as pd
import wordcloud
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from src.data_preprocessor import clean_text
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import src.data_loader as dl

# Load the dataset
data = dl.DataLoader().load_data()

# append the positive and negative text reviews
data["review"] = data["Negative_Review"] + data["Positive_Review"]

# create the label
data["is_bad_review"] = data["Reviewer_Score"].apply(lambda x: 1 if x < 5 else 0)

# remove 'No Negative' or 'No Positive' from text
data["review"] = data["review"].apply(lambda x: x.replace("No Negative", "").replace("No Positive", ""))

# clean text data
data["review_clean"] = data["review"].apply(lambda x: clean_text(x))


def show_wordcloud(data, title=None):
    wordcloud = WordCloud(
        background_color='white',
        max_words=200,
        max_font_size=40,
        scale=3,
        random_state=42
    ).generate(str(data))

    fig = plt.figure(1, figsize=(20, 20))
    plt.axis('off')
    if title:
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.show()


# print wordcloud
show_wordcloud(data["review"])


def get_hotel_score(data, name, country):
    """
    :param data: the dataset
    :param name: the name of the hotel
    :param country: the country of the hotel
    :return: the score of the hotel
    """
    return data[(data["Hotel_Name"] == name) & (data["countries"] == country)]["Average_Score"].values[0]
