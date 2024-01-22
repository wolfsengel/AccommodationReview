import pandas as pd
import matplotlib.pyplot as plt

from src.data_loader import DataLoader


def analyze_reviews(data):
    if data is not None:
        positive_reviews = data[data['Reviewer_Score'] > 5]

        # Define conditions for different types of reviews
        positive_and_negative = positive_reviews[(positive_reviews['Positive_Review'] != 'No Positive') &
                                                 (positive_reviews['Negative_Review'] != 'No Negative')]
        positive_no_negative = positive_reviews[(positive_reviews['Positive_Review'] != 'No Positive') &
                                                (positive_reviews['Negative_Review'] == 'No Negative')]
        no_positive_negative = positive_reviews[(positive_reviews['Positive_Review'] == 'No Positive') &
                                                (positive_reviews['Negative_Review'] != 'No Negative')]
        no_positive_no_negative = positive_reviews[(positive_reviews['Positive_Review'] == 'No Positive') &
                                                   (positive_reviews['Negative_Review'] == 'No Negative')]

        # Count the number of reviews for each category
        num_positive_and_negative = len(positive_and_negative)
        num_positive_no_negative = len(positive_no_negative)
        num_no_positive_negative = len(no_positive_negative)
        num_no_positive_no_negative = len(no_positive_no_negative)

        # Plotting
        labels = ['Positive and Negative', 'Positive but No Negative', 'No Positive but Negative',
                  'No Positive and No Negative']
        values = [num_positive_and_negative, num_positive_no_negative, num_no_positive_negative,
                  num_no_positive_no_negative]

        fig, ax = plt.subplots()

        # Plot the bars
        bars = plt.bar(labels, values)

        # Add count labels on top of the bars
        for bar, value in zip(bars, values):
            plt.text(bar.get_x() + bar.get_width() / 2 - 0.15, bar.get_height() + 0.1, str(value), ha='center')

        plt.title('Positive Reviews Analysis')
        plt.xlabel('Review Type')
        plt.ylabel('Number of Reviews')
        plt.show()


if __name__ == "__main__":
    # Load the dataset
    data = DataLoader().load_data()
    analyze_reviews(data)
