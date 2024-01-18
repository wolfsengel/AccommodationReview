import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from scripts.run_project import DATA_PATH

# Load the data
data = pd.read_csv(DATA_PATH)

# Combine positive and negative reviews into a single column
data['Text'] = data['Positive_Review'] + ' ' + data['Negative_Review']

# Create a binary column indicating sentiment (1 for positive, 0 for negative)
data['Sentiment'] = (data['Reviewer_Score'] > 7.5).astype(int)

# Drop unnecessary columns
data = data[['Text', 'Sentiment']]

# Text preprocessing (tokenization, stop word removal, lemmatization)
# You may need to customize this based on your specific requirements
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X = vectorizer.fit_transform(data['Text'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, data['Sentiment'], test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
predictions = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy:.2f}')

# Display additional metrics
print(classification_report(y_test, predictions))

