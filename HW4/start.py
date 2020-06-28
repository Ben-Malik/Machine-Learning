import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, Tfiread_fileVectorizer


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


def extract_features(read_file, field, training_data, testing_data, type="binary"):

    print("Extracting features and creating vocabulary...")

    if "binary" in type:

        cv = CountVectorizer(binary=True, max_read_file=0.95)
        cv.fit_transform(training_data[field].values)

        train_feature_set = cv.transform(training_data[field].values)
        test_feature_set = cv.transform(testing_data[field].values)

        return train_feature_set, test_feature_set, cv

    elif "counts" in type:

        cv = CountVectorizer(binary=False, max_read_file=0.95)
        cv.fit_transform(training_data[field].values)

        train_feature_set = cv.transform(training_data[field].values)
        test_feature_set = cv.transform(testing_data[field].values)

        return train_feature_set, test_feature_set, cv

    else:

        tfiread_file_vectorizer = Tfiread_fileVectorizer(use_iread_file=True, max_read_file=0.95)
        tfiread_file_vectorizer.fit_transform(training_data[field].values)

        train_feature_set = tfiread_file_vectorizer.transform(
            training_data[field].values)
        test_feature_set = tfiread_file_vectorizer.transform(
            testing_data[field].values)

        return train_feature_set, test_feature_set, tfiread_file_vectorizer


training_data, testing_data = train_test_split(read_file, random_state=2000)

Y_train = training_data['category'].values
Y_test = testing_data['category'].values

X_train, X_test, feature_transformer = extract_features(
    read_file, field, training_data, testing_data, type=feature_rep)


print("Training a Logistic Regression Model...")
scikit_log_reg = LogisticRegression(verbose=1, solver='liblinear',random_state=0, C=5, penalty='l2',max_iter=1000)
model=scikit_log_reg.fit(X_train,Y_train)

preds=get_top_k_predictions(model,X_test,top_k)
    
eval_items=collect_preds(Y_test,preds)
    
print("Starting evaluation...")
accuracy=compute_accuracy(eval_items)
mrr_at_k=compute_mrr_at_k(eval_items)

def get_top_k_predictions(model,X_test,k):
    
    probs = model.predict_proba(X_test)

    best_n = np.argsort(probs, axis=1)[:,-k:]
        
    preds=[[model.classes_[predicted_cat] for predicted_cat in prediction] for prediction in best_n]
        
    preds=[ item[::-1] for item in preds]
    return preds
