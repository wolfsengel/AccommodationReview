import numpy as np
from matplotlib import pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_curve, roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler

from src.data_loader import DataLoader
from src.data_preprocessor import clean_text

MIN_SCORE = 5
# Load the data
data = DataLoader().load_data()

# Remove 'No Negative' or 'No Positive' from the reviews
data['Negative_Review'] = data['Negative_Review'].apply(lambda x: x.replace('No Negative', ''))
data['Positive_Review'] = data['Positive_Review'].apply(lambda x: x.replace('No Positive', ''))

# Combine positive and negative reviews into a single column
data['Review'] = data['Positive_Review'] + data['Negative_Review']

# Clean the reviews
data['Review'] = data['Review'].apply(lambda x: clean_text(x))

# Just keep the positive and negative reviews, count of words in each review and the reviewer score
data = data[['Review', 'Review_Total_Positive_Word_Counts',
             'Review_Total_Negative_Word_Counts', 'Reviewer_Score']]

data['Is_Good_Review'] = data['Reviewer_Score'].apply(lambda x: 1 if x > MIN_SCORE else 0)

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
    ('classifier', LogisticRegression(max_iter=1000))  # Increase max_iter to 1000 to avoid ConvergenceWarning
])

# Train the model
pipeline.fit(X_train, y_train)

# Predict the labels of the test set
y_pred = pipeline.predict(X_test)

# Print accuracy score
print('Accuracy: ', pipeline.score(X_test, y_test))

# Print the classification report
print(classification_report(y_test, y_pred))

# Confusion Matrix
# disp = plot_confusion_matrix(pipeline, X_test, y_test, cmap=plt.cm.Blues, normalize='true')
# disp.ax_.set_title('Confusion Matrix')
# plt.show()

# ROC Curve and AUC
y_prob = pipeline.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = roc_auc_score(y_test, y_prob)

plt.figure()
plt.plot(fpr, tpr, lw=2, label='ROC curve (AUC = {:.2f})'.format(roc_auc))
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend(loc='lower right')
plt.show()


def predict_review(review):
    return pipeline.predict([review])[0]
