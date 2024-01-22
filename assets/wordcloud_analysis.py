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

# Remove 'No Negative' or 'No Positive' from text
data['Positive_Review'] = data['Positive_Review'].apply(lambda x: x.replace("No Positive", ""))
data['Negative_Review'] = data['Negative_Review'].apply(lambda x: x.replace("No Negative", ""))

# Create a new column 'Review' that contains the positive and negative review text
data['Review'] = data['Positive_Review'] + data['Negative_Review']
columns_to_drop = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Reviewer_Nationality',
                   'Total_Number_of_Reviews', 'Average_Score', 'Tags', 'days_since_review',
                   'Total_Number_of_Reviews_Reviewer_Has_Given', 'days_since_review', 'lat', 'lng']

data.drop(columns=columns_to_drop, inplace=True)

# Generate a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(data['Review'].to_string())

# Display the generated word cloud using matplotlib
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
