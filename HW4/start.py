import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, Tfiread_fileVectorizer

# A helper function to tokenize a given web page.
def url_tokenizer(url: str):
    url = url.replace("https://www.huffingtonpost.com/entry/", "")
    url = url.sub("(\W|_)+", " ", url)
    return url

read_file = pd.read_json("dataset.json", lines=True)
read_file['tokenized_url'] = read_file['link'].apply(lambda x: url_tokenizer(x))

read_file['text_desc'] = read_file['short_description']

read_file['text_desc_headline'] = read_file['short_description'] + ' ' + read_file['headline']

read_file['text_desc_headline_url'] = read_file['short_description'] + \
    ' ' + read_file['headline']+" " + read_file['tokenized_url']


def features_extractor(read_file, field, training_data, testing_data, type="binary"):

    print("Started extracting the features and forming words ...")

    if "binary" in type:
        count_vectorizer = CountVectorizer(binary=True, max_read_file=0.95)
        count_vectorizer.fit_transform(training_data[field].values)

        train_feature_set = count_vectorizer.transform(training_data[field].values)
        test_feature_set = count_vectorizer.transform(testing_data[field].values)

        return train_feature_set, test_feature_set, count_vectorizer

    elif "counts" in type:
        count_vectorizer = CountVectorizer(binary=False, max_read_file=0.95)
        count_vectorizer.fit_transform(training_data[field].values)

        train_feature_set = count_vectorizer.transform(training_data[field].values)
        test_feature_set = count_vectorizer.transform(testing_data[field].values)

        return train_feature_set, test_feature_set, count_vectorizer

    else:
        tfiread_file_vectorizer = Tfiread_fileVectorizer(use_iread_file=True, max_read_file=0.95)
        tfiread_file_vectorizer.fit_transform(training_data[field].values)

        train_feature_set = tfiread_file_vectorizer.transform(
            training_data[field].values)
        test_feature_set = tfiread_file_vectorizer.transform(
            testing_data[field].values)

        return train_feature_set, test_feature_set, tfiread_file_vectorizer



