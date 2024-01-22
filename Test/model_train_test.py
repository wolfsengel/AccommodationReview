import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk

from src.data_loader import DataLoader

# Download NLTK resources (uncomment the following line if not already downloaded)
# nltk.download('punkt')
# nltk.download('stopwords')

# Load data from CSV
df = DataLoader().load_data()

# Text preprocessing using NLTK
stop_words = set(stopwords.words('english'))
ps = PorterStemmer()


def preprocess_text(text):
    words = word_tokenize(text)
    words = [ps.stem(word) for word in words if word.isalnum() and word.lower() not in stop_words]
    return ' '.join(words)


df['reviews'] = df['Negative_Review'] + df['Positive_Review']
df['label'] = df['Reviewer_Score'].apply(lambda x: 1 if x > 5 else 0)
df['processed_reviews'] = df['reviews'].apply(preprocess_text)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['processed_reviews'], df['label'], test_size=0.2,
                                                    random_state=42)

# Convert text data to feature vectors using CountVectorizer
vectorizer = CountVectorizer()
X_train_vectors = vectorizer.fit_transform(X_train)
X_test_vectors = vectorizer.transform(X_test)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train_vectors, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test_vectors)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Example usage of the model
new_reviews = ["I love this Hotel!", "The worst experience ever."]
new_reviews_processed = [preprocess_text(review) for review in new_reviews]
new_reviews_vectors = vectorizer.transform(new_reviews_processed)
predictions = classifier.predict(new_reviews_vectors)

for review, prediction in zip(new_reviews, predictions):
    sentiment = "Good" if prediction == 1 else "Bad"
    print(f"Review: {review} | Sentiment: {sentiment}")
