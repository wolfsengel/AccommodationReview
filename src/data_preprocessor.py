import string
from ast import literal_eval

from nltk import WordNetLemmatizer, pos_tag
from nltk.corpus import wordnet, stopwords

lemm = WordNetLemmatizer()


def impute(column):
    """
        Used to impute the tags column

        :param column:
        :return: column after imputing:
    """
    column = column.iloc[0]  # Use iloc for positional indexing
    if not isinstance(column, list):
        return "".join(literal_eval(column))
    else:
        return column


def preprocess_data(data):
    """
        Preprocess the data
        :param data: the dataset to be preprocessed
        :return data after preprocessing:
    """
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


def get_wordnet_pos(pos_tag_text):
    """
    Used to get the pos tag of the word
    :param pos_tag_text: the pos tag of the word
    :return pos_tag:
    """
    if pos_tag_text.startswith('J'):
        return wordnet.ADJ
    elif pos_tag_text.startswith('V'):
        return wordnet.VERB
    elif pos_tag_text.startswith('N'):
        return wordnet.NOUN
    elif pos_tag_text.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN


def clean_text(text):
    """
        Clean the text data
        1. Lowercase the text
        2. Tokenize the text
        3. Remove punctuation
        4. Remove words that contain numbers
        5. Remove stop words
        6. Remove empty tokens
        7. Lemmatize text
        8. Remove words with only one letter

        :param text: the string to be cleaned
        :return text: the cleaned string
    """
    # lower text
    text = text.lower()
    # tokenize text and remove punctuation
    text = [word.strip(string.punctuation) for word in text.split(" ")]
    # remove words that contain numbers
    text = [word for word in text if not any(c.isdigit() for c in word)]
    # remove stop words
    stop = stopwords.words('english')
    text = [x for x in text if x not in stop]
    # remove empty tokens
    text = [t for t in text if len(t) > 0]
    pos_tags = pos_tag(text)
    # lemmatize text
    text = [WordNetLemmatizer().lemmatize(t[0], get_wordnet_pos(t[1])) for t in pos_tags]
    # remove words with only one letter
    text = [t for t in text if len(t) > 1]
    # join all
    text = " ".join(text)
    return text
