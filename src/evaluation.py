import pandas as pd
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer as  tfidf
from sklearn.metrics.pairwise import linear_kernel as lk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


nltk.download('stopwords')
nltk.download('punkt')

# Cargar el dataset
dataset = pd.read_csv('../data/Accommodation_Reviews.csv')

# Reducir el dataset a solo 1000 filas
dataset = dataset.iloc[:1000]

# Combinar las columnas relevantes para el análisis
dataset['review_negativa'] = dataset['Negative_Review'] + ' ' + dataset['Tags']

# Preprocesamiento de texto
stop_words = set(stopwords.words('english'))


def preprocess_text(text):
    # Tokenización y eliminación de stopwords
    tokens = word_tokenize(text.lower())
    tokens = [word for word in tokens if word.isalpha() and word not in stop_words]
    return ' '.join(tokens)


# Aplicar preprocesamiento al conjunto de datos
dataset['review_negativa'] = dataset['review_negativa'].apply(preprocess_text)

# Crear matriz TF-IDF para las revisiones negativas
tfidf_vectorizer_neg = tfidf()

tfidf_matrix_neg = tfidf_vectorizer_neg.fit_transform(dataset['review_negativa'])

# Calcular similitud entre revisiones negativas
cosine_sim_neg = lk(tfidf_matrix_neg, tfidf_matrix_neg)


# Función para obtener recomendaciones
def get_recommendations(hotel_index, similarity_matrix, n=5):
    sim_scores = list(enumerate(similarity_matrix[hotel_index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:n + 1]
    hotel_indices = [i[0] for i in sim_scores]
    return dataset['Hotel_Name'].iloc[hotel_indices]


# Ejemplo de recomendación para un hotel específico (cambia el índice según tu necesidad)
indice_hotel = 60
recommendations = get_recommendations(indice_hotel, cosine_sim_neg)

print(f"Recomendaciones para el hotel '{dataset['Hotel_Name'].iloc[indice_hotel]}':")
print(recommendations)
