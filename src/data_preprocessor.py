import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer


class DataPreprocessor:
    def preprocess_data(self, data):
        # Combine Positive and Negative reviews for better context
        data['combined_reviews'] = data['Positive_Review'] + ' ' + data['Negative_Review']

        # Tokenization, stop words removal, and stemming
        data['processed_reviews'] = data['combined_reviews'].apply(self.process_text)

        # TF-IDF Vectorization
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(data['processed_reviews'])

        data['tfidf_matrix'] = list(tfidf_matrix)

        return data

    def process_text(self, text):
        # Tokenize the text
        tokens = word_tokenize(text)

        # Remove stop words
        stop_words = set(stopwords.words('english'))
        filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

        # Stem the tokens
        stemmer = PorterStemmer()
        stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]

        # Join the stemmed tokens back into a single string
        processed_text = ' '.join(stemmed_tokens)

        return processed_text
