import numpy as np
from nltk import word_tokenize, WordNetLemmatizer, data
from nltk.corpus import stopwords
from sklearn.svm import SVC


stop_words = set(stopwords.words('english'))
lemm = WordNetLemmatizer()


def recommend_hotel(data, location, description):
    description_tokens = word_tokenize(description.lower())
    filtered = {word for word in description_tokens if not word in stop_words}
    filtered_set = set([lemm.lemmatize(word) for word in filtered])

    country = data[data['countries']==location.lower()]
    country = country.set_index(np.arange(country.shape[0]))
    list1 = []
    list2 = []
    cos = []
    for i in range(country.shape[0]):
        temp_token = word_tokenize(country["Tags"][i])
        temp_set = [word for word in temp_token if not word in stop_words]
        temp2_set = set()
        for s in temp_set:
            temp2_set.add(lemm.lemmatize(s))
        vector = temp2_set.intersection(filtered_set)
        cos.append(len(vector))
    country['similarity']=cos
    country = country.sort_values(by='similarity', ascending=False)
    country.drop_duplicates(subset='Hotel_Name', keep='first', inplace=True)
    country.sort_values('Average_Score', ascending=False, inplace=True)
    country.reset_index(inplace=True)
    return country[["Hotel_Name", "Average_Score", "Hotel_Address"]].head()


class AccommodationModel:
    def __init__(self):
        self.model = SVC()

    def train_model(self, data):
        # Assume labels are present in the dataset
        self.model.fit(data['tfidf_matrix'], data['labels'])

    def predict(self, tfidf_matrix):
        return self.model.predict(tfidf_matrix)
