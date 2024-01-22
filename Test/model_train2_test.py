from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

from src.data_loader import DataLoader

# Load the data
data = DataLoader().load_data()

# Combine positive and negative reviews into a single column
data['Review'] = data['Positive_Review'] + data['Negative_Review']

# Define a threshold for a good review
threshold = 5
data['Is_Good_Review'] = data['Reviewer_Score'].apply(lambda x: 1 if x > threshold else 0)

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data[['Review', 'Review_Total_Positive_Word_Counts',
                                                          'Review_Total_Negative_Word_Counts']], data['Is_Good_Review'],
                                                    test_size=0.2, random_state=42)

# Create a pipeline for text and numeric features
preprocessor = ColumnTransformer(
    transformers=[
        ('text', CountVectorizer(), 'Review'),
        ('num', StandardScaler(), ['Review_Total_Positive_Word_Counts', 'Review_Total_Negative_Word_Counts'])
    ])

# Create a pipeline with our preprocessor and classifier
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

# Train the model
pipeline.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = pipeline.predict(X_test)

# Print the classification report
print(classification_report(y_test, y_pred))
