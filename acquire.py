# importing libraries
import os
import pandas as pd
import numpy as np

# importing sql libraries/modules
import env 
from env import user, password, host

# sklearn libraries and functions
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression


from prepare import log_features




def get_telco_data():
    # editing for "caching" exercise
    filename = "telco.csv"
    if os.path.isfile(filename):
        return pd.read_csv(filename, index_col=[0])
    else:
        db_url = f'mysql+pymysql://{user}:{password}@{host}/telco_churn'
        query = ''' 
        SELECT *
        FROM customers
        RIGHT JOIN contract_types using (contract_type_id)
        RIGHT JOIN payment_types using (payment_type_id)
        RIGHT JOIN internet_service_types using (internet_service_type_id)
        '''
        df = pd.read_sql(query, db_url)
        df.to_csv(filename)
        return df

def model_features(df):
    # returns specified features proved statistically significant from testing'
    df = df[[ 
        'churn', \
        'internet_service_type_fiber_optic', \
        'internet_service_type_dsl', \
        'internet_service_type_no_internet_service', \
        'payment_type_credit_card_automatic', \
        'payment_type_e_check', \
        'payment_type_mailed_check', \
        'payment_type_bank_transfer_automatic', \
        'streaming_movies_no_internet_service', \
        'streaming_movies_yes', \
        'streaming_movies_no',
        'tech_support_no_internet_service', \
        'tech_support_yes', \
        'tech_support_no']]

    return df

def log_features():
    features = [ 
    'internet_service_type_fiber_optic', \
    'internet_service_type_dsl', \
    'internet_service_type_no_internet_service', \
    'payment_type_credit_card_automatic', \
    'payment_type_e_check', \
    'payment_type_mailed_check', \
    'payment_type_bank_transfer_automatic', \
    'streaming_movies_no_internet_service', \
    'streaming_movies_yes', \
    'streaming_movies_no',
    'tech_support_no_internet_service', \
    'tech_support_yes', \
    'tech_support_no']

    return features


def model_results(X_train, y_train, X_validate, y_validate):
    features = log_features()
    metrics = []
    models = ["Logistic Regression", "KNN", "Decision Tree", "Random Forest"]

    for ele in models:
        if ele == "Logistic Regression":
            logit = LogisticRegression(random_state=123)
            logit = logit.fit(X_train[features], y_train)
            in_sample_accuracy = logit.score(X_train[features], y_train)
            out_of_sample_accuracy = logit.score(X_validate[features], y_validate)
        elif ele == "KNN":
            knn = KNeighborsClassifier(n_neighbors = 20, weights='uniform')
            knn = knn.fit(X_train, y_train)
            in_sample_accuracy = knn.score(X_train, y_train)
            out_of_sample_accuracy = knn.score(X_validate, y_validate)
        elif ele == "Decision Tree":
            tree = DecisionTreeClassifier(max_depth = 3, random_state = 123)
            tree = tree.fit(X_train, y_train)
            in_sample_accuracy = tree.score(X_train, y_train)
            out_of_sample_accuracy = tree.score(X_validate, y_validate)
        elif ele == "Random Forest":
            rf = RandomForestClassifier(min_samples_leaf = 4, max_depth = 4, random_state = 123)
            rf = rf.fit(X_train, y_train)
            in_sample_accuracy = rf.score(X_train, y_train)
            out_of_sample_accuracy = rf.score(X_validate, y_validate)

        output = {
            "Classification Model": ele, \
            "train_accuracy": in_sample_accuracy, \
            "validate_accuracy": out_of_sample_accuracy
        }
        
        metrics.append(output)
        
    df = pd.DataFrame(metrics)
    df["percent_change_diff"] = ((df.train_accuracy - df.validate_accuracy) / df.train_accuracy)
    df.round(3)
    return df