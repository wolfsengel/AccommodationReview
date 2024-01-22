import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from scipy.sparse import hstack
# nltk

from src.data_loader import DataLoader

# Download NLTK resources (uncomment the following line if not already downloaded)
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('wordnet')

MIN_SCORE = 6

# Load data from CSV
df = DataLoader().load_data()

# Text preprocessing using NLTK
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    words = word_tokenize(text)
    words = [lemmatizer.lemmatize(word) for word in words if word.isalnum() and word.lower() not in stop_words]
    return ' '.join(words)


# Select relevant columns
df = df[['Negative_Review', 'Positive_Review', 'Reviewer_Score', 'Review_Total_Positive_Word_Counts',
         'Review_Total_Negative_Word_Counts']]

# Remove 'No Negative' or 'No Positive' from text
df['Negative_Review'] = df['Negative_Review'].apply(lambda x: x.replace("No Negative", ""))
df['Positive_Review'] = df['Positive_Review'].apply(lambda x: x.replace("No Positive", ""))

# Combine the positive and negative reviews
df['reviews'] = df['Negative_Review'] + df['Positive_Review']

# Create the label
df['label'] = df['Reviewer_Score'].apply(lambda x: 1 if x > MIN_SCORE else 0)

# Clean text data
df['processed_reviews'] = df['reviews'].apply(preprocess_text)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df[['processed_reviews', 'Review_Total_Positive_Word_Counts',
                                                        'Review_Total_Negative_Word_Counts']], df['label'],
                                                    test_size=0.2, random_state=42)

# Convert text data to feature vectors using TF-IDF Vectorizer
vectorizer = TfidfVectorizer()
X_train_text_vectors = vectorizer.fit_transform(X_train['processed_reviews'])
X_test_text_vectors = vectorizer.transform(X_test['processed_reviews'])

# Combine text features with other features
X_train_combined = hstack([X_train_text_vectors,
                           np.array(
                               X_train[['Review_Total_Positive_Word_Counts', 'Review_Total_Negative_Word_Counts']])])

X_test_combined = hstack([X_test_text_vectors,
                          np.array(X_test[['Review_Total_Positive_Word_Counts', 'Review_Total_Negative_Word_Counts']])])

# Train a Support Vector Machine classifier
classifier = SVC(kernel='linear')
classifier.fit(X_train_combined, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test_combined)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Classification report
print("Classification Report:")
print(classification_report(y_test, y_pred))
"""
# Example usage of the model
new_reviews = ["I love this Hotel!", "The worst experience ever.", "I will never come back again.",
               "I hate this hotel.", "I dislike this hotel.",
               "I had a bad time here it was awful, bad smell and dirty room."]
new_reviews_processed = [preprocess_text(review) for review in new_reviews]
new_reviews_text_vectors = vectorizer.transform(new_reviews_processed)

# Combine text features with other features for new reviews
new_reviews_combined = hstack([new_reviews_text_vectors,
                               np.array([[len(word_tokenize(review)) for review in new_reviews],
                                         [len(word_tokenize(review)) for review in new_reviews]]).T])


predictions = classifier.predict(new_reviews_combined)

for review, prediction in zip(new_reviews, predictions):
    sentiment = "Good" if prediction == 1 else "Bad"
    print(f"Review: {review} | Sentiment: {sentiment}")
"""