from sklearn.metrics import accuracy_score


def evaluate_model(model, data):
    # Assume you have labels in your dataset, modify accordingly
    predictions = model.predict(data['tfidf_matrix'])
    accuracy = accuracy_score(data['labels'], predictions)
    return accuracy
