from matplotlib import pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
from src.data_loader import DataLoader
import seaborn as sns
# Load the data
data = DataLoader().load_data()

# Initialize the SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Remove 'No Negative' or 'No Positive' from text
data['Positive_Review'] = data['Positive_Review'].apply(lambda x: x.replace("No Positive", ""))
data['Negative_Review'] = data['Negative_Review'].apply(lambda x: x.replace("No Negative", ""))

# Create a new column 'Review' that contains the positive and negative review text
data['Review'] = data['Positive_Review'] + data['Negative_Review']
columns_to_drop = ['Hotel_Address', 'Additional_Number_of_Scoring', 'Review_Date', 'Reviewer_Nationality',
                   'Total_Number_of_Reviews', 'Average_Score', 'Tags', 'days_since_review',
                   'Total_Number_of_Reviews_Reviewer_Has_Given', 'days_since_review', 'lat', 'lng']

data.drop(columns=columns_to_drop, inplace=True)
# Apply the SentimentIntensityAnalyzer to the 'Negative_Review' column
sentiment_scores = data['Review'].apply(sia.polarity_scores)

# Add the sentiment scores as new columns in the dataframe
data['neg'] = sentiment_scores.apply(lambda x: x['neg'])
data['pos'] = sentiment_scores.apply(lambda x: x['pos'])
data['neu'] = sentiment_scores.apply(lambda x: x['neu'])
data['compound'] = sentiment_scores.apply(lambda x: x['compound'])

ax = sns.barplot(x='Reviewer_Score', y='compound', data=data)
ax.set_title('Sentiment Analysis Result')
plt.show()

# New barplot for pos, neg and neu
ax = sns.barplot(x='Reviewer_Score', y='pos', data=data)
ax.set_title('Positive Sentiment')
plt.show()

ax = sns.barplot(x='Reviewer_Score', y='neg', data=data)
ax.set_title('Negative Sentiment')
plt.show()

ax = sns.barplot(x='Reviewer_Score', y='neu', data=data)
ax.set_title('Neutral Sentiment')
plt.show()
