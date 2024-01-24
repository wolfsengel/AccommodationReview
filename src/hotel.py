class Hotel:
    def __init__(self, name, average_score, data):
        """
        Class to store the hotel's information.

        :param name: the name of the hotel
        :param average_score: the average score of the hotel
        """
        self.name = name
        self.average_score = average_score
        self.worst_features = []
        self.best_features = []

    def __str__(self):
        """
        Method to print the hotel's information.
        """
        return f"Hotel: {self.name}\nAverage Score: {self.average_score}\n"
