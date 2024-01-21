from ast import literal_eval


def impute(column):
    column = column.iloc[0]  # Use iloc for positional indexing
    if not isinstance(column, list):
        return "".join(literal_eval(column))
    else:
        return column


def preprocess_data(data):
    # Remove not useful columns
    columns_to_drop = ['Additional_Number_of_Scoring',
                       'Review_Date', 'Reviewer_Nationality',
                       'Negative_Review', 'Review_Total_Negative_Word_Counts',
                       'Total_Number_of_Reviews', 'Positive_Review',
                       'Review_Total_Positive_Word_Counts',
                       'Total_Number_of_Reviews_Reviewer_Has_Given', 'Reviewer_Score',
                       'days_since_review', 'lat', 'lng']
    data.drop(columns=columns_to_drop, inplace=True)

    # United Kingdom is the same as UK
    data['Hotel_Address'] = data['Hotel_Address'].str.replace('United Kingdom', 'UK')

    # Split country from hotel address, so we can easily work with it
    data["countries"] = data.Hotel_Address.apply(lambda x: x.split(' ')[-1])

    # String 'list' of tags to an actual list
    data["Tags"] = data[["Tags"]].apply(impute, axis=1)

    # Lowercase countries and tags
    data['countries'] = data['countries'].str.lower()
    data['Tags'] = data['Tags'].str.lower()
    return data
