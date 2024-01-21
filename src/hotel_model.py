from collections import Counter
from src.data_preprocessor import clean_text
from src.hotel import Hotel


def create_hotel_objects(data):
    """
    Function to create a hotel object for every hotel in the dataset.

    :param data: the dataset
    :return: a list of hotel objects
    """
    hotel_objects = []
    for hotel_name in data["Hotel_Name"].unique():
        hotel_data = data[data["Hotel_Name"] == hotel_name].copy()
        average_score = hotel_data["Average_Score"].iloc[0]
        hotel_object = Hotel(hotel_name, average_score, data)
        hotel_objects.append(hotel_object)
    return hotel_objects


def get_worst_values_for_hotel(data, hotel_name):
    """
    Function to get the most frequent words in negative reviews for a specific hotel.

    :param data: the dataset
    :param hotel_name: hotel name
    :return: a list of the 10 most frequent words in negative reviews for the hotel
    """

    # Filter the data for the specific hotel
    hotel_data = data[data['Hotel_Name'] == hotel_name]
    macro_list = []

    # Get the negative reviews into a single string
    for bad_review in hotel_data['Negative_Review']:
        bad_review = clean_text(bad_review)
        for word in bad_review.split():
            macro_list.append(word)

    # Get the 10 most frequent words
    macro_list = Counter(macro_list).most_common(10)

    return macro_list


def get_best_values_for_hotel(data, hotel_name):
    """
    Function to get the most frequent words in positive reviews for a specific hotel.

    :param data: the dataset
    :param hotel_name: hotel name
    :return: a list of the 10 most frequent words in positive reviews for the hotel
    """

    # Filter the data for the specific hotel
    hotel_data = data[data['Hotel_Name'] == hotel_name]
    macro_list = []

    # Get the positive reviews into a single string
    for good_review in hotel_data['Positive_Review']:
        good_review = clean_text(good_review)
        for word in good_review.split():
            macro_list.append(word)

    # Get the 10 most frequent words
    macro_list = Counter(macro_list).most_common(10)

    return macro_list
