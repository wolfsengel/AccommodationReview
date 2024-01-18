from src.data_loader import DataLoader
from src.data_preprocessor import preprocess_data
from src.model import AccommodationModel
from src.evaluation import evaluate_model

DATA_PATH = 'C:\\Users\\angel\\PycharmProjects\\AccommodationReview\\data\\Accommodation_Reviews.csv'


def run_project():
    # Load data
    data_loader = DataLoader(DATA_PATH)
    data = data_loader.load_data()

    # Preprocess data
    processed_data = preprocess_data(data)

    # Train model
    model = AccommodationModel()
    model.train_model(processed_data)

    # Evaluate model
    evaluation_result = evaluate_model(model, processed_data)
    print("Evaluation Result:", evaluation_result)


if __name__ == "__main__":
    run_project()
