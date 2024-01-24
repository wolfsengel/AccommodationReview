from matplotlib import pyplot as plt

from src.data_loader import DataLoader
from wordcloud import WordCloud

from src.data_preprocessor import clean_text

# Load data
data_loader = DataLoader()
data = data_loader.load_data()

# Unify the text in the 'Positive_Review' and 'Negative_Review' columns
data['Positive_Review'] = data['Positive_Review'].apply(lambda x: x.replace("No Positive", ""))
data['Negative_Review'] = data['Negative_Review'].apply(lambda x: x.replace("No Negative", ""))
data['Review'] = data['Positive_Review'] + data['Negative_Review']

# Clean the text
data['Review'] = data['Review'].apply(clean_text)
# Wordcloud
wordcloud = WordCloud(
    background_color='white',
    max_words=200,
    max_font_size=40,
    scale=3,
    random_state=42
).generate(str(data['Review']))

fig = plt.figure(1, figsize=(20, 20))
plt.axis('off')
plt.imshow(wordcloud)
plt.show()

