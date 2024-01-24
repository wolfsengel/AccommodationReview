import time

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
current_time = time.time()

# Load the data
data = DataLoader().load_data()
print("Data Loaded in ", time.time() - current_time, " seconds")

# Remove 'No Negative' or 'No Positive' from the reviews
data['Negative_Review'] = data['Negative_Review'].apply(lambda x: x.replace('No Negative', ''))
data['Positive_Review'] = data['Positive_Review'].apply(lambda x: x.replace('No Positive', ''))

# Combine positive and negative reviews into a single column
data['Review'] = data['Positive_Review'] + data['Negative_Review']
print("Reviews Combined in ", time.time() - current_time, " seconds")

# Clean the reviews
data['Review'] = data['Review'].apply(lambda x: clean_text(x))
print("Reviews Cleaned in ", time.time() - current_time, " seconds")

# Just keep the positive and negative reviews, count of words in each review and the reviewer score
data = data[['Review', 'Review_Total_Positive_Word_Counts',
             'Review_Total_Negative_Word_Counts', 'Reviewer_Score']]

data['Is_Good_Review'] = data['Reviewer_Score'].apply(lambda x: 1 if x > MIN_SCORE else 0)
print("Data Processed\nStarting training")

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(data[['Review', 'Review_Total_Positive_Word_Counts',
                                                          'Review_Total_Negative_Word_Counts']], data['Is_Good_Review'],
                                                    test_size=0.3, random_state=42)

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
print("Training Complete in ", time.time() - current_time, " seconds")
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
print("END in ", time.time() - current_time, " seconds")


'''
Data Loaded in  2.0414106845855713  seconds
Reviews Combined in  2.332226037979126  seconds
Reviews Cleaned in  577.7847013473511  seconds
Data Processed
Starting training
Training Complete in  591.0267570018768  seconds
Accuracy:  0.9471956153617456
              precision    recall  f1-score   support

           0       0.62      0.29      0.40      9223
           1       0.96      0.99      0.97    145499

    accuracy                           0.95    154722
   macro avg       0.79      0.64      0.69    154722
weighted avg       0.94      0.95      0.94    154722

END in  682.8744542598724  seconds

Process finished with exit code 0

'''
