# needed modules:
import os
import pymysql
import pandas as pd
import env 
from env import user, password, host



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


def clean_telco_data(df):
    df["total_charges"] = pd.to_numeric(df["total_charges"], errors="coerce")
    filling_values = df[df.isnull().any(axis=1)].monthly_charges
    df["total_charges"] = df["total_charges"].fillna(df["monthly_charges"])
    df = df.drop(columns=['internet_service_type_id', 'payment_type_id', 'contract_type_id'])
    df["senior_citizen"] = df["senior_citizen"].replace({0: "No", 1: "Yes"})
    categorical_lst = ['internet_service_type', \ 
       'payment_type', \
       'contract_type', \
       'gender', \
       'senior_citizen', \
       'partner', \
       'dependents', \
       'phone_service', \
       'multiple_lines', \
       'online_security', \
       'online_backup', \
       'device_protection', \
       'tech_support', \
       'streaming_tv', \
       'streaming_movies', \
       'paperless_billing']
    dummy_df = pd.get_dummies(df[categorical_lst], drop_first=True)
    df = pd.concat([df, dummy_df], axis = 1)
    
    for column in df.columns:
        if df[column].dtype == "uint8":
            df[column] = df[column].astype("bool")