from sklearn.svm import SVC


class AccommodationModel:
    def __init__(self):
        self.model = SVC()

    def train_model(self, data):
        # Assume labels are present in the dataset
        self.model.fit(data['tfidf_matrix'], data['labels'])

    def predict(self, tfidf_matrix):
        return self.model.predict(tfidf_matrix)
