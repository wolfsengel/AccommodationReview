from src.data_loader import DataLoader
from src.data_preprocessor import DataPreprocessor
from src.model import AccommodationModel
from src.evaluation import evaluate_model


def run_project():
    # Load data
    data_loader = DataLoader('your_dataset.csv')
    data = data_loader.load_data()

    # Preprocess data
    data_preprocessor = DataPreprocessor()
    processed_data = data_preprocessor.preprocess_data(data)

    # Train model
    model = AccommodationModel()
    model.train_model(processed_data)

    # Evaluate model
    evaluation_result = evaluate_model(model, processed_data)
    print("Evaluation Result:", evaluation_result)


if __name__ == "__main__":
    run_project()
